"""second

Revision ID: 0290a40b430c
Revises: 5143ec7cf37e
Create Date: 2023-02-04 22:54:35.084826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0290a40b430c'
down_revision = '5143ec7cf37e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'currency', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'currency', type_='unique')
    # ### end Alembic commands ###
