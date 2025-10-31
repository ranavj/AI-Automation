from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, text
from sqlalchemy.dialects.postgresql import JSONB
from app.db.session import Base

class Workflow(Base):
    __tablename__ = "workflows"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    definition: Mapped[dict] = mapped_column(JSONB, server_default=text("'{}'::jsonb"))
    created_at: Mapped[str] = mapped_column(server_default=text("NOW()"))

    runs = relationship("Run", back_populates="workflow")
