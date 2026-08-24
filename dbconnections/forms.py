from dajango.forms import ModelForm
from .models import loginform,courses,nav_bar,movie_card,ticketbooking,id_card,laptop,attendance,results,rapido_booking
class loginform(forms.ModelForm,):
    class meta:
        model =loginform 
        fields = '__all__'


class coursesform(ModelForm):
    class meta:
        model = courses
        fields = '__all__'


class nav_barform(ModelForm):
    class meta:
        model = nav_bar
        fields = '__all__'



class movie_cardform(ModelForm):
    class meta:
        model = movie_card
        fields = '__all__'




class ticketbookingform(ModelForm):
    class meta:
        model = ticketbooking
        fields ='__all__'


class id_cardform(ModelForm):
    class meta:
        model = id_card
        fields = '__all__'


class laptopform(ModelForm):
    class meta:
        model = laptop
        fields = '__all__'


class attendanceform(ModelForm):
    class meta:
        model = attendance
        fields = '__all__'

class resultform(ModelForm):
    class meta:
        model = result
        fields = '__all__'


class rapido_bookingformnav_bar(ModelForm):
    class meta:
        model = rapido_booking
        fields = '__all__'