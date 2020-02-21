from django.http import HttpResponse
from django.views.generic import View
from .models import EmployeeModel
import json
from django.core.serializers import serialize

class ReadOneEmployee(View):
    def get(self,request):
        res = EmployeeModel.objects.get(idno=101)

        d1 = {"eidno":res.idno,
              "ename":res.name,
              "ecno":res.contactno,
              "eemail":res.email,
              "esal":res.salary
              }
        json_data = json.dumps(d1)
        return HttpResponse(json_data,content_type="application/json")

class ReadOneEmployeeDetails(View):
    def get(self,request):
        res = EmployeeModel.objects.get(idno=102)
        json_data = serialize("json",[res])
        return HttpResponse(json_data,content_type="application/json")

class AllEmployeeDetails(View):
    def get(self,request):
        qs = EmployeeModel.objects.all()
        json_data = serialize("json",qs)
        return HttpResponse(json_data,content_type="application/json")

class AllEmployeeNSDetails(View):
    def get(self,request):
        qs = EmployeeModel.objects.all()
        json_date = serialize("json",qs,fields=("name","salary"))
        return HttpResponse(json_date,content_type="application/json")

class ReadSpecificEmployee(View):
    def get(self,request,eid):
        res = EmployeeModel.objects.get(idno=eid)
        json_data = serialize("json",[res])
        return HttpResponse(json_data,content_type="application/json")
