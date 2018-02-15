from django.shortcuts import render
from django.conf import settings

from pdf.models import *
from pdf.forms import *

# Create your views here.

def indicator_list(request):
    core_init = Core.objects.filter(id=1)
    stage_init = Stage.objects.filter(id=1)
    form = IndicatorList()
    cors = Core.objects.all().order_by('name')
    stags = Stage.objects.all().order_by('id')
    frameworks = None
    indicator_list = None
    if request.method == 'POST':
        core = request.POST.get('core_list', False)
        stage = request.POST.getlist('stage_list', False)
#        core = int(float(request.POST['core']))
#        stage = int(float(request.POST['stage']))
        #if form.is_valid():
        indicator_list = Indicator.objects.filter(stage__id__in=stage,framework__core__id=core)
        frameworks = Framework.objects.filter(core__id=core)
#    indicator_list = Indicator.objects.filter(stage__id='1',framework__core__id="1")
    return render(request, 'indicator_list.html', {'form':form, 'frameworks':frameworks, 'indicator_list':indicator_list, 'cors':cors, 'stags':stags})
#    return render(request, 'indicator_list.html', {'form': form,})