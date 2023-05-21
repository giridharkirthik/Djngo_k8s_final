from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
from .forms import EmployeeForm, FlightScheduleForm, AttendanceForm
import datetime
import datetime
from num2words import num2words
import random
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from .models import FlightSchedule, Employees, Attendance_Manager
from sklearn.ensemble import RandomForestClassifier

now = datetime.datetime.now()
date_str = now.strftime("%d %m %Y")
weekday = now.strftime("%A").upper()
wd = int(now.strftime("%w"))+1
print("wd is", wd)
current_time = datetime.datetime.now().time()
# Create your views here


def mainpage(request):

    return render(request, "mainpage.html")


import pandas as pd

def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add")

    else:
        form = EmployeeForm()
    return render(request, "add.html", {"form": form})


def fail(request):

    return render(request, "fail.html")


def UpDel(request):

    employees = Employees.objects.all()
    flight_schedules = FlightSchedule.objects.all()
    employee_form = EmployeeForm()
    flight_schedule_form = FlightScheduleForm()

    return render(
        request,
        "UpDel.html",
        {
            "employees": employees,
            "flight_schedules": flight_schedules,
            "employee_form": employee_form,
            "flight_schedule_form": flight_schedule_form,
        },
    )


def EmpDel(request, sap):
    emp = Employees.objects.get(sap=sap)
    print(sap)
    emp.delete()
    return redirect("UpDel")


def EditEmployees(request, sap):
    form = EmployeeForm()
    empEdit = Employees.objects.get(sap=sap)
    return render(request, "EditEmployees.html", {"empEdit": empEdit, "form": form})


def UpdateEmployee(request, sap):
    empEdit = Employees.objects.get(sap=sap)
    form = EmployeeForm(request.POST or None, instance=empEdit)
    print(request.method)  # add this line to check the request method
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("UpDel")
    return render(request, "EditEmployee.html", {"empEdit": empEdit, "form": form})


def deleteFlight(request, F):

    Flight_info_dep = FlightSchedule.objects.get(id=F)

    Flight_info_dep.delete()
    return redirect("showFlights")


# def att(request, id):
#     no= Employees.objects.all()
#     print(no)
#     return render(request, "att.html")


def U(request, id):
    # arrival_schedule = Arrivalschedule.objects.get(id=id)
    # departure_schedule = Departureschedule.objects.get(id=id)

    # if request.method == 'POST':
    #     arrival_schedule_form = ArrivalScheduleForm(request.POST, instance=arrival_schedule)
    #     departure_schedule_form = DepartureScheduleForm(request.POST, instance=departure_schedule)

    #     if arrival_schedule_form.is_valid() and departure_schedule_form.is_valid():
    #         # process the forms and save the data
    #         arrival_schedule = arrival_schedule_form.save(commit=False)
    #         departure_schedule = departure_schedule_form.save(commit=False)
    #         arrival_schedule.save()
    #         departure_schedule.save()
    return redirect("Schedule")
    # else:
    #     arrival_schedule_form = ArrivalScheduleForm(instance=arrival_schedule)
    #     departure_schedule_form = DepartureScheduleForm(instance=departure_schedule)

    # return render(request, 'U.html', {'arrival_schedule_form': arrival_schedule_form, 'departure_schedule_form': departure_schedule_form})

    return render()


def Schedule(request):
    objects = FlightSchedule.objects.all()
    Schedule_form = FlightScheduleForm()

    da = []
    for i in objects:
        da.append({
            "flight_no_arr": i.flight_no_arr,
            "flight_no_dep": i.flight_no_dep,
            "sta": i.sta,
            "std": i.std,
            "arrival_days": i.arrival_days,
            "departure_days": i.departure_days,
            "destination_from": i.destination_from,
            "destination_to":i.destination_to,
        })
    df = pd.DataFrame(da)
    print(df)

    if request.method == "POST":
        Schedule_form = FlightScheduleForm(request.POST)
        if Schedule_form.is_valid():

            arrival_days = Schedule_form.cleaned_data.get("arrival_days")
            departure_days = Schedule_form.cleaned_data.get("departure_days")
            # for a in range(len(arrival_days)):
            #     #Check if the Value is a Weekday.
            #     weekday()

            Schedule_form.save()
            return redirect("Schedule")
        else:
            print(f"Form errors: {Schedule_form.errors}")
            # if the form is not valid, redirect to the main page
            return redirect("mainpage")

    # if the request method is GET, render the template with the forms
    return render(request, "Schedule.html", {"Schedule_form": Schedule_form})


def alloc(request):
    return render(request, "alloc.html")


def menu(request):
    return render(request, "menu.html")


def EditFlights(request, id, id_D):
    # Edit_Flight_info = Arrivalschedule.objects.get(id=id)
    # Edit_Flight_info_dep = Departureschedule.objects.get(id=id_D)
    return render(request, "EditFlights.html")


