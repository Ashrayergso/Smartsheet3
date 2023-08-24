```python
from django.shortcuts import render
from .utils import get_smartsheet_data, get_excel_data, compare_and_update_data

def index(request):
    return render(request, 'app/index.html')

def update_data(request):
    if request.method == 'POST':
        smartsheet_df = get_smartsheet_data()
        excel_df = get_excel_data()
        updated_df = compare_and_update_data(smartsheet_df, excel_df)
        context = {
            'smartsheet_data': smartsheet_df.to_html(),
            'excel_data': excel_df.to_html(),
            'updated_data': updated_df.to_html(),
        }
        return render(request, 'app/result.html', context)
    else:
        return render(request, 'app/index.html')
```