from django.db import models


class Customer(models.Model):
    line_number = models.IntegerField()
    customer_name = models.IntegerField()

    def __str__(self):
        return f"Line number {self.line_number}"
