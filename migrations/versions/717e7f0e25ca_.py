"""empty message

Revision ID: 717e7f0e25ca
Revises: 
Create Date: 2020-07-02 00:24:51.667082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '717e7f0e25ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homeless_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('currently_homless', sa.Boolean(), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('story', sa.String(length=10000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('homeless_user_id', sa.Integer(), nullable=False),
    sa.Column('card_number', sa.Integer(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('transaction_pending', sa.Float(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('daily_limit', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['homeless_user_id'], ['homeless_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('number_of_contributions', sa.Integer(), nullable=True),
    sa.Column('donated_to_homeless_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['donated_to_homeless_user'], ['homeless_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('shelter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shelter_name', sa.String(length=80), nullable=False),
    sa.Column('address_1', sa.String(length=120), nullable=False),
    sa.Column('address_2', sa.String(length=120), nullable=False),
    sa.Column('beds_available', sa.Boolean(), nullable=True),
    sa.Column('shelter_to_homeless_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shelter_to_homeless_user'], ['homeless_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('shelter_name')
    )
    op.create_table('deposit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('homeless_user_id', sa.Integer(), nullable=False),
    sa.Column('contributor_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contributor_user_id'], ['contributor.id'], ),
    sa.ForeignKeyConstraint(['homeless_user_id'], ['homeless_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deposit')
    op.drop_table('shelter')
    op.drop_table('contributor')
    op.drop_table('card')
    op.drop_table('homeless_user')
    # ### end Alembic commands ###
