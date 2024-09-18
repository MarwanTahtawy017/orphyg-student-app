from django.shortcuts import render
from .models import Assistant

# Create your views here.


def ShowAssistants(request):
    Ordered_List = Assistant.objects.order_by('Name')
    context = {'Ordered_List': Ordered_List}
    return render(request, 'Assistants/assistantsblog.html', context)
