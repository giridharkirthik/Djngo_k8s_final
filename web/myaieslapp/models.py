from django.db import models

class FlightSchedule(models.Model):

    F= models.AutoField(db_column='F', primary_key= True)
    flight_no_arr = models.CharField(db_column='Flight_no_arr', max_length=25)  # Field name made lowercase.
    flight_no_dep = models.CharField(db_column='Flight_no_dep', max_length=25, blank=True, null=True)  # Field name made lowercase.

    sta = models.IntegerField(db_column='STA')  # Field name made lowercase.
    std = models.IntegerField(db_column='STD', blank=True, null=True)  # Field name made lowercase.

    arrival_days = models.CharField(db_column='Arrival_days', max_length=50)  # Field name made lowercase.
    departure_days = models.CharField(db_column='Departure_days', max_length=50, blank=True, null=True)  # Field name made lowercase.

    destination_from = models.CharField(max_length=25)
    destination_to = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'FlightSchedule'

class Employees(models.Model):

    empname = models.CharField(db_column='Empname', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sap = models.IntegerField(db_column='SAP', primary_key= True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=25)  # Field name made lowercase.
    mob = models.CharField(db_column='Mob', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    trained = models.CharField(db_column='Trained', max_length=10)  # Field name made lowercase.
    grp = models.CharField(db_column='Grp', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'employees'



class Attendance_Manager(models.Model):
    Date = models.CharField(db_column='Date', max_length=20, 
                            )
    Employee_name = models.CharField(db_column='Employee_name', max_length=25)
    Employee_sap = models.CharField(db_column='Employee_sap', max_length=25)
    Group = models.CharField(db_column='Group', max_length=25)
    Attendance = models.CharField(db_column='Attendance', max_length=25)
    Shift = models.CharField(db_column='Shift', max_length=25)

    class Meta:
        db_table = 'Attendance'

class Allotment(models.Model):
    s_no= models.CharField(db_column= 'S.No', max_length= 5)
    arrival_flight= models.CharField(db_column= 'Arrival', max_length= 10)
    arrival_from= models.CharField(db_column= 'From', max_length= 10)
    

