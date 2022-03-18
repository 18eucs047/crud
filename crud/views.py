from django.shortcuts import render,redirect


from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
               if request.user.is_authenticated:
                                  user = request.user
                                  print(user.username)
                                  return redirect('/vehicle/list/'+user.username+'/')
               return render(request,"home.html")