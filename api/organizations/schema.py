import graphene

from api.users.schema import UserGraphene


class OrganizationGraphene(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    owner = graphene.Field(UserGraphene)
    icon = graphene.Enum('OrganizationIcon', [('DEFAULT', "default")])
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()