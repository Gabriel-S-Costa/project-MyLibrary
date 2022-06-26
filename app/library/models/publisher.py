from contextlib import nullcontext
from tokenize import blank_re
from django.db import models

from app.library.models.base import BaseModel


class Publisher(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    address = models.JSONField(null=True, blank=True)
    phone = models.CharField(max_length=80, null=True, blank=True)
    site = models.CharField(max_length=50)
    email = models.EmailField(blank=False, null=False)

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

    def __str__(self) -> str:
        return self.name