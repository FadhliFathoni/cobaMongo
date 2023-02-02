from django.urls import path
from . import views

urlpatterns = [
    path("",views.listKaryawan),
    path("<int:delete_id>/delete",views.deleteView),
    path("<str:nama>/update",views.updateView),
]
