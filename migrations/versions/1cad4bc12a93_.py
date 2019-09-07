"""empty message

Revision ID: 1cad4bc12a93
Revises: 524a5562b729
Create Date: 2019-09-02 19:19:24.580807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cad4bc12a93'
down_revision = '524a5562b729'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_name'), 'comment', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_name'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###
