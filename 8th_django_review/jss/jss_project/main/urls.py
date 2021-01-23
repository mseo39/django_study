from django.urls import path
import main.views


urlpatterns = [
    path('', main.views.index, name="index"),
    path('detail/<int:jss_id>',main.views.detail,name="detail"),
    path('create', main.views.create, name="create"),
    path('delete/<int:jss_id>',main.views.delete, name="delete"),
    path('update/<int:jss_id>',main.views.update, name="update"),
]