from typing import Mapping

from job_hunting.models.base import Base


class JobRequest(Base):
    def __init__(
        self,
        company_name: str,
        title: str,
        conditions: Mapping[str: float]
    ) -> None:
        self.company_name = company_name
        self.title = title
        self.conditions = conditions
