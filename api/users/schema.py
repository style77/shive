import graphene

from api.users.models import UserCreate
from api.users.services import service


class UserGraphene(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    full_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    is_active = graphene.Boolean()


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        full_name = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: UserGraphene)

    async def mutate(root, info, username, email, full_name, password):
        user = service.create_user(
            UserCreate(username=username, email=email, full_name=full_name, password=password)
        )
        return CreateUser(user=user)


class Query(graphene.ObjectType):
    users = graphene.String()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
