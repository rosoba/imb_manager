
from django.urls import path
from . import views

app_name = 'publishing'
urlpatterns = [
    path('', views.PublicationListView.as_view(), name='publication-list'),
    path('create/', views.PublicationCreateView.as_view(), name='publication-create'),
    path('<int:id>/', views.PublicationDetailView.as_view(), name='publication-detail'),
    path('<int:id>/update/', views.PublicationUpdateView.as_view(), name='publication-update'),
    path('<int:id>/delete/', views.PublicationDeleteView.as_view(), name='publication-delete'),
]
