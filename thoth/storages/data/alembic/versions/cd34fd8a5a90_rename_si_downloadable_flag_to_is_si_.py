"""Rename si_downloadable flag to is_si_analyzable

Revision ID: cd34fd8a5a90
Revises: c8017a5b43f1
Create Date: 2020-09-29 07:58:34.949144+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cd34fd8a5a90"
down_revision = "c8017a5b43f1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("python_package_version", "is_downloadable", new_column_name="is_si_analyzable")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("python_package_version", "is_si_analyzable", new_column_name="is_downloadable")
    # ### end Alembic commands ###
