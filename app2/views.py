# Create your views here.
from django.views.generic import View
from django.shortcuts import render
from app2.models import Comparative

class App2Home(View):

    ''' View for home page for comparative graph .If get request contains object
    id it returns that object or else the first object from the list and display that '''

    def get(self, request):

        comp_list = Comparative.objects.all()
        if comp_list:
            if request.GET.get('plot_id'):
                obj = comp_list.get(id=int(request.GET['plot_id']))
            else:
                obj = comp_list[0]
        return render(request, "app2/home.html", {'comp_list':comp_list, 'obj':obj})