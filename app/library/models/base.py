from django.db import models
from django.utils import timezone


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True

class SoftDeletionQuerySet(models.QuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now())
    
    def hard_delete(self):
        return super().delete()
    
    def alive(self):
        return self.filter(deleted_at=None)
    
    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)            
        return SoftDeletionQuerySet(self.model)
    
    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True
    
    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
    
    def hard_delete(self):
        super().delete()


class BaseModel(TimeStampModel, SoftDeletionModel):
    class Meta:
        abstract = True

    