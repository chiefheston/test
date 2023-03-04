from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(("Название пункта"), max_length=50)
    parent = models.ForeignKey("self", 
                            verbose_name=("Лежит в"), 
                            on_delete=models.CASCADE, 
                            null=True, blank=True,
                            default='0',
                            related_name='children')

    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")

    def __str__(self):
        return self.name
    