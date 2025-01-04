from django.shortcuts import render, HttpResponse
from .models import Booking
from .utils import generate_qr_code

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        booking = Booking.objects.create(name=name)
        qr_code = generate_qr_code(booking.id)
        booking.qr_code.save(f"{booking.id}.png", qr_code)
        booking.save()
        context = {'booking': booking}
        print("created")
        return render(request, 'index.html', context)
    return render(request, 'index.html')