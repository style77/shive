"""index username

Revision ID: cd5b2b49e930
Revises: b0db1ea14c75
Create Date: 2024-03-10 03:08:45.597096

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "cd5b2b49e930"
down_revision: Union[str, None] = "b0db1ea14c75"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_username_key", "users", type_="unique")
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.create_unique_constraint("users_username_key", "users", ["username"])
    # ### end Alembic commands ###
