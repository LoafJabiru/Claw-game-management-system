from django.db import models
class Machine(models.Model):
    machine_id = models.CharField(max_length=100)
    machine_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    

    def __str__(self):
        return self.machine_id