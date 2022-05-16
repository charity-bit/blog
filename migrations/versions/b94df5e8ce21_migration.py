"""migration

Revision ID: b94df5e8ce21
Revises: 6266579f0d4d
Create Date: 2022-05-15 23:39:34.973199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b94df5e8ce21'
down_revision = '6266579f0d4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'text2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('text2', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
