from __future__ import annotations

import uuid
from typing import List, Iterable, Mapping
from dataclasses import dataclass, field
import datetime


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email_address: str,
        biography: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.biography = biography
        self._experiences: List[Experience] = []
        self.id = str(uuid.uuid4())

    @property
    def experiences(self) -> Iterable[Experience]:
        return self._experiences

    def add_experience(self, experience: Experience) -> None:
        self._experiences.append(experience)


class Company:
    def __init__(
        self,
        name: str,
        address: str,
        description: str
    ) -> None:
        self.name = name
        self.address = address
        self.description = description
        self.id = str(uuid.uuid4())
        self._job_requests: List[JobRequest] = []

    @property
    def job_requests(self) -> Iterable[JobRequest]:
        return self._job_requests

    def add_job_request(self, job_request: JobRequest) -> None:
        self._job_requests.append(job_request)


@dataclass
class Experience:
    user_id: str
    company_id: str
    title: str
    starts_at: datetime.date
    ends_at: datetime.date = field(default_factory=datetime.date.today)


@dataclass
class JobRequest:
    company_name: str
    title: str
    conditions: Mapping[str: float]
