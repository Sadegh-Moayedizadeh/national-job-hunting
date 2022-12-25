from job_hunting.models.base import Base
from job_hunting.models.experience import Experience


class User(Base):
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

        self.id = email_address

        self.experiences = []

    def add_experience(self, experience: Experience) -> None:
        self.experiences.append(experience)
