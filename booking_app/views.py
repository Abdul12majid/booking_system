from django.shortcuts import render, HttpResponse, get_object_or_404
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


def get_booking_details(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_details.html', {'booking': booking})