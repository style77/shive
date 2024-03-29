"""make username and email fields unique and add indexing

Revision ID: b0db1ea14c75
Revises: 3b5d2ed9106c
Create Date: 2024-03-10 01:01:43.626903

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa  # noqa: F401
import sqlmodel  # noqa: F401


# revision identifiers, used by Alembic.
revision: str = "b0db1ea14c75"
down_revision: Union[str, None] = "3b5d2ed9106c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_unique_constraint(None, "users", ["username"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    # ### end Alembic commands ###
