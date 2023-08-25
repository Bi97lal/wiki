from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name='error'),
    path('wiki/<str:title>', views.entry, name='entry'),
    path('search/', views.search_text, name='search'),
    path('create/', views.create_page, name='create_page'),
    path('edit/', views.edit, name='edit'),
    path('edit_page/', views. edit_page, name='edit_page'),
    path('rand_page/', views.rand_page, name='rand_page'),

    

]
