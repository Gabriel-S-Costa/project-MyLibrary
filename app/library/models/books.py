from django.db import models

from app.library.models.base import BaseModel
from app.common import choices

class Books(BaseModel):
    code = models.CharField(max_length=8, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Título do livro')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Categoria')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Editora')
    version = models.IntegerField(blank=False, null=False, default=1)
    publication_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    isbn = models.CharField(max_length=80, null=False, blank=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Autor')
    status = models.CharField(max_length=50, choices=choices.STATUS_BOOKS, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self) -> str:
        return self.code + "|" + self.title
