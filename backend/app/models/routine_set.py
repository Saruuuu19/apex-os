from uuid import UUID as PyUUID
from uuid import uuid4
from decimal import Decimal


from sqlalchemy import ForeignKey, Numeric, Integer
from sqlalchemy import UUID as SqlUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import SetType

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.routine_exercise import RoutineExercise


class RoutineSet(Base):
    __tablename__ = "routine_sets"
    id: Mapped[PyUUID] = mapped_column(
        SqlUUID(as_uuid=True), primary_key=True, default=uuid4
    )
    routine_exercise_id: Mapped[PyUUID] = mapped_column(
        SqlUUID(as_uuid=True), ForeignKey("routine_exercises.id"), nullable=False
    )
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    target_reps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    target_weight: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    set_type: Mapped[SetType] = mapped_column(default=SetType.NORMAL)

    routine_exercise: Mapped["RoutineExercise"] = relationship(
        back_populates="routine_sets"
    )
