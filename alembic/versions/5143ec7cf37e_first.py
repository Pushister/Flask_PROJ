"""first

Revision ID: 5143ec7cf37e
Revises: 
Create Date: 2023-02-04 22:52:03.531477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5143ec7cf37e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bank', sa.String(length=50), nullable=True),
    sa.Column('currency', sa.String(length=120), nullable=True),
    sa.Column('date_exchange', sa.String(length=120), nullable=True),
    sa.Column('buy_rate', sa.Float(), nullable=True),
    sa.Column('sale_rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('currency')
    # ### end Alembic commands ###
