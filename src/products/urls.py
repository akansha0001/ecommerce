


from django.conf.urls import url


from .views import(
     ProductListView,
     product_list_view,
     ProductDetailView,
     product_detail_view,
     ProductFeaturedListView,
     ProductFeaturedDetailView,
      ProductDetailSlugView
)


urlpatterns = [
  


    url(r'^$', ProductListView.as_view(),name='list'),
    url(r'^products_fbv/$', product_list_view),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(),name='detail'),
    url(r'^products_fbv/(?P<pk>\d+)/$', product_detail_view),


    # url(r'^features/$', ProductFeaturedListView.as_view()),
    # url(r'^features/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),



  
]
app_name = 'products'
