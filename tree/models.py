from django.db import models


class Node(models.Model):
    # Model for Binary Tree
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, null=True)
    value = models.IntegerField(unique=True, null=True)
    left = models.ForeignKey('self', related_name="left_set", on_delete=models.SET_NULL, null=True)
    right = models.ForeignKey('self', related_name="right_set", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
