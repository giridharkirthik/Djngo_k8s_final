from django import forms
from .models import Employees, FlightSchedule, Attendance_Manager


DESIGNATION_CHOICES = (
    ('DGM', 'DGM'),
    ('SAGM', 'SAGM'),
    ('MGR SE', 'MGR SE'),
    ('Sr Supd SE', 'Sr Supd SE'),
    ('Supd SE', 'Supd SE'),
    ('Sr SE', 'Sr SE'),
    ('SE', 'SE'),
    ('MGR SE', 'MGR SE'),
    ('TECHNICIAN', 'TECHNICIAN'),
)

Group_Choices= (
    ('Group 1', 'Group 1'), 
    ('Group 2', 'Group 2'), 
    ('Group 3', 'Group 3'), 
    ('Group 4', 'Group 4')
)
TRAINED_CHOICES = (
        ('B777', 'B777'),
        ('B787', 'B787'),
        ('B737', 'B737'),
        ('A320', 'A320'),
        ('A330', 'A330'),
        ('ATR', 'ATR'),
    )
class EmployeeForm(forms.ModelForm):
    designation = forms.ChoiceField(choices=DESIGNATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%; padding-bottom: 10px; border-radius: 10px; margin-bottom: 10px; height:37px;'}))
    grp= forms.ChoiceField(choices= Group_Choices, widget= forms.Select(attrs= {'class': 'new-form-control', 'style': 'width: 100%; padding-bottom: 10px; border-radius: 10px; margin-bottom: 10px; height:37px;'}))

    trained = forms.MultipleChoiceField(choices=TRAINED_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'trained-field form-check-input', 'style': 'margin-right: 5px'}))





    class Meta:
        model = Employees
        fields = ['empname', 'sap', 'designation', 'mob', 'email', 'trained', 'grp']



ARRIVAL_DAYS_CHOICES= ((1, 'M(1)'), (2, 'T(2)'), (3, 'W(3)'), (4, 'Th(4)'), (5, 'F(5)'), (6, 'Sa(6)'), (7, 'S(7)'))
DEPARTURE_DAYS_CHOICES= ((1, 'M(1)'), (2, 'T(2)'), (3, 'W(3)'), (4, 'Th(4)'), (5, 'F(5)'), (6, 'Sa(6)'), (7, 'S(7)'))

class FlightScheduleForm(forms.ModelForm):
    arrival_days = forms.MultipleChoiceField(
        choices=ARRIVAL_DAYS_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'N', 'style': 'display: inline-block'}
        ),
    )
    departure_days = forms.MultipleChoiceField(
        choices=DEPARTURE_DAYS_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'N', 'style': 'display: inline-block'}
        ),
    )

    class Meta:
        model = FlightSchedule
        fields = [
            'flight_no_arr',
            'flight_no_dep',
            'sta',
            'std',
            'arrival_days',
            'departure_days',
            'destination_from',
            'destination_to',
            'F',
        ]

        widgets = {
            'flight_no_arr': forms.TextInput(attrs={'style': 'height: 30px'}),
            'flight_no_dep': forms.TextInput(attrs={'style': 'height: 30px'}),
            'sta': forms.TextInput(attrs={'style': 'height: 30px'}),
            'std': forms.TextInput(attrs={'style': 'height: 30px'}),
            'destination_from': forms.TextInput(attrs={'style': 'height: 30px'}),
            'destination_to': forms.TextInput(attrs={'style': 'height: 30px'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arrival_days'].initial = [choice[0] for choice in self.fields['arrival_days'].choices]
        self.fields['departure_days'].initial = [choice[0] for choice in self.fields['departure_days'].choices]

        
ATTENDANCE_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave')
    )
class AttendanceForm(forms.ModelForm):

    Attendance = forms.ChoiceField(choices=ATTENDANCE_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'attendance-field',
        'style': 'display: inline-block; margin-right: 10px;',
        'id': 'id_Attendance'
    }))


    
    class Meta:
        model = Attendance_Manager
        fields = ['Attendance']
# class ArrivalScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Arrivalschedule
#         fields = ['id', 'flight_no_arr', 'sta', 'arrival_days', 'destination_from']
#         widgets = {
#             'arrival_days': forms.CheckboxSelectMultiple
#         }

#     arrival_days = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=[
#             ('1', 'M'),
#             ('2', 'TU'),
#             ('3', 'W'),
#             ('4', 'T'),
#             ('5', 'F'),
#             ('6', 'S'),
#             ('7', 'S'),
#         ]
#     )

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     if self.initial.get('select_all', True):
#     #             self.initial['arrival_days'] = [str(i) for i in range(1, 8)]


# class DepartureScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Departureschedule
#         fields = ['id', 'flight_no_dep', 'std', 'departure_days', 'destination_to']
#         widgets = {
#             'departure_days': forms.CheckboxSelectMultiple
#         }

#     departure_days = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=[
#             ('1', 'M'),
#             ('2', 'TU'),
#             ('3', 'W'),
#             ('4', 'T'),
#             ('5', 'F'),
#             ('6', 'S'),
#             ('7', 'S'),
#         ]
#     )

    