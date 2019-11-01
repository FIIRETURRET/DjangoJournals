from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Journal
from .forms import NewJournalForm

def index(request):
    journal_list = Journal.objects.order_by('-created_at')
    context = {
        'journal_list': journal_list,
    }
    return render(request, 'journals/index.html', context)

def detail(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    return render(request, 'journals/detail.html', {'journal': journal})
    
def new_journal(request):
    if request.method == 'POST':
        form = NewJournalForm(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('journals:index')
    else:
        form = NewJournalForm()
    return render(request, 'journals/new_journal.html', {'form': form})