from django.db import models

class TimeSlot(models.Model):
    day_of_week = models.CharField(max_length=9)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    ids = models.JSONField()  # Birden fazla ID'yi tutmak için
    camera_ids = models.JSONField(null=True, blank=True)  # Opsiyonel Camera ID'ler için

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.stop_time}"