def Group(request): 
    At_Form = AttendanceForm()
    print(weekday)
    
    if request.method == "POST":
        print(request.POST)

        if At_Form.is_valid():
            print(request.POST)

            At_Form.save()
        else:
            At_Form = AttendanceForm()
            print("No data")

        # Get all flights from FlightSchedule
    next_day = now + datetime.timedelta(days=0)
    days = int(next_day.strftime("%j"))
    print("Number of days:", days)

    raw_number = days % 8
    print(raw_number)

    # Define the function to calculate the group
    def my_function(a):
        global shift
        global filter_value
        current_time = datetime.datetime.now().time()

        op = raw_number

        if op == 0 or op == 1:
            dict = {"night": "Group 1", "morning": "Group 2", "afternoon": "Group 3"}
        elif op == 2 or op == 3:
            dict = {"night": "Group 3", "morning": "Group 1", "afternoon": "Group 2"}
        elif op == 4 or op == 5:
            dict = {"night": "Group 2", "morning": "Group 4", "afternoon": "Group 1"}
        elif op == 6 or op == 7:
            dict = {"night": "Group 1", "morning": "Group 3", "afternoon": "Group 4"}

        if current_time > datetime.time(6, 30) and current_time < datetime.time(13, 30):
            filter_value = dict["morning"]
            shift= list(dict.keys())[1]

        elif current_time > datetime.time(13, 30) and current_time < datetime.time(21, 30):
            filter_value = dict["afternoon"]
            shift = list(dict.keys())[2]

        else:
            filter_value = dict["night"]
            shift = list(dict.keys())[0]


        return filter_value

    # Call the function to get the group
    filter_value = my_function(raw_number)
    Fetch_group = Employees.objects.all()
    da= []
    if request.method=="POST":

        #CODE FOR DEVOPS TESTING------>
        
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        import time

        start_time = time.time()
        # Load the Iris dataset
        iris = load_iris()
        X = iris.data
        y = iris.target

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a Random Forest classifier
        rf = RandomForestClassifier(n_estimators=100, random_state=42)

        # Fit the classifier to the training data
        rf.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = rf.predict(X_test)

        # Evaluate the classifier
        accuracy = rf.score(X_test, y_test)
        print("Accuracy:", accuracy)

        end_time = time.time()
        print("Time taken:", end_time - start_time, "seconds")
        #<--------------------CODE ENDS




        for i in Fetch_group:
            if i.grp== filter_value:
                attendance = request.POST.get(str(i.grp) + "_" + str(i.sap), None)

                da.append({"Date": date_str, "Employee_name": i.empname, "Employee_sap": i.sap, "Group": i.grp, "attendance": attendance, "shift": shift})
                df= pd.DataFrame(da)
        print(df)
        for _, row in df.iterrows():
    # create an instance of the Attendance_Manager model
            attendance = Attendance_Manager()

            # set the fields of the model instance from the DataFrame row
            attendance.Date = row['Date']
            attendance.Employee_name = row['Employee_name']
            attendance.Employee_sap = row['Employee_sap']
            attendance.Group = row['Group']
            attendance.Attendance = row['attendance']
            attendance.Shift = row['shift']

            # save the model instance to the database
            attendance.save()
    date_get= Attendance_Manager.objects.filter(Date= str(date_str)).exists()
    group_get= Attendance_Manager.objects.filter(Group= filter_value).exists()
    if date_get and group_get:
                print("Attendance already submitted")
                attendance_status= "Submitted"
    else:
                print("NOT SUBMITTED!!")
                attendance_status= "Notsubmitted"
         

    # Define the context dictionary and add the filter value to it
    print(filter_value)

    return render(request,"Group.html",{"attendance_status": attendance_status, "filter": filter_value,"Fetch_group": Fetch_group,"date": now,"weekday": weekday,"date_str": date_str, "At_Form": At_Form})


def showFlights(request):
    print("Wd is", wd)
    check_wd = str(wd)
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Get the group value based on current time
    if current_time > datetime.time(6, 30) and current_time < datetime.time(13, 30):
        group = "morning"
    elif current_time > datetime.time(13, 30) and current_time < datetime.time(21, 30):
        group = "afternoon"
    else:
        group = "night"

    # Define the range of sta for the current group
    if group == "morning":
        start_time = 630
        end_time = 1330
        print("MOR")
    elif group == "afternoon":
        start_time = 1330
        end_time = 2120
        print("AFT")
    else:
        start_time = 2100
        end_time = 2400
        print("NIG")

    # Convert sta field to an integer
    Fl = FlightSchedule.objects.filter(
        arrival_days__contains=check_wd, sta__range=[str(start_time), str(end_time)]
    )
    

    return render(
        request,
        "showFlights.html",
        {"Fl": Fl, "weekday": weekday, "group": group.upper()},
    )


