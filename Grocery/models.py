from django.db import models

class Gro(models.Model):
	item_name=models.CharField(max_length=20)
	item_quantity=models.CharField(max_length=20)
	item_status = models.CharField(max_length=20)

	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.item_name + ' ' + self.item_quantity + ' ' + self.item_status

	class Meta:
		ordering = ['created']