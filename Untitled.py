#!/usr/bin/env python
# coding: utf-8

# In[26]:


num = int(input())
row_loop=num+num//2+2
space_handler=0
star_handler=0
space_handler_mid=0
star_handler_mid=0
for i in range(1,row_loop):
    #first inverse tringle
    if i <= num//2+1:   
        if i>1:
            space_handler+=1
            for k in range(space_handler):
                print(' ',end='')
        for j in range(num-star_handler):
                print("*",end='')
        
        if i>1:
            for k in range(space_handler):
                print(' ',end='')
           
    else:
        for j in range(num):
            print(" ",end='')
            
    #Its for middle trigle
    for j in range(num):
        if i<=num:
            if j==0 or j==num-1:
                 print("@",end='')
            else:
               print(' ',end='')
    if i>num:
         
        if i>num:
             for k in range(space_handler_mid):
                    print(' ',end='')

        for j in range(num-star_handler_mid):
                print("@",end='')
        star_handler_mid+=2

        if i>num:
             for k in range(space_handler_mid):
                    print(' ',end='')
             space_handler_mid+=1
            


    #Its for  last and final loop
    if i <= num//2+1:   
        if i>1:
           
            for k in range(space_handler):
                print(' ',end='')
        for j in range(num-star_handler):
                print("*",end='')
        star_handler+=2
       
        if i>1:
            for k in range(space_handler):
                print(' ',end='')
           
    else:
        for j in range(num):
            print(" ",end='')
            
            
        
    print()
        
    
    



# In[ ]:




