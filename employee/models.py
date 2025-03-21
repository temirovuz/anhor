from django.db import models
from datetime import datetime, timedelta


class AccessTimes(models.Model):
    enter_time = models.TimeField()

    def __str__(self):
        return self.enter_time.strftime('%H:%M:%S')  # 24 soatlik format


class DepartureTimes(models.Model):
    departure_time = models.TimeField()

    def __str__(self):
        return self.departure_time.strftime('%H:%M:%S')  # 24 soatlik format


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Mahsulot nomi
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)  # 1 dona mahsulot narxi

    def __str__(self):
        return f"{self.name} - {self.price_per_unit} so‘m"


class WorkingDay(models.Model):
    date = models.DateField()  # Ish kuni

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


class DailyProduction(models.Model):
    date = models.ForeignKey(WorkingDay, on_delete=models.CASCADE, related_name="productions")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productions")
    total_quantity = models.IntegerField()

    @property
    def total_amount(self):
        """Kunlik ishlab chiqarilgan mahsulot qiymati."""
        return self.total_quantity * self.product.price_per_unit

    def __str__(self):
        return f"{self.date} - {self.product.name}: {self.total_quantity} dona"


class Employee(models.Model):
    CHOICE_TYPE = [
        ("yangi", 'Yangi'),
        ('doimiy', 'Doimiy'),
        ('bolalar', 'Bolalar')
    ]
    employee_type = models.CharField(max_length=15, choices=CHOICE_TYPE, default='yangi')
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendances")
    date = models.ForeignKey(WorkingDay, on_delete=models.CASCADE, related_name="attendances")
    check_in = models.ForeignKey(AccessTimes, on_delete=models.SET_NULL, null=True, related_name="check_ins")
    check_out = models.ForeignKey(DepartureTimes, on_delete=models.SET_NULL, null=True, related_name="check_outs")
    worked_hours = models.CharField(max_length=10, default="00:00")  # HH:MM format
    break_time = models.DurationField(default=timedelta())  # Default 0

    def save(self, *args, **kwargs):
        """AccessTimes va DepartureTimes asosida ishlagan vaqtni HH:MM formatida hisoblaydi."""
        if self.check_in and self.check_out:
            check_in_time = datetime.combine(datetime.today(), self.check_in.enter_time)
            check_out_time = datetime.combine(datetime.today(), self.check_out.departure_time)

            if check_out_time < check_in_time:
                check_out_time += timedelta(days=1)  # Agar ishchi kechasi ishlagan bo‘lsa

            time_difference = check_out_time - check_in_time

            # Agar tanaffus mavjud bo‘lsa, uni jami ishlagan vaqtga chegiramiz
            total_seconds = time_difference.total_seconds() - self.break_time.total_seconds()
            total_seconds = max(total_seconds, 0)  # Manfiy bo'lishining oldini olish

            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)

            self.worked_hours = f"{hours:02}:{minutes:02}"  # HH:MM formatida saqlash

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.worked_hours} soat"
