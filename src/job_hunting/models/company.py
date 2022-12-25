from job_hunting.models.base import Base
from job_hunting.models import JobRequest


class Company(Base):
    def __init__(
        self,
        name: str,
        address: str,
        description: str
    ) -> None:
        self.name = name
        self.address = address
        self.description = description
        
        self.id = name
        
        self.job_requests = []

    def add_job_request(self, job_request: JobRequest) -> None:
        if job_request.title in \
                set(map(lambda j: j.title, self.job_requests)):
            raise ValueError(
                'The job request with the given title already exists.')
        self._job_requests.append(job_request)
