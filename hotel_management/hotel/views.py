from django.shortcuts import render
from django.db import connection
from .models import Guest, Room

def available_rooms_base_de_datos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hotel_room WHERE is_available = TRUE")
        rows = cursor.fetchall()

    return render(request, 'rooms_DB.html', {'rooms': rows})

def guest_list_base_de_datos(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM hotel_guest ORDER BY check_in_date DESC')
        rows = cursor.fetchall()

    return render(request, 'guests_DB.html', {'guests': rows})

# ------------------------------------------------------------------------

def available_rooms(request):
    rooms = Room.objects.raw("SELECT * FROM hotel_room WHERE is_available = TRUE")
    return render(request, 'rooms.html', {'rooms': rooms})


def guest_list(request):
    guests = Guest.objects.raw('SELECT * FROM hotel_guest ORDER BY check_in_date DESC')
    return render(request, 'guests.html', {'guests': guests})