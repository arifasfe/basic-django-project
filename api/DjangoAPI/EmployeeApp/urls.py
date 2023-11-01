from django.urls import path
from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('department/', views.departmentApi, name='department'),
    path('department/<int:id>', views.departmentApi, name='department'),

    path('employee/', views.employeeApi, name='employee'),
    path('employee/<int:id>', views.employeeApi, name='employee'),

     path('employee/savefile/', views.SaveFile, name='savefile')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)