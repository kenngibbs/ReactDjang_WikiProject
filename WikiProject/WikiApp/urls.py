from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new_author/', views.newAuthor, name="newAuthor"),
    path('user_wiki_entries/', views.userEntries, name="userEntries"),
    path('add_main_wiki/', views.mainAdd, name="mainAdd"),
    path('user_logout/', views.userLogout, name="userLogout"),
    path('wiki_search/', views.wikiSearch, name="wikiSearch"),
    path('detail_main_wiki/<int:mainWikiID>/', views.mainDetails, name="mainDetails"),
    path('edit_main_wiki/<int:mainWikiID>/', views.mainEdit, name="mainEdit"),
    path('delete_main_wiki/<int:mainWikiID>/', views.mainDelete, name="mainDelete"),
    path('add_related_wiki/<int:mainWikiID>/', views.relatedAdd, name="relatedAdd"),
    path('edit_related_wiki/<int:relatedWikiID>/', views.relatedEdit, name="relatedEdit"),
    path('delete_related_wiki/<int:relatedWikiID>/', views.relatedDelete, name="relatedDelete"),
]