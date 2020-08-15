from django.db import models

# Create your models here.

class Translation(models.Model):
    translation_text = models.TextField(max_length=200, default="None")

    def __str__(self):
        return self.translation_text

class Choice(models.Model):
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    pyuru_string = models.TextField(default="None")

    def __str__(self):
        return self.pyuru_string
