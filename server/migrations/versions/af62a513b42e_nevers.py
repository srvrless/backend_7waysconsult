"""nevers

Revision ID: af62a513b42e
Revises: 37d6ad054d6f
Create Date: 2023-06-18 18:43:09.968442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af62a513b42e'
down_revision = '37d6ad054d6f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('links_query_key', 'links', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('links_query_key', 'links', ['query'])
    # ### end Alembic commands ###
