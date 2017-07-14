"""Sync Referral to mobile app

Revision ID: 37f0939aa4a2
Revises: 1ce224e80aeb
Create Date: 2017-07-14 13:05:25.158330

"""

# revision identifiers, used by Alembic.
revision = '37f0939aa4a2'
down_revision = '1ce224e80aeb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('referrals', sa.Column('community_unit', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('country', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('county', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('district', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('lat', sa.Float(), server_default=sa.text(u"'0'"), nullable=True))
    op.add_column('referrals', sa.Column('lon', sa.Float(), server_default=sa.text(u"'0'"), nullable=True))
    op.add_column('referrals', sa.Column('mapping_id', sa.String(length=64), nullable=True))
    op.add_column('referrals', sa.Column('mobilization', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('recruitment_id', sa.String(length=64), nullable=True))
    op.add_column('referrals', sa.Column('subcounty', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('synced', sa.String(length=45), nullable=True))
    op.add_column('referrals', sa.Column('village', sa.String(length=45), nullable=True))
    op.create_index(op.f('ix_referrals_mapping_id'), 'referrals', ['mapping_id'], unique=False)
    op.create_index(op.f('ix_referrals_recruitment_id'), 'referrals', ['recruitment_id'], unique=False)
    op.drop_index('ix_referrals_location_id', table_name='referrals')
    op.drop_constraint(u'referrals_location_id_fkey', 'referrals', type_='foreignkey')
    op.create_foreign_key(None, 'referrals', 'mapping', ['mapping_id'], ['id'])
    op.create_foreign_key(None, 'referrals', 'recruitments', ['recruitment_id'], ['id'])
    op.drop_column('referrals', 'location_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('referrals', sa.Column('location_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'referrals', type_='foreignkey')
    op.drop_constraint(None, 'referrals', type_='foreignkey')
    op.create_foreign_key(u'referrals_location_id_fkey', 'referrals', 'location', ['location_id'], ['id'])
    op.create_index('ix_referrals_location_id', 'referrals', ['location_id'], unique=False)
    op.drop_index(op.f('ix_referrals_recruitment_id'), table_name='referrals')
    op.drop_index(op.f('ix_referrals_mapping_id'), table_name='referrals')
    op.drop_column('referrals', 'village')
    op.drop_column('referrals', 'synced')
    op.drop_column('referrals', 'subcounty')
    op.drop_column('referrals', 'recruitment_id')
    op.drop_column('referrals', 'mobilization')
    op.drop_column('referrals', 'mapping_id')
    op.drop_column('referrals', 'lon')
    op.drop_column('referrals', 'lat')
    op.drop_column('referrals', 'district')
    op.drop_column('referrals', 'county')
    op.drop_column('referrals', 'country')
    op.drop_column('referrals', 'community_unit')
    ### end Alembic commands ###
