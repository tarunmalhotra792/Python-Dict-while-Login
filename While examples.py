#Sum the numbers according to there occurences 
'''
n1=int(raw_input('Please eneter the no of values to be added:-'))
i=int(raw_input('Please eneter the starting point of number:-'))
sum=0
while i<10:
    sum=sum+i
    print "The sum is {} and the occurence is {}".format(sum,i)
    i=i+1
else:
    print "Deal done"
'''

#Printing squence  and all
'''
n1=int(raw_input('Please eneter the no where you would like to stop:-'))

i=5
print"welcome to the world of printing %d and %d " %(n1,i)
while n1>i:
    print "sequience is {} {}".format(i,n1)
    i=i+1
    print "the number is ",i,n1
else:
   print "don't know what is happening"
'''
'''
n1=int(raw_input('Please eneter the no where you would like to stop:-'))#50
i=input('Please eneter the itertation number:-')#10
print"welcome to the world of printing %d and %d " %(n1,i)
while n1>i: #50>10
    if i<n1/2: #10<25
        print "sequience is" ,n1/2 ,'{} {}'.format(i,n1)
        i=i+1
else:
    print "don\'t know what is happening"



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''
'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''
'''
counter = 0

while counter < 3:
    print("Inside loop",counter)
    counter =counter+1
    print("Inside -2 loop - 2",counter)
    
    print("  counter = counter + 1Inside -3 loop - 3",counter)
    print "chak"
    print "det"
    x=10
    print(x)
else:
    print("Inside else")

'''
'''
Difference btwe break and continue
i = 1
while i < 6:
  print(i)
  if i == 3:
    continue
  i += 1

 '''

'''
a=['lop','sdf',122]
b=['lop','sdfg',122]
mergedlist = tuple(set(a + b))
print mergedlist
'''
'''
a = ['foo', 'bar', 'baz']
while a:
    print a
    print(a.index('bar'))
'''
'''
n = 5
while n > 0:
    print n
    n -= 1
    print n
    if n == 2:
        continue
    print(n)
print('Loop ended.')
'''
'''
n = 5
while n > 0:
    print n
    n =n-1
    print n
    if n == 2:
        continue
    print(n)
print('Loop ended.')
'''
'''
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')
'''
#I want to concatonate  a[0] with a[s][0]....a[s][n] 
'''
a = ['booze', 'bar', 'ghar', '34','corge'] #5
s = ['Choze','ghar','bazi','12'] #4
i=0
while i<len(a):  #0<5
    while a[i]<len(s): #0<4
        t=a[i]+ "-" +s[i]
        i+=1
    print t
else:
    print "pta n kya ho ra hai"
'''
'''
a=['lop','sdf',122]
b=['lop','sdfg']

print a,b
i=0
while i<len(a):
    for a[i] in b:
        print a[i],b[j],' 'yeah'
        i-i+1
else:
    print 'a[i],b[j],' "not in a"
'''
'''
a = ['booze', 'bar', 'ghar', '34','corge'] #5
s = ['Choze','ghar','bazi','12'] #4

i=0
for y in range(len(s)):
    print a[y]
    i+=1  
else:
    print "pta n kya ho ra hai"
'''

def swap(x, y): 
    temp = x; 
    x = y; 
    y = temp;
    x=2
    y=3

    print(x)
    print(y)




