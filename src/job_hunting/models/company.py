from job_hunting.models.base import Base


class Company(Base):
    pass


# class Company(ModelBase):
#     def __init__(
#         self,
#         name: str,
#         address: str,
#         description: str
#     ) -> None:
#         self.name = name
#         self.address = address
#         self.description = description
#         self.id = str(uuid.uuid4())
#         self._job_requests: List[JobRequest] = []

#     @property
#     def job_requests(self) -> Iterable[JobRequest]:
#         return self._job_requests

#     def add_job_request(self, job_request: JobRequest) -> None:
#         self._job_requests.append(job_request)
