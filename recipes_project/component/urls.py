from django.urls import path
from . import views
app_name='recipe'
urlpatterns = [
    path('', views.all_recipes,name='all_recipes'),
    path('<int:recipe_id>/', views.detail_recipe,name='detail_recipe'),
]
