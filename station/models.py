from django.db import models

class Bus(models.Model):
    info = models.CharField(max_length=255, null=True)
    num_seats = models.IntegerField()

    @property
    def is_small(self):
        return self.num_seats <= 25




    class Meta:
        verbose_name_plural = "buses"

    def __str__(self):
        return f"{self.info} (id = {self.id})"

