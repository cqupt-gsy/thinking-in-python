__author__ = 'Mentu'
from django.db.models import Q
from django.shortcuts import render_to_response
from MySearching.models import Thing

def thingSearchResults(request):
    search = request.POST.get('search', '')
    if search:
        sset=(Q(tname=search)|Q(tposition=search)|Q(tkeeper=search))
        results=Thing.objects.filter(sset).distinct
        length=Thing.objects.filter(sset).count()
    else:
        results=Thing.objects.all().distinct
        length=Thing.objects.all().count()
    return render_to_response('thing_results.html', {'type' : 'Thing', 'results' : results , 'length' : length})