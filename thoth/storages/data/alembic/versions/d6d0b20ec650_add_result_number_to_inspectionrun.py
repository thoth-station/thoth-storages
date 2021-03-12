"""Add result number to inspectionRun

Revision ID: d6d0b20ec650
Revises: 10925df620b1
Create Date: 2020-07-08 16:07:37.994149+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d6d0b20ec650"
down_revision = "10925df620b1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "inspection_run", sa.Column("inspection_result_number", sa.Integer(), nullable=False, server_default="0")
    )
    op.drop_constraint("inspection_run_inspection_document_id_key", "inspection_run", type_="unique")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        "inspection_run_inspection_document_id_key", "inspection_run", ["inspection_document_id"]
    )
    op.drop_column("inspection_run", "inspection_result_number")
    # ### end Alembic commands ###
