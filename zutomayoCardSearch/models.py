from django.db import models

class Search(models.Model):
    name = models.CharField('お名前', max_length=50)
    content = models.TextField('内容', max_length=140)

    def __str__(self):
        return self.name