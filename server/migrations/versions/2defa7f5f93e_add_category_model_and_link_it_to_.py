"""Add Category model and link it to Product

Revision ID: 2defa7f5f93e
Revises: 211432aca61b
Create Date: 2025-05-11 16:29:43.432290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2defa7f5f93e'
down_revision = '211432aca61b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_products_category')
        batch_op.create_foreign_key('fk_products_category_id', 'categories', ['category_id'], ['id'])
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_index('ix_products_category', ['category'], unique=False)
        batch_op.drop_column('category_id')

    op.drop_table('categories')
    # ### end Alembic commands ###
