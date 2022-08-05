from django.urls import path
from .views import MenuList, menu_vote, menu_unvote, RestaurantList

urlpatterns = [
    path('menus', MenuList.as_view()),
    path('restaurant', RestaurantList.as_view()),
    path('<int:pk>/vote/', menu_vote),
    path('<int:pk>/unvote/', menu_unvote),
]