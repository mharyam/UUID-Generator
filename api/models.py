from django.db import models

# Create your models here.


class UUIDRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=500)

    def __str__(self):
        return self.uuid

    @property
    def key_value(self):
        return {self.created: self.uuid}
