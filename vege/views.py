from django.shortcuts import render, redirect
from .models import*

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
       
        name = data.get('receipe_name')
        descriptions = data.get('receipe_description')
        image = request.FILES.get('receipe_image')

        print(name)
        print(descriptions)
        print(image)

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