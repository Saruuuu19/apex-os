from uuid import UUID as PyUUID
from uuid import uuid4

from sqlalchemy import ARRAY, String
from sqlalchemy import UUID as SqlUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.routine_exercise import RoutineExercise


class Exercise(Base):
    __tablename__ = "exercises"
    id: Mapped[PyUUID] = mapped_column(
        SqlUUID(as_uuid=True), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    primary_muscle: Mapped[str] = mapped_column(String(50), nullable=False)
    secondary_muscles: Mapped[list[str]] = mapped_column(
        ARRAY(String(50)), default=list
    )
    equipment: Mapped[str] = mapped_column(String(50), nullable=False)
    media_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    routine_exercises: Mapped[list["RoutineExercise"]] = relationship(
        back_populates="exercise"
    )
