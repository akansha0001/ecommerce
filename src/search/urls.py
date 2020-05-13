


from django.conf.urls import url


from .views import(
     SearchProductListView,
  
)


urlpatterns = [
    url(r'^$', SearchProductListView.as_view(),name='search_list')
  
]
app_name = 'search'
