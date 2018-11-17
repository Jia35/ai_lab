import json
import datetime
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from monitor.models import AirData

# 首頁
def home(request):
    airData = AirData.objects.all().order_by('-creation_date')
    date_time = list(airData.values())
    for i in date_time:
        i["creation_date"] = timezone.localtime(i["creation_date"])

    airData = json.dumps(date_time, cls=DjangoJSONEncoder)
    return render(request, 'monitor/home.html', locals())

# 空氣品質監測
def aqm(request):
    airData = AirData.objects.all().order_by('creation_date')
    date_time = list(airData.values())
    for i in date_time:
        i["creation_date"] = timezone.localtime(i["creation_date"])

    airData = json.dumps(date_time, cls=DjangoJSONEncoder)
    return render(request, 'monitor/aqm.html', locals())

# 水族生態
def aquarium(request):
    if 'led' in request.POST:
        led_status = request.POST['led']
        if led_status == "on":
            res = requests.get('http://140.125.32.123/lighton/light_on.php')
        else:
            res = requests.get('http://140.125.32.123/motor/stop_find.php')
        print(res.text)
    return render(request, 'monitor/aquarium.html', locals())


# 上傳POST空氣品質資料
@csrf_exempt
def upload_air(request):
    if 'pm25' in request.POST:
        pm01 = request.POST['pm01']
        pm25 = request.POST['pm25']
        pm10 = request.POST['pm10']
        #pm01 = request.POST.get('pm01')
        airData = AirData(pm01=pm01, pm25=pm25, pm10=pm10)
        airData.save()
        return HttpResponse('upload air data Success!')
    return HttpResponse('upload air data Fail!')
