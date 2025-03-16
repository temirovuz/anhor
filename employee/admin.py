from django.contrib import admin
from django.contrib.admin import ModelAdmin

from employee.models import AccessTimes, DepartureTimes, WorkingDay, Product, DailyProduction, Employee, Attendance


@admin.register(AccessTimes)
class AccessTimeAdmin(ModelAdmin):
    fields = ['enter_time']
    list_display = ['id', 'enter_time']
    search_fields = ['id', 'enter_time']
    search_help_text = "ID va Vaqt bo'yicha qidirish"


@admin.register(DepartureTimes)
class DepartureTimeAdmin(ModelAdmin):
    fields = ['departure_time']
    list_display = ['id', 'departure_time']
    search_fields = ['id', 'departure_time']
    search_help_text = "ID va Vaqt bo'yicha qidirish"


@admin.register(WorkingDay)
class WorkingDayAdmin(ModelAdmin):
    fields = ['date']
    list_display = ['id', 'date']
    search_fields = ['id', 'date']
    search_help_text = "ID va Sana bo'yicha qidirish"


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    fields = ['name', 'price_per_unit']
    list_display = ['id', 'name', 'price_per_unit']
    search_fields = ['id', 'name']
    search_help_text = "ID va Nomi bo'yicha qidirish"



@admin.register(DailyProduction)
class DailyProductionAdmin(ModelAdmin):
    fields = ['date', 'product', 'total_quantity']
    list_display = ['id','date' ,'product', 'total_quantity']
    search_fields = ['id', 'date', 'product']
    search_help_text = "ID va Sana va Maxsulot bo'yicha qidirish"


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    fields = ['employee_type', 'full_name']
    list_display = ['id','employee_type' ,'full_name']
    search_fields = ['id', 'employee_type', 'full_name']
    search_help_text = "ID va Ishchi va Ishchi turi bo'yicha qidirish"


@admin.register(Attendance)
class AttendanceAdmin(ModelAdmin):
    fields = ['date', 'employee','check_in', 'check_out', 'break_time']
    list_display = ['id','date' ,'employee','check_in', 'check_out', 'break_time', 'worked_hours']
    search_fields = ['id', 'date']
    search_help_text = "ID va Sana bo'yicha qidirish"
