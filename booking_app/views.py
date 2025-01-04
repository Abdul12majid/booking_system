from django.shortcuts import render, HttpResponse
from .models import Booking
from .utils import generate_qr_code

# Create your views here.

def index(request):
	context = {

	}
	return render(request, 'index.html', context)