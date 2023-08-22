from django.shortcuts import render
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

    return render(request, 'receipes.html')