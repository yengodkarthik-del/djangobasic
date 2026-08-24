from dajango.forms import ModelForm
from .models import homepage

class login(ModelForm):
    class meta:
        model = login
        fields = ['username', 'email', 'password']


class courses(ModelForm):
    class meta:
        model = courses
        fields = ['course_name', 'price']


class nav_bar(ModelForm):
    class meta:
        model = nav_bar
        fields = ['name', 'link']



class movie_card(ModelForm):
    class meta:
        model = movie_card
        fields = ['movie_name', 'genre', 'description', 'image', 'rating']




class ticketbooking(ModelForm):
    class meta:
        model = ticketbooking
        fields = ['name', 'destination', 'number_of_tickets', 'date', 'time', 'phone_no']


class id_card(ModelForm):
    class meta:
        model = id_card
        fields = ['name', 'id_number', 'phone_no', 'address', 'image', 'organization']


class laptop(ModelForm):
    class meta:
        model = laptop
        fields = ['brand', 'model', 'price', 'specifications', 'image']


class attendance(ModelForm):
    class meta:
        model = attendance
        fields = ['name', 'date', 'status']

class result(ModelForm):
    class meta:
        model = result
        fields = ['name', 'subject', 'internal_marks', 'external_marks', 'total_marks', 'percentage']


class rapido_booking(ModelForm):
    class meta:
        model = rapido_booking
        fields = ['name', 'phone_no', 'pickup_location', 'drop_location', 'vehicle_type']