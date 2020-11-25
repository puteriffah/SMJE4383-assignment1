from django.urls import path
from todo_list import views

urlpatterns = [
	path('', views.home, name = "HOMEPAGE"),
	path('delete/<list_id>', views.delete, name = "delete"),
	path('cross_off/<list_id>', views.cross_off, name = "cross_off"),
	path('uncross/<list_id>', views.uncross, name = "uncross"),
]
