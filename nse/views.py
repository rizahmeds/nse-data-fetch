from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from nse.models import Equities

# Create your views here.
class EquitiesList(ListView):
    model = Equities
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(EquitiesList, self).get_context_data(*args, **kwargs)
        context['symbols'] = Equities.objects.values('SYMBOL').distinct()
        return context
    
    def get(self, request, *args, **kwargs):
        symbol = request.GET.get('symbol')
        object_list = Equities.objects.filter(SYMBOL=symbol)
        all_symbols = Equities.objects.values('SYMBOL').distinct()
        context = {
            'object_list': object_list,
            'symbols': all_symbols
        }
        return render(request, "nse/equities_list.html", context=context)