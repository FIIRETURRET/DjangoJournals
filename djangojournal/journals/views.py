from django.shortcuts import render, get_object_or_404

from .models import Journal

def index(request):
    journal_list = Journal.objects.order_by('-created_at')
    context = {
        'journal_list': journal_list,
    }
    return render(request, 'journals/index.html', context)

def detail(request, journal_id):
    query = get_object_or_404(Query, pk=journal_id)
    return render(request, 'journals/detail.html', {'journal': journal})