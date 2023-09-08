from datetime import datetime


class Comment:
    def __init__(
        self,
        email,
        content,
        created=None,
    ):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

    def __str__(self) -> str:
        return f"{self.email} - {self.content} - {self.created}"
