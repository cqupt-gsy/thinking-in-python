from django.shortcuts import render_to_response
# from django.http import HttpResponse

# Create your views here.

# def testConnect(request):
#     solid=Solid.objects.all()
#     html='<html><body>Connection content is %s.</body></html>' % solid[0].sid
#     return HttpResponse(html)

def indexPage(request):
    return render_to_response('index.html' , {'type' : 'Solid' , 'searchtype' : 'solidsearch'})

def thingPage(request):
    return render_to_response('thing.html', {'type' : 'Thing' , 'searchtype' : 'thingsearch'})

def medicalPage(request):
    return render_to_response('medical.html', {'type' : 'Medical' , 'searchtype' : 'medicalsearch'})

def othersPage(request):
    return render_to_response('others.html' , {'type' : 'Others' ,  'searchtype' : 'otherssearch'})

