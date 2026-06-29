#..............OPERATORS IN PYTHON.............\\
#...............ARITHMETIC OPERATOR.............\\
a=10
b=3
print(a+b) #.......addtion....\\
print(a-b) #.......subtraction....\\
print(a/b) #.......division......\\
print(a*b) #.......multiplication...\\
print(a//b) #.....floor division...\\
print(a%b) #.......modulo division...\\
print(a**b) #......exponenation.......\\
#..............ASSIGNMENT OPERATOR....................\\
#..............SINGLE&MULTI LINE ASSIGNMENT............\\
#SYNTAX:var name=value\\\\\var name1=var name2\\\var name=expression.....\\\
#...............SINGLE LINE ASSIGNMENT................................\\
c=10
d=20
e=c+d
print(c,d,e)
#.........................MULTI LINE ASSIGNMENT.........................\\
# SYNTAX:var1,var2.........varn=val1,val2,................val n  &
#        var1,var2............varn=exp1,exp2..............exp n
print(c,d,e)
stno=10
sname="MAK"
marks=9.90
print(stno,sname,marks)
#..................RELATIONAL OPERATOR..........................\\
print(a>b)  #..greater then
print(a<b)  #..less then
print(a==b)  #..equalto
print(a>=b)  #..greater then orequalto
print(a<=b)  #..less then orequalto
print(a!=b)  #..not equal to
#............Logical operator.................................\\
# ............SYNTAX=(Rel-Exp1)logical operator(Rel-Exp2)...........\\
# ...............and/or/not...............................\\
#............and.............\\
f=10
g=10
h=10
print(f,g,h)
print((f>g) and (f>=h))
print((h<g) and (f<=h))
print((10>2) and (10==5))
#................or..................\\
print((f!=g) or (f==10))
print((f>=g) or (f==10))
print((f<=g) or (f!=10))
#.................not.................\\
print(not(f!=g) or (f==10))
print(not(f==g) and (f==20))
10>=4
print(not(10>=4))
#.....................BITWISE OPERATOR....................\\
#.........BITWISE-left shift/right shift/or/and/complement/xor///
#..........BITWISE-LEFT SHIFT OPERATOR............\\
rs=10<<3
print(rs)
#...........BITWISE-RIGHT SHIFT OPERATOR.............\\
ak=23>>2
print(ak)
#...........BITWISE-OR OPERATOR.......................\\
#...........BITWISE-AND OPERATOR.......................\\
#............BITWISE-COMPLEMENT OPERATOR..............\\
~g
print(~g)
~b
print(~b)
#................BITWISE-XOR OPERATOR....................\\
#................MEMBERSHIP OPERATOR.....................\\
#....................IN OR NOTIN........................\\
s="PYTHON"
print("p" in s)
print("TH" in s)
print("ON" in s)
print("PY" not in s)
#......................IDENTITY OPERATOR..............//
#.....................IS OR NOTIS.......................\\
x=None
y=None
print(x,id(x))
print(y,id(y))
print(x is y)
print(x is x)
d1={10:"APPLE",13:"HoT",79:"SWEET"}
d2={10:"APPLE",13:"HoT",79:"SWEET"}
print(d1,id(d1))
print(d2,id(d2))
print(d1 is d2)
print(d1 is not d2)