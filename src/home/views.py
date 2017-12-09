
from django.shortcuts import render
from .models import Photo
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View


#class HomeView(View):
	#def get(self,request,*args,**kwargs):
		#return render(request,"index.html",{})
def photo_list(request):
 	queryset =Photo.objects.all()
 	context = {
 			"photos":queryset, 		
 	}
 	return render(request,"index.html",context)