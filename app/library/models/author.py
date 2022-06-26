from django.db import models

from app.library.models.base import BaseModel


class Author(BaseModel):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self) -> str:
        return self.first_name + self.last_name