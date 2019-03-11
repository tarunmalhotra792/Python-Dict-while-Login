#Life for 'for'
'''
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum=0
for val in numbers:
    sum=sum+val
    print"Sum of",val,"is", sum
    print(tuple(range(10)))
'''
'''
genre = ['pop', 'rock', 'jazz']

for i in genre:
    print(i)
'''
'''
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print genre,genre[i]
    '''
'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''
'''
a = ['booze', 'bar', 'ghar', '34','corge'] #5
s = ['Choze','ghar','bazi','12'] #4


for x in range(len(a)):
    print a[x] +"-"+ s[x]
    print a,s,x
else:
    print "pta n kya ho ra hai"

'''
'''
for i in range(5):
    for j in range(i):
        print i,"-",j
    else:
        print "If loop else"
else:print "for loop else"
'''
'''

i=[1,2,3,4,5]
j=[2,3,4,5,6]

for x in range(len(i)):
    
    print i[x] ,j[x]
---------------------------------
OUTPUT
1 2
2 3
3 4
4 5
5 6
---------------------------------
'''
'''
i=[1,2,3,4,15]
y=i[]
for x in range(len(i):
    for y in range(x):
        print i[x],i
        '''
'''

j=[5,4,3,2]
for i in range(len(j)):
    print (j-i) * j[i],i 

'''



#Entering Username and Password for cred_check
user=raw_input("Please enter your user_id\n")
pswd=raw_input("Please enter your password for username {0}\n".format(user))

#Defining the default dictionary
Dic={'User1':'123user1','User2':'123user2'}

#Defining the function


if user in Dic and Dic[user] == pswd:
    print 'shi hai'
else:
    print 'galat hai'
print Dic.has_key(user)
    
print Dic.viewvalues()
print Dic.values()
print [user for user, pswd in Dic.items() if user == 'User1']
