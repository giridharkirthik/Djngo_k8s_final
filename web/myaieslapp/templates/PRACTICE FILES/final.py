import datetime
import pandas as pd

# Define the shift schedule as a list of tuples, where each tuple represents a day and its corresponding shift
shift_schedule = [
    ("off", "off"),
    ("morning", "morning"),
    ("afternoon", "afternoon"),
    ("night", "night"),
    ("night", "off"),
    ("morning", "off"),
    ("afternoon", "off"),
    ("off", "off")
]

# Define a function to get the current shift based on the current day and time
def get_shift():
    # DETERMINE THE SHIFT OF THE CURRENT EMPLOYEE
    now = datetime.datetime.now()
    day_of_cycle = (now.date() - datetime.date(2023, 1, 1)).days % len(shift_schedule)
    print(shift_schedule[day_of_cycle])
    return shift_schedule[day_of_cycle]
 
    

# Define a function to allocate employees to flights based on their shift and the flights' arrival and departure times
def allocate_employees_to_flights():
    # Get the current shift
    shift = get_shift()

    # Filter employees by group and shift
    employees = Employees.objects.filter(grp=shift[0], trained=shift[1])

    # Get the flights that arrive and depart during the current shift
    now = datetime.datetime.now()
    flights = FlightSchedule.objects.filter(
        arrival_days__contains=now.strftime("%A"),
        sta__hour=now.hour,
        sta__minute__lte=now.minute
    ).exclude(departure_days="").filter(
        departure_days__contains=now.strftime("%A"),
        std__hour=now.hour,
        std__minute__gte=now.minute
    )

    # Create a DataFrame to hold the allocation data
    allocation_data = []
    for flight in flights:
        allocation_data.append({
            "flight_no_arr": flight.flight_no_arr,
            "flight_no_dep": flight.flight_no_dep,
            "destination_from": flight.destination_from,
            "destination_to": flight.destination_to,
            "employees": []
        })
    allocation_df = pd.DataFrame(allocation_data)

    # Allocate employees to flights
    for employee in employees:
        # Sort the flights by the difference between their sta and the current time
        flights_sorted = flights.order_by(
            abs(now - datetime.datetime.combine(now.date(), flight.sta))
        )

        # Find the flight with the fewest allocated employees
        allocation_counts = allocation_df["employees"].apply(len)
        min_allocation_count = allocation_counts.min()
        flights_min_allocation_count = allocation_df[allocation_counts == min_allocation_count]
        flight = flights_sorted.filter(pk__in=flights_min_allocation_count.index).first()

        # Add the employee to the flight's allocation
        allocation_df.at[flights_min_allocation_count.index[0], "employees"].append({
            "sap": employee.sap,
            "empname": employee.empname,
            "designation": employee.designation,
            "mob": employee.mob,
            "email": employee.email
        })

    return allocation_df.to_dict("records")
