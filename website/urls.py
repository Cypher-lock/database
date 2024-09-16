from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("website/", views.index, name='index'),
    path("<int:aID>", views.materialInfo),
    #path("<str:sort>", views.indexWithSort),
    path('search/', views.search, name='search'),
    path('add_material', views.add_material, name='add_material'),
    path('materialInfo/<int:sID>/', views.materialInfo, name='materialInfo'),
    path('deleteItem/<int:sID>/', views.delete_item, name='delete_item'),
    path('updateItem/<int:sID>/', views.edit_material, name='update'),
    path('lockItem/<int:sID>/', views.lock_item, name='lock'),
    path('', views.homepage, name='homepage'),
    path('show_pdf/', views.show_pdf, name='show_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)