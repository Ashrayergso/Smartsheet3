```python
from django.contrib import admin
from .models import SmartsheetData, ExcelData

class SmartsheetDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'sign_on_date', 'sign_off_date']

class ExcelDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'sign_on_date', 'sign_off_date']

admin.site.register(SmartsheetData, SmartsheetDataAdmin)
admin.site.register(ExcelData, ExcelDataAdmin)
```