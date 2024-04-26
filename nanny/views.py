from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Nanny
# Create your views here.
def index(request):
    nanny = Nanny.objects.all # 去抓取 nanny裡的所有物件

    return render(request, "nannies/index.html", {"nannies":nanny})

def new(request):
    return render(request, "nannies/new.html")

# GET
@require_POST
def create(request):
    # return HttpResponse(request.POST["name"])
    nanny = Nanny(
        name = request.POST["name"],
        gender = request.POST["gender"],
        description = request.POST["description"],
    )
    nanny.save()
    

    return redirect(reverse("root"))

def show(request, id):
    # return HttpResponse(f"id = {id}")
    # try:
    #     nanny = Nanny.objects.get(pk=id)
    # except:
    #     return HttpResponse("no data", status=404)
    nanny = get_object_or_404(Nanny, pk = id)
    if request.method == "POST":
        nanny.name = request.POST["name"]
        nanny.gender = request.POST["gender"]
        nanny.description = request.POST["description"]
        nanny.save()

        return redirect(f"/nannies/{nanny.id}")
        return redirect(reverse("nannies:show", args=[nanny.id]))
    else:
        return render(request, "nannies/show.html", { "nannies": nanny })

def edit(request, id):
    nanny = get_object_or_404(Nanny, pk = id)

    return render(request, "nannies/edit.html", { "nannies": nanny })

@require_POST
def delete(request, id):
    nanny = get_object_or_404(Nanny, pk = id)
    nanny.delete()

    return redirect('nannies:index')