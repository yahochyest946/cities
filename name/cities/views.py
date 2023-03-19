from django.urls import reverse_lazy
from django.views.generic import*
from .models import City
from .forms import*



class CitiesListView(ListView):
    paginate_by = 5
    model = City
    template_name = "cities/home.html"


class CitiesCreateView(CreateView):
    model=City
    form_class = CityForm
    template_name= "cities/create.html"

class CitiesDetaiView(DetailView):
    model = City
    template_name = "cities/detail.html"


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = "cities/update.html"
    success_url = reverse_lazy("cities:home")



class CityDeleteView(DetailView):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy("cities:home")

