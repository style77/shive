import random
import string
from typing import List
import graphene
from sqlmodel import select

from api.users.models import User, UserCreate
from api.users.services import service
from api.database import async_session


class UserGraphene(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    full_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    is_active = graphene.Boolean()


class CreateUserFailOther(graphene.ObjectType):
    error_message = graphene.String(required=True)


class CreateUserFailUsernameExists(CreateUserFailOther):
    suggested_alternatives = graphene.List(graphene.String)


class CreateUserSuccess(graphene.ObjectType):
    user = graphene.Field(UserGraphene, required=True)


class CreateUserPayload(graphene.Union):
    class Meta:
        types = (CreateUserFailUsernameExists, CreateUserFailOther, CreateUserSuccess)


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        full_name = graphene.String(required=True)
        password = graphene.String(required=True)

    Output = CreateUserPayload

    @staticmethod
    async def _username_exists(username: str) -> bool:
        """
        Check if a username exists in the database.

        :param username: The username to check.
        :return: True if the username exists, False otherwise.
        """
        async with async_session() as session:
            result = await session.execute(
                select(User).where(User.username == username)
            )
            return result.scalars().first() is not None

    @staticmethod
    async def _get_alternative_usernames(username: str, *, count: int = 5) -> List[str]:
        """
        Generate a list of alternative usernames based on the given username.
        The generated usernames are checked against the database to ensure they are unique.

        :param username: The username to generate alternatives for.
        :param count: The number of alternatives to generate.
        :return: A list of alternative usernames.
        """
        alternatives = []
        suffixes = set()

        while len(suffixes) < count:
            numeric_suffix = random.randint(10, 99)
            random_suffix = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=3)
            )
            suffixes.add(f"{numeric_suffix}{random_suffix}")

        async with async_session() as session:
            existing_usernames_query = select(User.username).where(
                User.username.in_([f"{username}_{suffix}" for suffix in suffixes])
            )
            result = await session.execute(existing_usernames_query)
            existing_usernames = {row[0] for row in result.all()}

        filtered_suffixes = [
            suffix
            for suffix in suffixes
            if f"{username}_{suffix}" not in existing_usernames
        ]

        for suffix in filtered_suffixes[:count]:
            alternatives.append(f"{username}_{suffix}")

        while len(alternatives) < count:
            unique_suffix = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=5)
            )
            proposed_username = f"{username}_{unique_suffix}"
            if proposed_username not in alternatives:
                alternatives.append(proposed_username)

        return alternatives

    async def mutate(root, info, username, email, full_name, password):
        """
        Create a new user.

        :param root: The root object.
        :param info: The info object.
        :param username: The username of the new user.
        :param email: The email of the new user.
        :param full_name: The full name of the new user.
        :param password: The password of the new user.
        :return: The result of the mutation. Either a success or a failure.
        """
        if await CreateUser._username_exists(username):
            return CreateUserFailUsernameExists(
                error_message="Username already exists.",
                suggested_alternatives=await CreateUser._get_alternative_usernames(
                    username
                ),
            )
        if select(User).where(User.email == email).first():
            return CreateUserFailOther(error_message="Email already exists.")

        try:
            user = await service.create_user(
                UserCreate(
                    username=username,
                    email=email,
                    full_name=full_name,
                    password=password,
                )
            )
            return CreateUserSuccess(user=user)
        except Exception:
            return CreateUserFailOther(
                error_message="Something went wrong while creating the user."
            )


class Query(graphene.ObjectType):
    users = graphene.String()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
