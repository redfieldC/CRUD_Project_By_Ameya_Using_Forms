from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MembersForm
# Create your views here.
def list(request):
    return render(request,'list.html')

def create(request):
    if request.method=='POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    # form = MembersForm()
    # context = {'datas':form}
    return render(request,'create.html')


