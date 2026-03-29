from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    ingredient = models.CharField(max_length=255, db_index=True)
    company = models.CharField(max_length=255, blank=True, default="")

    def __str__(self) -> str:
        return f"{self.name} ({self.ingredient})"
