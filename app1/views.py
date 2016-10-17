# Create your views here.
from django.views.generic import ListView, DeleteView, View
from django.shortcuts import render, HttpResponse
from app1.models import Member, Catagory
from django.db.models import Max
import json

class App1Home(View):

    ''' Employment/unployment statistic home page which shows all members and catagory hierarchy'''

    template_name = "app1/home.html"

    def get(self, request):
        levels_list = Catagory.objects.values('level')
        levels = list(set([i['level'] for i in levels_list]))
        valid_levels =[]
        parent = Catagory.objects.filter(parent__isnull=True)
        for i in levels:
            valid_levels.append(Catagory.objects.filter(level=i))
        members_list = Member.objects.all()
        return render(request, self.template_name, {'members':Member.objects.all(),
                                                    'catagories': Catagory.objects.all(),
                                                    'l1':valid_levels, 'members_list':members_list})

class Validate(View):

    ''' view for ajax request to detect whether the member belongs to parrticualar catagory. This view returns ajax reponse '''

    def get(self, request):

        try:
            cat_obj = Catagory.objects.get(id=int(request.GET.get('cat_id')))
            member_list = Member.objects.filter(id=int(request.GET.get('member_id')), catagory=cat_obj)
            status = "Correct" if member_list else "Incorrect"
        except:
            status = "Incorrect"
        return HttpResponse(json.dumps({'status':status}), mimetype = 'application/json')
