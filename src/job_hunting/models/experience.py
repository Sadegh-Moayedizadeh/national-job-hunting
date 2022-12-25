import datetime

from job_hunting.models.base import Base


class Experience(Base):
    def __init__(
        self,
        user_id: str,
        company_id: str,
        title: str,
        starts_at: datetime.date,
        ends_at: datetime.date
    ) -> None:
        self.user_id = user_id
        self.company_id = company_id
        self.title = title
        self.starts_at = starts_at
        self.ends_at = ends_at
