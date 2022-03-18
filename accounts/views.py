from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.cache import cache_control

import string

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if request.user.is_authenticated:
                                  user = request.user
                                  print(user.username)
                                  return redirect('/vehicle/list/'+user.username+'/')
    if request.method == "POST":


        usernames = request.POST['username']
        if len(usernames)>100:
                        return render(request,'accounts/signup.html',{'error':'Username should not exceed more than 100 characters!'})
        username_user = usernames.translate({ord(c): None for c in string.whitespace})
        length = len(username_user)
        if length==0:
                       return render(request,'accounts/signup.html',{'error':'Username should not be empty!'})
        num = 0
        spec=0
        #if any(c in regex2 for c in username_user):
        for ch in username_user:
                              if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
                                              #print("The Given Character ", ch, "is an Alphabet")
                                              l=0
                              elif(ch >= '0' and ch <= '9'):
                                              #print("The Given Character ", ch, "is a Digit")
                                              num+=1
                              else:
                                              spec+=1

        if num==length:
                      return render(request,'accounts/signup.html',{'error':'Username should not be full of numeric!'})
        #print(num,' ',length)

        #for c in username_user:
         #                        if(not c.is)
          #                           spec+=1
        if spec==length:
                       return render(request,'accounts/signup.html',{'error':'Username should not be full of special characters!'})
        fin = num+spec
        if fin==length:
                       return render(request,'accounts/signup.html',{'error':'Username should not be full of numbers and special characters!'})





        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],first_name=request.POST['company'])
                username = request.POST['username']
                auth.login(request,user)
                request.session['uname'] = username
                return redirect('/vehicle/list/'+username+'/',name=user)
        else:
            return render (request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/signup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.user.is_authenticated:
                                  user = request.user
                                  print(user.username)
                                  return redirect('/vehicle/list/'+user.username+'/')
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            username = request.POST['username']
            auth.login(request,user)
            request.session['uname'] = username
            return redirect('/vehicle/list/'+username+'/',name=user)
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reset(request):
              if request.user.is_authenticated:
                                  user = request.user
                                  print(user.username)
                                  return redirect('/vehicle/list/'+user.username+'/')
              if request.method == 'POST':
                                try:
                                                User.objects.get(username = request.POST['username'])
                                #trying
                                                print('User is')
                                                print(User.objects.get(username = request.POST['username']))
                                #if user is not None:

                                                username = request.POST['username']
                                                #auth.login(request,user)


                                                if request.POST['password1'] == request.POST['password2']:
                                                                                 #try:
                                                                                        user = User.objects.get(username = request.POST['username'])
                                                                                        #user.password = request.POST['password1']
                                                                                        user.set_password(request.POST['password1'])
                                                                                        user.save()
                                                                                        return render (request,'accounts/login.html', {'error':'Password has been changed.So,login now!'})
                                                                                 #except User.DoesNotExist:
                                                                                        #user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                                                                                        #username = request.POST['username']
                                                                                        #auth.login(request,user)

                                                                                        #return redirect('/vehicle/list/'+username+'/',name=user)
                                                else:
                                                                        return render (request,'accounts/resetPassword.html', {'error':'Password does not match!'})

                                                #return redirect('/vehicle/list/'+username+'/',name=user)
                                                #return render (request,'accounts/resetPassword.html', {'error':'Password does not match!'})
                                except User.DoesNotExist:
                                                   return render (request,'accounts/resetPassword.html', {'error':'Username is not registered!'})
                                #else:
                                 #               return render (request,'accounts/login.html', {'error':'Username is not registered!'})
              else:
                                      return render(request,'accounts/resetPassword.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if request.method == 'POST':

        try:
                   del request.session['uname']
        except KeyError:
                   pass

        auth.logout(request)
    return redirect('/')
