from job_hunting.models import Company, Experience, JobRequest, User
import datetime
from typing import Optional, Mapping


def add_user(
    first_name: str,
    last_name: str,
    email_address: str,
    biography: str
) -> None:
    user = User(first_name, last_name, email_address, biography)
    user.create()


def add_company(name: str, address: str, description: str) -> None:
    company = Company(name, address, description)
    company.create()


def add_experience(
    user_id: str,
    company_id: str,
    title: str,
    starts_at: datetime.date,
    ends_at: Optional[datetime.date] = None
) -> None:
    if ends_at is None:
        ends_at = datetime.date.today()
    experience = Experience(user_id, company_id, title, starts_at, ends_at)
    experience.create()
    # How should we handle the relationships??


def add_job_request(
    company_name: str,
    title: str,
    conditions: Mapping[str, float]
) -> None:
    job_request = JobRequest(company_name, title, conditions)
    job_request.create()
    # How do we handle the relationships?
