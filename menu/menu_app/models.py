from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    item_id = models.CharField(max_length=200)
    thumbnail = models.URLField(max_length=2000)

    def __str__(self):
        return f'{self.item_id} - {self.name}'