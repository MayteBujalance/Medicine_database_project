from django.db import models

# Create the model here


class Medicine(models.Model):
    bnf_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Pricing(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)

class Terminology(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()
