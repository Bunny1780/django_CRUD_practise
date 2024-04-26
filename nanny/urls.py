from django.urls import path
from . import views

app_name = 'nannies' # app_name 固定名稱

urlpatterns = [
    path("", views.index, name="index"), # 有名字的路徑的話就使用app_name來方便辨別路徑
    path("new", views.new, name="new"),
    path("add", views.create, name="add"),
    path("<id>/edit", views.edit, name="edit"), # 順序很重要這樣寫代表任何路徑都會被當成 id
    path("<id>/delete", views.delete, name="delete"), # 順序很重要這樣寫代表任何路徑都會被當成 id
    path("<id>", views.show, name="show"), # 順序很重要這樣寫代表任何路徑都會被當成 id
]