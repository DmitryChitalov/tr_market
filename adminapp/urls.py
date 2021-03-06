import adminapp.views as adminapp
from django.urls import path


app_name = 'adminapp'

urlpatterns = [
    # раб
    path('users/create/', adminapp.user_create, name='user_create'),
    # раб
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    # раб
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    # раб
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    # раб
    path('countries/create/', adminapp.CountryCreateView.as_view(), name='country_create'),
    # раб
    path('countries/read/', adminapp.countries, name='countries'),
    # раб
    path('countries/update/<int:pk>/', adminapp.country_update, name='country_update'),
    # раб
    path('countries/delete/<int:pk>/', adminapp.CountryDeleteView.as_view(), name='country_delete'),
    # раб
    path('accommodation/create/countries/<int:pk>/', adminapp.accommodation_create, name='accommodation_create'),
    # раб
    path('accommodation/read/countries/<int:pk>/', adminapp.accommodations, name='accommodations'),
    # раб
    path('accommodation/read/<int:pk>/', adminapp.AccommodationDetailView.as_view(), name='accommodation_read'),
    path('accommodation/update/<int:pk>/', adminapp.accommodation_update, name='accommodation_update'),
    path('accommodation/delete/<int:pk>/', adminapp.accommodation_delete, name='accommodation_delete'),
]
