__author__ = 'Mentu'
from django.db.models import Q
from django.shortcuts import render_to_response
from MySearching.models import Solid

def solidSearchResults(request):
    search = request.POST.get('search', '')
    if search:
        sset=(Q(sname=search)|Q(sposition=search)|Q(skeeper=search))
        results=Solid.objects.filter(sset).distinct
        length=Solid.objects.filter(sset).count()
    else:
        results=Solid.objects.all().distinct
        length=Solid.objects.all().count()
    return render_to_response('solid_results.html', {'type' : 'Solid', 'results' : results , 'length' : length})