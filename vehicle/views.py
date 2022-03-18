from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from vehicle.forms import VehicleForm
from vehicle.models import Vehicles
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.cache import cache_control

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def vehicle_list(request,name):
               if(request.session['uname']!=name):
                                           return redirect('/vehicle/list/'+request.session['uname']+'/')


               ve = Vehicles.objects.all()

               compa = ''
               try:
                     u = User.objects.get(username = name)
                     compa = u.first_name
               except User.DoesNotExist:
                         compa = 'NULL'

               #print(ve)
               li = []
               for v in ve:
                         if v.company==compa:
                                        li.append(v)
               #print(li)
               #for l in li:
                #          print(l.username)
               context = {'vehicle_list':li,'name':name,'company':compa}
               #print(name)
               #user = User.objects.get(username=name)
               #print(user)
               return render(request,"vehicle/vehicle_list.html",context)

@login_required
def vehicle_form(request,id=0,names='',na=''):
               if request.method == "GET":
                     if id==0:
                               form = VehicleForm()
                               #print(form.cleaned_data['username'])
                     else:
                               vehicle = Vehicles.objects.get(pk=id)
                               form = VehicleForm(instance=vehicle)

                     #print(names)
                     #print(VehicleForm(request.POST).cleaned_data['username'])
                     #print(VehicleForm().cleaned_data['username'])
                     #u = request.POST['username']
                     #print(u)
                     return render(request,"vehicle/vehicle_form.html",{'form':form,'names':na,'id':id,'sess':request.session['uname'],'nam':names})
               else:
                     if id==0:
                                form = VehicleForm(request.POST,request.FILES)
                                compa = ''
                                try:
                                         u = User.objects.get(username = names)
                                         compa = u.first_name
                                except User.DoesNotExist:
                                               compa = 'NULL'
                                if form.is_valid():
                                               veh = Vehicles()
                                               veh.username = names
                                               veh.company = compa
                                               veh.name = form.cleaned_data['name']
                                               veh.vehicle_code = form.cleaned_data['vehicle_code']
                                               veh.vehicle_price = form.cleaned_data['vehicle_price']
                                               veh.quality = form.cleaned_data['quality']
                                               veh.image = form.cleaned_data['image']
                                               veh.save()
                                return redirect('/vehicle/list/'+names+'/')
                     else:
                                vehicle = Vehicles.objects.get(pk=id)
                                form = VehicleForm(request.POST,request.FILES,instance=vehicle)

                                if form.is_valid():

                                                  form.save()
                                return redirect('/vehicle/list/'+na+'/')


                     #fin = ''
                     #if id==0:
                      #         fin = '/vehicle/list/'+names+'/'
                     #else:
                      #         fin = '/vehicle/list/'+na+'/'
                     #return redirect(fin)

                     #return reverse('vehicle_list',kwargs={'name':names})

@login_required
def vehicle_delete(request,id,name):
               vehicle = Vehicles.objects.get(pk=id)
               vehicle.delete()
               return redirect('/vehicle/list/'+name+'/')