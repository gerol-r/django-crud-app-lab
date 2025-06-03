from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

class Show:
    def __init__(self, title, description, streaming_platform, genres):
        self.title = title
        self.description = description
        self.streaming_platform = streaming_platform
        self.genres = genres

shows = [
    Show('The Blue Horizon', 'A sci-fi adventure through space.', 'Netflix', ['Sci-Fi', 'Adventure']),
    Show('Comedy Gold', 'A hilarious mix of stand-up and skits.', 'Hulu', ['Comedy', 'Variety Shows']),
    Show('Crime Files', 'Deep dives into real-life crime cases.', 'HBO Max', ['Crime', 'Documentary']),
    Show('Fantasy Realm', 'An epic journey through mystical lands.', 'Disney+', ['Fantasy', 'Action']),
    Show('Sports Nation', 'Your ultimate sports recap and analysis.', 'ESPN+', ['Sports', 'Talk Shows']),
]

def show_index(request):
    # shows = Show.objects.all()  # look familiar?
    return render(request, 'shows/index.html', {'shows': shows})
# above returns show obj, but model deffed and returned below

def show_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    # # toys = Toy.objects.all()  # Fetch all toys
    # # Only get the toys the show does not have
    # toys_show_doesnt_have = Toy.objects.exclude(id__in = show.toys.all().values_list('id'))
    # # instantiate FeedingForm to be rendered in the template
    # feeding_form = FeedingForm()
    return render(request, 'shows/detail.html', {
        # # include the show and feeding_form in the context
        # 'show': show, 'feeding_form': feeding_form, 
        # # 'toys': toys,  # Pass toys to the template 
        # 'toys': toys_show_doesnt_have,  # send those toys
    })



