from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'administrator/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            obj = LoginTable.objects.get(username=username,password=password)
            if obj.usertype == 'admin':
                return HttpResponse('''<script>alert("welcome to admin home"),window.location="/Home";</script>''')
            
            else:
                return HttpResponse("User type not recognized")
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("Invalid username or password"),window.location="";</script>''')


class complaints(View):
    def get(self, request):
        obj = Complaints.objects.all()
        return render(request, 'administrator/complaints.html', {'obj': obj})
    def post(self,request):
        message = request.POST['message']
        obj = Complaints.objects.get('id=comp_id')
        obj.complaints = message
        obj.save()
        return HttpResponse('''<script>alert("Complaint updated"),window.location="/complaints";</script>''')
    
    
class feedback(View):
    def get(self, request):
        obj = Feedback.objects.all()
        return render(request, 'administrator/feedback.html', { 'obj': obj })
    
class Home(View):
    def get(self, request):
        return render(request, 'administrator/Home.html')
    
class manage_user(View):
    def get(self, request):
        obj = UserTable.objects.all()
        return render(request, 'administrator/manage_user.html', {'obj':obj})
    
class accept_user(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.usertype = 'user'
        obj.save()
        return HttpResponse('''<script>alert("User accepted"),window.location="/manage_user";</script>''')
    
class rejected_user(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.usertype = 'rejected'
        obj.save()
        return HttpResponse('''<script>alert("User rejected"),window.location="/manage_user";</script>''')