from django.http import Http404
from django.views.generic import ListView, DetailView


from django.shortcuts import render, get_object_or_404



from products.models import Product

# Create your views here.

class SearchProductListView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['query']=self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query=request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
