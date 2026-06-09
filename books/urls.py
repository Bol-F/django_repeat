from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    AuthorListCreateView,
    AuthorDetailView,
    BookListCreateView,
    BookDetailView,
)


urlpatterns = [
    path("", BookListCreateView.as_view(), name="book-list-create"),
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    path("authors/", AuthorListCreateView.as_view(), name="author-list-create"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),

    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]