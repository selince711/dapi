"""dapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path, include
from rest_framework import routers

from interface import views
from interface.views import ModuleListView, AddModuleView, UpdateModuleView, DeleteModuleView, CaseGroupListView, \
    InterfaceListView, AddCaseGroupView, DeleteCaseGroupView, UpdateCaseGroupView, ProductListView, AddProductView, \
    UpdateProductView, DeleteProductView

router = routers.DefaultRouter()
router.register('product_info', views.ProductInfoViewSet)
router.register('module_info', views.ModuleInfoViewSet)
router.register('case_group_info', views.CaseGroupInfoViewSet)
router.register('interface_info', views.InterfaceInfoViewSet)

urlpatterns = [
    path('admin/', xadmin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('login/', views.login),
    path('', views.login),
    path('home/', views.home),
    path('logout/', views.logout),

    path('product/', ProductListView.as_view(), name='product'),
    path('product_add/', AddProductView.as_view(), name='product_add'),
    path('product_update/', UpdateProductView.as_view(), name='product_update'),
    path('product_delete/', DeleteProductView.as_view(), name='product_delete'),

    path('module/', ModuleListView.as_view(), name='module'),
    path('module_add/', AddModuleView.as_view(), name='module_add'),
    path('module_update/', UpdateModuleView.as_view(), name='module_update'),
    path('module_delete/', DeleteModuleView.as_view(), name='module_delete'),

    path('case_group/', CaseGroupListView.as_view(), name='case_group'),
    path('case_group_add/', AddCaseGroupView.as_view(), name='case_group_add'),
    path('case_group_update/', UpdateCaseGroupView.as_view(), name='case_group_update'),
    path('case_group_delete/', DeleteCaseGroupView.as_view(), name='case_group_delete'),

    path('interface/', InterfaceListView.as_view(), name='interface'),
]