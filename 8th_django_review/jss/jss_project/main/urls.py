from django.urls import path
import main.views


urlpatterns = [
    path('', main.views.index, name="index"),
    path('detail/<int:jss_id>',main.views.detail,name="detail"),
    path('create', main.views.create, name="create"),
    path('delete/<int:jss_id>',main.views.delete, name="delete"),
    path('update/<int:jss_id>',main.views.update, name="update"),
     path('my_index', main.views.my_index, name="my_index"),

    path('create_comment/<int:jss_id>', main.views.create_comment, name="create_comment"),
    path('delete_comment/<int:jss_id>/<int:comment_id>', main.views.delete_comment, name="delete_comment"),

]