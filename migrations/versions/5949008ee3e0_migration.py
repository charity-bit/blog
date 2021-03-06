"""migration

Revision ID: 5949008ee3e0
Revises: 7b883808bb83
Create Date: 2022-05-15 16:52:59.007412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5949008ee3e0'
down_revision = '7b883808bb83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'title')
    # ### end Alembic commands ###
