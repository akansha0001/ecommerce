


from django.conf.urls import url


from .views import(
     ProductListView,
     ProductDetailSlugView
)


urlpatterns = [
  

    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(),name='detail'),
    url(r'^$', ProductListView.as_view(),name='list'),

]
app_name = 'products'
