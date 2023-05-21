# import datetime

# date_default_timezone_set('Asia/kolkata');
# $day=date('l');
# $days_num=date('z');
# echo date('z');
# echo $day;
# $dat= date('d m Y' );
# //echo date(' G i s' );
# $date=date('d');
# $mon=date('m');
# $year=date('Y');
# $hour=date('g');
 
# $min=date('i');
# $time=date('G i');
# $rem=$days_num % 8;
# echo $rem;
# $count=$rem % 4;

	# switch ($count) {
        
    # 	case   0:
    #         $mor='G-3';
    #         $aft='G-3';
    #         $ngt='G-4';
    #         $ga='3';
    #         $gm='2';
    #         $gn='4';
    #         break;
    #     case 1:
    # 	    $mor='G-1';
    #         $aft='G-2';
    #         $ngt='G-3';
    #         echo $erem;
    #         $ga='2';
    #         $gm='1';
    #         $gn='3';
    #         break;
        
        
#         case 2:
#     	    $mor='G-4';
#             $aft='G-1';
#             $ngt='G-2';
#             $ga='1';
#             $gm='4';
#             $gn='2';
#     	    break;
#         case  3:
#                     $mor='G-3';
#                     $aft='G-4';
#                     $ngt='G-1';
#                     $ga='4';
#                     $gm='3';
#                     $gn='1';
#                     break;

#                     default:
#                     echo "i is freecodecamp";
#                     break;    
    	
#         }
#     echo $rem;
#     echo $mor;
#     echo $gm;
#     echo $time;

    # if($time>'06 30' && ($time<'13 30')) {
    #     echo 'success m';
    #     $shift='Morning';
    #     $gp=$mor;
    #     $g=$gm;
    # }
    
    # //   } elseif( ($time>='06 30') && ($time<='13 00')) {
          
#     //     echo 'success a';
#     //     $shift='Afternoon';
#     //      $gp=$aft;
#     //      $g=$ga;
#     //   } elseif ($time>='21 01' && $time<='07 00'){
#     //     echo 'success n';
#     //         $shift='Night';
#     //         $gp=$ngt;
#     //         $g=$gn;  
#     //   }
    
    

    


   
# ?>

#First, we find the reminder:

import datetime
from num2words import num2words

def my_function(a):

    current_time = datetime.datetime.now().time()


    op = raw_number

    if (op == 0 or op == 1):

            night= "Group 1"
            morning= "Group 2"
            afternoon= "Group 3"

    elif (op == 2 or op == 3):
        night= "Group 3"
        afternoon= "Group 2"
        morning= "Group 1"
    elif (op == 4 or op == 5):
        morning= "Group 4"
        night= "Group 2"
        afternoon= "Group 1"
    elif (op == 6 or op == 7):
        afternoon= "Group 4"
        morning= "Group 3"
        night= "Group 1"

    if current_time > datetime.time(6, 30) and current_time < datetime.time(13, 30):
        print(morning)
    elif current_time > datetime.time(13, 30) and current_time < datetime.time(21, 30):
         print(afternoon)
    else:
        print(night)
  # prints "one"
# print(my_function(3))  # prints "invalid argument"


now = datetime.datetime.now()
next_day = now + datetime.timedelta(days=0)
days = int(next_day.strftime("%j"))
print("Number of days:", days)

raw_number = days % 8
print(raw_number)

my_function(raw_number)
#0, 1, 2, 3, 4, 5, 6, 7


import turtle
import math

# Define the polar curves
def polar_curve1(t):
    return 4 * (1 + math.cos(t))

def polar_curve2(t):
    return 5 * (1 - math.cos(t))

# Define the function to plot the angle between two curves
def plot_angle(theta):
    turtle.pencolor("blue")
    turtle.left(theta)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(theta)

# Define the function to plot the curvature
def plot_curvature(curvature):
    turtle.pencolor("red")
    turtle.circle(1 / curvature, abs(curvature) * 10)

# Set up the turtle graphics window
turtle.setup(800, 600)
turtle.setworldcoordinates(-15, -15, 15, 15)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Plot the polar curves
for t in range(0, 628, 1):
    theta = t / 100
    turtle.pencolor("green")
    turtle.goto(polar_curve1(theta) * math.cos(theta), polar_curve1(theta) * math.sin(theta))
    turtle.pencolor("purple")
    turtle.goto(polar_curve2(theta) * math.cos(theta), polar_curve2(theta) * math.sin(theta))

# Plot the angle between the curves
for t in range(0, 628, 1):
    theta = t / 100
    curve1_slope = (polar_curve1(theta + 0.01) - polar_curve1(theta)) / 0.01
    curve2_slope = (polar_curve2(theta + 0.01) - polar_curve2(theta)) / 0.01
    angle = math.degrees(math.atan(abs((curve2_slope - curve1_slope) / (1 + curve1_slope * curve2_slope))))
    plot_angle(angle)

# Plot the curvature
for t in range(0, 628, 1):
    theta = t / 100
    curve1_slope = (polar_curve1(theta + 0.01) - polar_curve1(theta)) / 0.01
    curve1_second_derivative = (polar_curve1(theta + 0.02) - 2 * polar_curve1(theta + 0.01) + polar_curve1(theta)) / 0.0001
    curve1_curvature = abs(curve1_second_derivative / math.pow(1 + math.pow(curve1_slope, 2), 1.5))
    plot_curvature(curve1_curvature)

    curve2_slope = (polar_curve2(theta + 0.01) - polar_curve2(theta)) / 0.01
    curve2_second_derivative = (polar_curve2(theta + 0.02) - 2 * polar_curve2(theta + 0.01) + polar_curve2(theta)) / 0.0001
    curve2_curvature = abs(curve2_second_derivative / math.pow(1 + math.pow(curve2_slope, 2), 1.5))
    plot_curvature(curve2_curvature)

turtle.done()



