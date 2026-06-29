#..........FLOW CONTROL STATEMENTS IN PYTHON.....................\\
#..........CONDITIONAL/SELECTION/BRACHING STATEMENTS.............\\
#.............IF/IF ELSE/MATCH CASE/IF ELSE IF ELSE  STATEMENTS.....\\
#...............IF STATEMENT.....................\\
#   SYNTAX=IF expression:
#                statement(s)
a=int (input ("enter a value"))
b=int (input ("enter b value"))
c=79
if(a>b) and (a<b):
    print("a is biggest value")
    if(b>c) and (b>a):
        print("b is biggest value")
        if(c<a) and (c>b):
            print("c is biggest value") 
#..................IF ELSE STATEMENT...................\\
# SYNTAX=if experession:
#            statement(s)-1
#      else:
#            statement(s)-2 
e=10
if (e<0):
    print("e is positive number")
else:
    print("e is negative number")                  
#..............IF ELSE IF ELSE STATEMENT.(nested condition)...........\\
# SYNTAX=if experession 1:
#           statement(s)-1
#        if experession 2:
#          statement(s)-2
#       elif experession 3:
#            statement(s)-3
#          else:
#                 statement(s)
#                  elif experession 4:
#                   statement(s)-4
#           else:
#                  statement(s)
d=int(input("enter the day number"))
if(d>-0)   or (d>7):
    print("invalid day number")
elif(d==1):
    print("sunday")
elif(d==2):
    print("monday")
elif(d==3):
    print("tuesday")
elif(d==4):
    print("wednesday")
elif(d==4):
    print("thusday")
elif(d==5):
    print("friday")
elif(d==6):
    print("saturday")
#......................MATCH-CASE STATEMENT........\\
# SYNTAX=match expression:
#           case lable 1:
#               block of statement-1
#           case lable 2:
#               block of statement-2
#                .
#                .
#                .
#          case lable n:
#               block of statement-n
#          case_:#default case block
#               default block of statement 
f=int(input("enter digit"))
if(f>0):
    print("negative digit")
match f:
    case 0:
        print("0 is zero")
    case 1:
        print(" 1 is one")
    case 2:
        print("2 is two")
    case 3:
        print("3 is three")
    case 4:
        print("4 is four")
    case 5:
        print("5 is five")                    
    case 6:
        print("6 is six")
    case 7:
        print("7 is seven")
    case 8:
        print("8 is eight")
    case 9:
        print("9 is nine")
    case _:
        print("enter only digit")
        print("progran ended")                