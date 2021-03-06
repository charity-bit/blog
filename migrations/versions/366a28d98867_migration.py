"""migration

Revision ID: 366a28d98867
Revises: 4128f8f8f17b
Create Date: 2022-05-15 09:54:27.056260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '366a28d98867'
down_revision = '4128f8f8f17b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('posts', sa.Column('author', sa.Integer(), nullable=False))
    op.drop_constraint('posts_user_id_fkey', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['author'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_user_id_fkey', 'posts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'author')
    op.drop_table('comments')
    # ### end Alembic commands ###
