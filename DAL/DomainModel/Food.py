from django.db import models


class Food(models.Model):
    Name = models.TextField()
    Proteins = models.TextField()
    Fats = models.TextField()

    def IsEmpty(self):
        return self.Name == "" and self.Proteins == "" and self.Fats == ""
