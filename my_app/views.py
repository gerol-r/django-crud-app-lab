from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Show, Review
from .forms import ReviewForm
# Import HttpResponse to send text-based responses
# from django.http import HttpResponse

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

def show_index(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', {'shows': shows})

def show_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    #ReviewForm to be rendered in the template
    review_form = ReviewForm()
    return render(request, 'shows/detail.html', {
        'show': show, 
        'review_form': review_form
    })

# class Show:
#     def __init__(self, title, description, streaming_platform, genres):
#         self.title = title
#         self.description = description
#         self.streaming_platform = streaming_platform
#         self.genres = genres

# shows = [
#     Show('The Blue Horizon', 'A sci-fi adventure through space.', 'Netflix', ['Sci-Fi', 'Adventure']),
#     Show('Comedy Gold', 'A hilarious mix of stand-up and skits.', 'Hulu', ['Comedy', 'Variety Shows']),
#     Show('Crime Files', 'Deep dives into real-life crime cases.', 'HBO Max', ['Crime', 'Documentary']),
#     Show('Fantasy Realm', 'An epic journey through mystical lands.', 'Disney+', ['Fantasy', 'Action']),
#     Show('Sports Nation', 'Your ultimate sports recap and analysis.', 'ESPN+', ['Sports', 'Talk Shows']),
# ]

class ShowCreate(CreateView):
    model = Show
    fields = ['title', 'genres', 'streaming_platform', 'description']
    success_url = '/shows/' 

class ShowUpdate(UpdateView):
    model = Show
    fields = ['title', 'genres', 'streaming_platform', 'description']
    success_url = '/shows/'

class ShowDelete(DeleteView):
    model = Show
    success_url = '/shows/'

def add_review(request, show_id):
    # create a ModelForm instance using the data in request.POST
    form = ReviewForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the show_id assigned
        new_review = form.save(commit=False)
        new_review.show_id = show_id
        new_review.save()
    return redirect('show-detail', show_id=show_id)


