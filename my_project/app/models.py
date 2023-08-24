```python
from django.db import models

class SmartsheetData(models.Model):
    name = models.CharField(max_length=255)
    sign_on_date = models.DateField()
    sign_off_date = models.DateField()

    class Meta:
        db_table = 'smartsheet_data'

class ExcelData(models.Model):
    name = models.CharField(max_length=255)
    sign_on_date = models.DateField()
    sign_off_date = models.DateField()

    class Meta:
        db_table = 'excel_data'
```