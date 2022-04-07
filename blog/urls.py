from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.BlogCreate.as_view(), name='create'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.BlogUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BlogDelete.as_view(), name='delete'),
    path('science-list/', views.ScienceView.as_view(), name='science_list'),
    path('dailylife-list/', views.DailylifeView.as_view(), name='dailylife_list'),
    path('music-list/', views.MusicView.as_view(), name='music_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]