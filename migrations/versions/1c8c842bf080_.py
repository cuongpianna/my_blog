"""empty message

Revision ID: 1c8c842bf080
Revises: 75e6cdb84ee0
Create Date: 2018-11-07 10:05:06.250905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c8c842bf080'
down_revision = '75e6cdb84ee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('slug_name', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'category', ['slug_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_column('category', 'slug_name')
    # ### end Alembic commands ###
