from django.db import models

from app.library.models.base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.name
