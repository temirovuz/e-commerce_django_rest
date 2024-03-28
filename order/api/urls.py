from django.urls import path


urlpatterns = [
    path('order/', CategoryListView.as_view(), name='category-list')
]