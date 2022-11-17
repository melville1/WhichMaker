from django.urls  import path 
from whichApp.views   import SandView, IngredientsView, SandwichGeneratorView



urlpatterns = [
path('', SandView.as_view(), name = 'sandwich'),
path ('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name = 'ingredients_list'),
 path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),


]