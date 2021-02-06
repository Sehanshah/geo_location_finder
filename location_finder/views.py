from django.shortcuts import render
from django.http import HttpResponse
from .config import *
import pandas as pd
import requests
from io import BytesIO as IO


def get_geo_location(address):
    try:
        response = requests.get(get_geo_info(address))
        result = response.json().get('results')[0].get('locations')[0].get('displayLatLng')
    except: 
        result = {}
    return str(result)


def home(request):
    if request.POST:
        try:
            df = pd.read_excel(request.FILES.get('xl_file'))
        except Exception as e:
            return render(request, 'home_page.html', {'error': 'Upload valid excel file'})

        df['Geo location'] = df['Address Data'].map(lambda address: get_geo_location(address))
        excel_file = IO()
        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        df.to_excel(xlwriter, 'Sheetname1', index=False)
        xlwriter.save()
        xlwriter.close()
        excel_file.seek(0)
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=GeoLocation_updated.xlsx'
        return response
    
    return render(request, 'home_page.html', {})