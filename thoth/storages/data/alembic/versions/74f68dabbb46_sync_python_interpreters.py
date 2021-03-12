"""Sync python interpreters

Revision ID: 74f68dabbb46
Revises: 184e698fe2c2
Create Date: 2019-10-16 13:34:12.694324+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74f68dabbb46"
down_revision = "184e698fe2c2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "python_interpreter",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("path", sa.String(length=256), nullable=False),
        sa.Column("link", sa.String(length=256), nullable=True),
        sa.Column("version", sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "found_python_interpreter",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("python_interpreter_id", sa.Integer(), nullable=False),
        sa.Column("package_extract_run_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["package_extract_run_id"], ["package_extract_run.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["python_interpreter_id"], ["python_interpreter.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", "python_interpreter_id", "package_extract_run_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("found_python_interpreter")
    op.drop_table("python_interpreter")
    # ### end Alembic commands ###
