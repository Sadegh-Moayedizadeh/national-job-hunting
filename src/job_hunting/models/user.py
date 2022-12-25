from job_hunting.models.base import Base


class User(Base):
    pass


# class User(ModelBase):
#     def __init__(
#         self,
#         first_name: str,
#         last_name: str,
#         email_address: str,
#         biography: str
#     ) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email_address = email_address
#         self.biography = biography
#         self._experiences: List[Experience] = []
#         self.id = str(uuid.uuid4())

#     @property
#     def experiences(self) -> Iterable[Experience]:
#         return self._experiences

#     def add_experience(self, experience: Experience) -> None:
#         self._experiences.append(experience)
