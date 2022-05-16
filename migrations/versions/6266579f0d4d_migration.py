"""migration

Revision ID: 6266579f0d4d
Revises: 5949008ee3e0
Create Date: 2022-05-15 23:39:20.987379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6266579f0d4d'
down_revision = '5949008ee3e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('text2', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'text2')
    # ### end Alembic commands ###
