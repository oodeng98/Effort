from django.urls import path
from myapp import views

urlpatterns = [  # myproject의 urls.py에서 넘어온 패턴을 관리하는 역할
                 # URL 패턴별로 그 패턴을 담당할 '함수'를 지정
    path('', views.index), 
    path('create/', views.create), 
    path('read/<id>/', views.read),
    path('delete/', views.delete), 
    path('update/<id>/', views.update)
]
