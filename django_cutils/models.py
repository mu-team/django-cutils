from django.db import models
from django.utils import timezone


class SoftDeletionQuerySet(models.QuerySet):
    def delete(self):
        return self.update(deleted_at=timezone.now())


class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return SoftDeletionQuerySet(self.model).filter(deleted_at=None)


class SoftDeletionModel(models.Model):
    """
    `SoftDeletionModel` replaces the standard removal mechanism with a soft one.
    """

    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()


class TimestampModel(models.Model):
    """
    `TimestampModel` monitors for any changes in the
    internal state of the child model when save and update.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CUDModel(TimestampModel, SoftDeletionModel):
    """
    C - Create, U - Update, D - Delete.
    Compilation of `TimestampModel` and `SoftDeletionModel`.
    """
    pass
