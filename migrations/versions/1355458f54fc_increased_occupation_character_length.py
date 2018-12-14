"""Increased occupation character length

Revision ID: 1355458f54fc
Revises: cb0bf8167ff4
Create Date: 2018-12-14 11:48:45.931140

"""

# revision identifiers, used by Alembic.
revision = '1355458f54fc'
down_revision = 'cb0bf8167ff4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('registrations', 'occupation',
                    type_=sa.String(length=1024))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('registrations', 'occupation',
                    type_=sa.String(length=128))
    # ### end Alembic commands ###
