#............DATA TYPES IN PYTHON......(14)..........\\
#............FUNDAMENTAL DATATYPES................\\
#................hello world..........................\\
print("HELLO WORLD!")
#.........INTEGER.............\\
a=123
print(a)
print(type(a))
#..............FLOAT...........\\
b=17.05
print(b)
print(b,type(b))
#...............BOOLEN.........\\
c=True
d=False
print(c,type(c))
print(d,type(d))
#..............SPECIAL EXAMPLES.........\\\
e=True
g=False
print(e,type(e))
print(g,type(g))
print(True+True)
print(True+False+2)
print(True>False)
print(True*False)
print(False)
print(True+False==True)
print(True/True)  
#..............COMPLEX..........\\
f=2+3j
h=2-10j
i=2.3+3.4j
j=2+3.7j
print(f,type(f))
print(h,type(h))
print(i,type(i))
print(j,type(j))

#...........SEQUENCE DATATYPES..............\\
#...........STRING..........................\\
s1="MOTHUKURI ANJANIKUMAR"
s2="MAK"
print(s1,type(s1))
print(s2,type(s2))
#...............SINGLINE STRING DATA..........\\
s3="MOTHUKURI SWATHI"
s4='MOTHUKURI SRINIVAS'
print(s3,type(s3))
print(s4,type(s4))
#..................MULTILINE STRING DATA...........\\
s5="""""MY BROTHER NAME IS MOTHUKURI TEJEGANESH AND 
        HE IS BTECH 3rd YEAR AML DEPARTMENT 
        COLLEGE NAME IS RITE RAJAMUNDRY """
s6=''''my member of brother is 7 members
       1st one is MOTHUKURI PRASAD
       2nd one is MOTHUKURI MANI
       3rd one is MOTHUKURI VENKATESH
       4th one is MOTHUKURI MARKENDEYA SWAMI
       5th one is MOTHUKURI SAI KRISHNA
       6th one is ME MOTHUKURI ANJANIKUMAR
       7th one is MOTHUKURI TEJAGANESH'''
#.............BYTES................\\
l1=[10,20,23,0,256]
print(l1,type(l1))
#b=bytes(l1)...value error invalid\\
b=bytes(l1)
print(b,type(b))
for v in b:
    print(v)
#................BYTE ARRYA.............\\
l=[10,17,5,2004,0]
ba=bytearray(l)
print(ba,type(ba))
print(id(ba))
for kvr in ba:
    print(kvr)

ba[1]=2005
for kvr in ba:
    print(kvr)

print(id(ba))
print(ba[0])
print(ba[2])
#................RANG........\\
r=range(13)
print(r,type(r))
for v in r:
    print(v)

r1=range(13,79)
print(r1,type(r1))
for v in r1:
    print(v)
#........................LIST DATATYPES (COLLECTION DATATYPES)..........\\
#........................LIST DATATYPES(MUTABLE(CHANGEABLE))....[]........\\
lst1=[10,20,-13,79,10]
print(lst1,type(lst1))
lst2=[13,"MAK","AK",79.13]
print(lst2,type(lst2))
listobj=[]           #..........EMPTY LIST.....\\
listobj=list()       #...........EMPTY LIST.....\\
#..........................TUPLE.......()........\\
t1=(13,"MAK",10,80,79)  
print(t1)
print(t1[3])
print(t1[1:4])
print(t1[1::5])
#....................SET DATATYPES......{}..............\\
s1={10,20,13,79,-40}
print(s1,type(s1))
#...................DICT DATATYPE....(KEY,VALUE).........\\
#......................EMPTY DICT...........................\\
d1={}
print(d1,type(d1))
len(d1)
d3=[name]="anjani"
d3=[prof]="student"
d3=[place]="nl"
print(d3,type(d3))
d1["place"]="nether lands"
print(d1,type(d1))
#..................NON EMPTY DICT..........\\
d2={13:"APPLE",15:"MANGO"}
print(d2,type(d2),id(d2))
d2[10]="GUVA"
print(d2,type(d2),id(d2))