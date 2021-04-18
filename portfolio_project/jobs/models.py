from django.db import models

# Create your models here.
class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)

    def __str__(self):
        if len(self.summery) > 22:
            return f"{self.summery[:22]}..."
        else:
            return self.summery
