from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    employed_at = models.DateTimeField()
    chief = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    root = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name[:2]

    def save(self, *args, **kwargs):
        if Employee.objects.count() == 0:
            self.root = True
            self.chief = None
            super(Employee, self).save(*args, **kwargs)
        elif self.chief is not None:
            super(Employee, self).save(*args, **kwargs)
