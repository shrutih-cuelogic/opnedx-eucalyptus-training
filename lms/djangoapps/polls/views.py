import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from edxmako.shortcuts import render_to_response, render_to_string
from polls.forms import ReferenceForm
from polls.models import Reference

from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def create_reference(request):
    if request.method == 'POST':
        reference_data = {}
        reference_data['reference_name'] = request.POST.get('reference_name',None)
        reference_data['reference_type'] = request.POST.get('reference_type',"")
        reference_data['reference_link'] = request.POST.get('reference_link', default="Link")
        reference_data['reference_description'] = request.POST.get('reference_description')

        if reference_data:
            reference_object = Reference(**reference_data)
            reference_object.save()
            return redirect('view_reference')
        else:
            return HttpResponse({"Error":"sgdhsg"})
        return HttpResponse(
            json.dumps({"response_data":"shdgdh"}),
            content_type="application/json"
        )
        return redirect('view_reference')
    else:
       return render_to_response('polls/create_reference.html')


def view_reference(request):
    reference_details = Reference.objects.all()
    return render_to_response('polls/view_reference_details.html', {'reference_details': reference_details})

def edit_reference(request, reference_id):
    if request.method == "POST":
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference_obj = Reference.objects.get(id=reference_id)
            form = ReferenceForm(request.POST, instance = reference_obj)
            form.save()
            return redirect('view_reference')
    else:
        reference_obj = Reference.objects.get(id=reference_id)
        form = ReferenceForm(instance=reference_obj)
    return render_to_response('polls/edit_reference.html', {'reference_data': reference_obj})

def delete_reference(request, reference_id):
    reference_obj = Reference.objects.get(id=reference_id).delete()
    return redirect('view_reference')
