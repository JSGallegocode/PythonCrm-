from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 


from .models import Client
from .forms import AddClientForm

# Create your views here.

@login_required
def clients_list (request):
    clients = Client.objects.filter
    return render(request, 'client/clients_list.html',{
        'clients': clients
    })


@login_required
def clients_detail (request,pk):
    client = get_object_or_404(Client, created_by= request.user, pk=pk)

    return render(request, 'client/client_detail.html',{
        'client': client
    })


@login_required
# Create your views here.
def clients_add(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)

        if form.is_valid():
           cliente= form.save(commit = False)
           cliente.created_by= request.user
           cliente.save()

           messages.success(request, "Client Created.")

           return redirect ('clients_list')
    else:
        form= AddClientForm()
    form = AddClientForm()
    return render(request, 'client/clients_add.html', {
        'form': form
    })

@login_required
def clients_delete(request,pk):
    client = get_object_or_404(Client, created_by = request.user, pk=pk)
    client.delete()

    messages.success(request, "Client Deleted")

    return redirect('clients_list')

@login_required
def clients_edit(request,pk):
    client = get_object_or_404(Client, created_by= request.user , pk=pk)
     
    if request.method =='POST':
        form = AddClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            messages.success(request,"Client Updated.")
            return redirect('clients_list')
            
    else:
        form = AddClientForm(instance=client)
    
    return render(request,'client/clients_edit.html',{

        'form': form

    })