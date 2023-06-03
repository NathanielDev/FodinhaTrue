from django.db import models

# Create your models here.


class tmp_user(models.Model):
    # this is a temporary class just to achieve our beloved MVP of
    # printing our name to each other terminal
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
