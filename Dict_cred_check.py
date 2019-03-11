

#Defining the default dictionary
Dic={'User1':'123user1','User2':'123user2'}

def func_success_login():
    globals().update(flag=0) 
    print 'Welcome {}, hope you enjoy our site'.format(user)
    
def func_Unsuccessfull_login():
    inp=input("Ohh! It seems like you are a new customer\n\nPlease press 1 if you would like to register:-\n\nplease press 2 if you would like to exit:-\n")    
    if inp==1:
        Dic[user]=pswd
        globals().update(flag=0)
        print Dic
        print "Thanks Mr",user,"for registerng with us"
    if inp==2:
        globals().update(flag=2)
        print "Hope we will see you again"

#condition to check
flag=0
while flag<=1:
    #Taking inputs for UserId and Password
    user=raw_input("Please enter your user_id\n")
    pswd=raw_input("Please enter your password for username {0}\n".format(user))
    if Dic.has_key(user)==True and Dic[user] == pswd :
        func_success_login()
        break
    else:
        func_Unsuccessfull_login()
        
         
#Defining the function

        
#Entering Username and Password for cred_check
    





    
        
    

'''
if Dic.has_key(user)==True:
if user in Dic and Dic[user] == pswd:    
'''
