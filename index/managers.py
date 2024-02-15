from django.db import models

class IsStar_manager(models.Manager):
    def is_star(self):
        return self.filter(star=True)