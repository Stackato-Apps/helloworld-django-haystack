from django.shortcuts import render_to_response

from haystack.forms import SearchForm


def notes(request):
    form = SearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})
