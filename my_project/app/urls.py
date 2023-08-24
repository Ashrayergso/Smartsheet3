```python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.update_data, name='update_data'),
    path('result/', views.result, name='result'),
]
```