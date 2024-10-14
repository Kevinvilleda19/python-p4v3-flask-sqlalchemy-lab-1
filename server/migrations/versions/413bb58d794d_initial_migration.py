"""initial migration

Revision ID: 413bb58d794d
Revises: 
Create Date: 2024-10-14 17:41:45.682328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413bb58d794d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earthquakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magnitude', sa.Float(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earthquakes')
    # ### end Alembic commands ###
