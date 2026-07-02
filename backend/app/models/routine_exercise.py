from decimal import Decimal
from uuid import UUID as PyUUID
from uuid import uuid4

from sqlalchemy import ForeignKey, Numeric, Integer
from sqlalchemy import UUID as SqlUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.routine import Routine
    from app.models.exercise import Exercise


class RoutineExercise(Base):
    __tablename__ = "routine_exercises"
    id: Mapped[PyUUID] = mapped_column(
        SqlUUID(as_uuid=True), primary_key=True, default=uuid4
    )
    routine_id: Mapped[PyUUID] = mapped_column(
        SqlUUID(as_uuid=True), ForeignKey("routines.id"), nullable=False
    )
    exercise_id: Mapped[PyUUID] = mapped_column(
        SqlUUID(as_uuid=True), ForeignKey("exercises.id"), nullable=False
    )
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    sets: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    reps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    target_weight: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)

    routine: Mapped["Routine"] = relationship(back_populates="routine_exercises")
    exercise: Mapped["Exercise"] = relationship(back_populates="routine_exercises")
