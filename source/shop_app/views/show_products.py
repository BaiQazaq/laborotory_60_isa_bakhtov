from django.views.generic import ListView
from django.db.models import Q
from urllib.parse import urlencode

from shop_app.models import Good
from shop_app.forms import SearchForm



class IndexView(ListView):
    template_name = 'show_products.html'
    model = Good
    context_object_name = 'goods'
    ordering = ('category', 'title')
    # extra_context = {'aaa': 'bbb'}
    #queryset = Good.objects.filter(is_deleted=True, balance__gt=0)
    paginate_by = 4
    paginate_orphans = 1
    
    
    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)
    
    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        query = Q(balance__gt=0) 
        queryset = queryset.filter(query)
        if self.search_value:
            query = Q(category__icontains=self.search_value) | Q(title__icontains=self.search_value) | Q(price__icontains=self.search_value) 
            queryset = queryset.filter(query)
        return queryset

