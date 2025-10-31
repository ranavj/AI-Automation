from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, text
from sqlalchemy.dialects.postgresql import JSONB
from app.db.session import Base

class Run(Base):
    __tablename__ = "runs"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    workflow_id: Mapped[int] = mapped_column(ForeignKey("workflows.id", ondelete="CASCADE"), index=True)
    status: Mapped[str] = mapped_column(String(20), default="queued")
    input_payload: Mapped[dict] = mapped_column(JSONB, server_default=text("'{}'::jsonb"))
    output_payload: Mapped[dict] = mapped_column(JSONB, server_default=text("'{}'::jsonb"))
    logs: Mapped[dict] = mapped_column(JSONB, server_default=text("'[]'::jsonb"))
    started_at: Mapped[str] = mapped_column(server_default=text("NOW()"))
    finished_at: Mapped[str | None]

    workflow = relationship("Workflow", back_populates="runs")
