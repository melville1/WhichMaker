from django.urls  import path 
from whichApp.views   import SandView, IngredientsView



urlpatterns = [
path('', SandView.as_view(), name = 'sandwich'),
path ('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name = 'ingredients_list'),


]