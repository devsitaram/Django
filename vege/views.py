from django.shortcuts import render, redirect
from .models import*
from django.http import HttpResponse

from .models import Receipe

# Create your views here.
def receipes_add(request):
    if request.method == "POST":
        data = request.POST
    
        name = data.get('receipe_name')
        descriptions = data.get('receipe_description')
        image = request.FILES.get('receipe_image')

        # data save in model
        Receipe.objects.create(
            receipe_name = name,
            receipe_description = descriptions,
            receipe_image = image
        )

        return redirect('/receipes/') # redirect again (redirect) go to the same page then not show the alert dialog box

    queryset = Receipe.objects.all() # receipes data is add in the queryset variable
    context = {'receipes':queryset} # data is add in conte

    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(pk=id)
    queryset.delete()
    return redirect('/receipes/')


def update_receipe(request, id):
    queryset = Receipe.objects.get(pk=id)

    if request.method == "POST":
        data = request.POST
    
        name = data.get('receipe_name')
        descriptions = data.get('receipe_description')
        image = request.FILES.get('receipe_image')

        queryset.receipe_name = name
        queryset.receipe_description = descriptions
        
        if image:
            queryset.receipe_image = image

        queryset.save()
        return redirect('/receipes/')

    context = {'receipe': queryset} # data is add in conte
    return render(request, 'update_receipe.html', context)