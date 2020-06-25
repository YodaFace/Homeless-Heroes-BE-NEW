"""empty message

Revision ID: 57050cdc74d1
Revises: 53480d6f4f49
Create Date: 2020-06-25 14:21:43.417165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '57050cdc74d1'
down_revision = '53480d6f4f49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('homeless_user_id', sa.Integer(), nullable=False),
    sa.Column('card_number', sa.Integer(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['homeless_user_id'], ['homeless_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('shelter', 'shelter_name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shelter', 'shelter_name',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.drop_table('card')
    # ### end Alembic commands ###
