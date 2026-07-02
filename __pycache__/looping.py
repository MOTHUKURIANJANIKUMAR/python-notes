#.............................LOOPING STATEMENTS............\\
#.................LOOPING/ITERATIVE/REPETITING STATEMENTS..........\\
#............WHILE/FOR STATEMENTS.......................\\
#.................WHILE OR WHILE....ELSE................\\
#SYNTAX=initialization part
#       conditional part
#       updation part(increment and decrement)
#....while else....SYNTAX=while expression or while (test condition):
#                               statement(s)
#                               updation
#                             else:
#                                 statement(s)
n=int(input("enter the n value"))
i=2
while(i<=n):
     print(i)
     i=i+2
else:
     print("{} is negative value format(i)")     
#...........FOR OR FOR ELSE...............\\
#SYNTAX=for iterating_var in squence:
#           statement(s)
#       else:
#            statement(s)
i=int(input("Enter the i value"))
for i in range(4):
    print(i)
#.................BREAK STATEMENT..........\\
# SYNTAX=for var in iterable_object:
#        if (test cond):
#            break
# SYNTAX 2= initialization
#           while(test cond-1):
#               if(test cond-2):
#                   break
#              updation part
f=int(input("Enter the f value"))
for f in range(1,8):
     if f== 3:
        break 
print(f)
print("Loop is finished!")
#..............CONTINUE STATEMENT..........\\
#SYNTAX=for varname in iterble_object:
#        if(test cond):
#          continue
#         statement-1
#         statement-2
#         statement-n
#SYNTAX 2= initialization
#            while(expression):
#               if(test cond):     
#                  continue
#                  updation part
#                statement-1
#                statement-2
#                statement-n
g=int(input("Enter the g value"))
for g in range(1,5):
     if g== 3:
        continue
print(g)
print("Loop is finished!")
#.......................PASS STATEMENT.............\\
#SYNTAX= for varname in iterable _object:
#        if (test cond):
#            pass
h=int(input("Enter the h value"))
for h in range(1,4):
     if h== 3:
        pass
print(h)
print("Loop is finished!")