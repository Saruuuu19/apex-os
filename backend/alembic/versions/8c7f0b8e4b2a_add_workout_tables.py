"""add workout tables

Revision ID: 8c7f0b8e4b2a
Revises: d1b4acfc0db9
Create Date: 2026-07-02 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "8c7f0b8e4b2a"
down_revision: Union[str, Sequence[str], None] = "d1b4acfc0db9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


set_type_enum = postgresql.ENUM(
    "WARM_UP",
    "NORMAL",
    "DROP_SET",
    "FAILURE",
    name="settype",
    create_type=False,
)


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("routine_sets", "reps", new_column_name="target_reps")

    op.create_table(
        "workout_sessions",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("routine_id", sa.UUID(), nullable=True),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["routine_id"], ["routines.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "workout_exercises",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("workout_session_id", sa.UUID(), nullable=False),
        sa.Column("exercise_id", sa.UUID(), nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["exercise_id"], ["exercises.id"]),
        sa.ForeignKeyConstraint(["workout_session_id"], ["workout_sessions.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sets",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("workout_exercise_id", sa.UUID(), nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.Column("set_type", set_type_enum, nullable=False),
        sa.Column("reps", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Numeric(precision=6, scale=2), nullable=True),
        sa.Column("rpe", sa.Numeric(precision=2, scale=1), nullable=True),
        sa.ForeignKeyConstraint(["workout_exercise_id"], ["workout_exercises.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("sets")
    op.drop_table("workout_exercises")
    op.drop_table("workout_sessions")

    op.alter_column("routine_sets", "target_reps", new_column_name="reps")
