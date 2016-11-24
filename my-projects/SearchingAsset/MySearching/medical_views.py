__author__ = 'Mentu'
from django.db.models import Q
from django.shortcuts import render_to_response
from MySearching.models import Medical

def medicalSearchResults(request):
    search = request.POST.get('search', '')
    if search:
        sset=(Q(mname=search)|Q(mposition=search)|Q(mkeeper=search))
        results=Medical.objects.filter(sset).distinct
        length=Medical.objects.filter(sset).count()
    else:
        results=Medical.objects.all().distinct
        length=Medical.objects.all().count()
    return render_to_response('medical_results.html', {'type' : 'Medical', 'results' : results , 'length' : length})