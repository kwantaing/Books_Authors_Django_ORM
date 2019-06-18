from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$',views.author),
    url(r'^view/books/(?P<id>\d+)$',views.showbook),
    url(r'^view/authors/(?P<id>\d+)$',views.showauthor),
    url(r'^add_book$',views.add_book),
    url(r'^add_author$',views.add_author),
    url(r'^add_author_to_book$',views.add_author_to_book),
    url(r'^add_book_to_author$',views.add_book_to_author)
]