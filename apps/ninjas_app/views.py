from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas_app/index.html')

def allninjas(request):
    return render(request, 'ninjas_app/allninjas.html')

def ninja(request, ninjacolor):
    ninjacoldict = {
        'image':'notapril.jpg'
    }
    if ninjacolor == 'blue':
        ninjacoldict['image']='leonardo.jpg'
    elif ninjacolor == 'orange':
        ninjacoldict['image']='michelangelo.jpg'
    elif ninjacolor == 'red':
        ninjacoldict['image']='raphael.jpg'
    elif ninjacolor == 'purple':
        ninjacoldict['image']='donatello.jpg'
    else:
        ninjacoldict['image']='notapril.jpg'
    return render(request, 'ninjas_app/ninja.html', ninjacoldict)

