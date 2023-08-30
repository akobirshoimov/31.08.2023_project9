from django.shortcuts import render,get_object_or_404
from .models import Moshinalar,Country
from django.http import JsonResponse

# Create your views here.
def all(request):
    all = Moshinalar.objects.all()
    result = []
    for i in all:
        result.append({
            'name':i.name,
            'year':i.year,
            'colour': i.colour
        })
    return JsonResponse(result,safe= False)
def detail(request,detail_id):
    each = Country.objects.get(id=detail_id)
    each = get_object_or_404(Country,id=detail_id)
    info = f'name:{Country.name},location:{Country.location}'
    return JsonResponse(info)
