#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fib2(n):  # return Fibonacci series up to n 
    result  =  [] 
    a ,  b  =  0 ,  1 
    while  b  <  n : 
        result . append ( b ) 
        a ,  b  =  b ,  a + b 
    return  result


# In[ ]:




