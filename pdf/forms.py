from django import forms
from pdf.models import Core, Stage

class IndicatorList(forms.Form):
    core_list = forms.ModelChoiceField(queryset=Core.objects.all().order_by('name'),initial = Core.objects.first().id)
    stage_list = forms.ModelChoiceField(queryset=Stage.objects.all().order_by('id'),initial = Stage.objects.first().id)
