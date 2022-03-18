from django import forms
from vehicle.models import Vehicles

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicles
        fields = ['name','vehicle_code','vehicle_price','quality','image']


    def __init__(self,*args,**kwargs):
             super(VehicleForm,self).__init__(*args,**kwargs)
             self.fields['quality'].empty_label = "Select"
             self.fields['image'].required = True
