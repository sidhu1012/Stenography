#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('\t\t\t\t\tYour Personal Stenographer')


# In[8]:


def encode(text):
    print()
    global sten_dict
    l=[]
    for i in text:
        l.append(sten_dict[i])
    s=''.join(l)
    print(s)


# In[11]:


def decode(text):
    print()
    global eng_dict
    l=[]
    for i in text:
        l.append(eng_dict[i])
    s=''.join(l)
    print(s)


# In[13]:


global sten_dict
global eng_dict
sten_dict={'a':'`','b':'~','c':'=','d':'+','e':'-','f':'_','g':'|','h':'1','i':'2','j':'3','k':'4','l':'5','m':'6','n':'7','o':'8','p':'9','q':'0','r':'<','s':':','t':';','u':'/','v':'"','w':"'",'x':'[','y':'{','z':'>','1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')',' ':']','.':'}'}
eng_dict={'`':'a','~':'b','=':'c','+':'d','-':'e','_':'f','|':'g','1':'h','2':'i','3':'j','4':'k','5':'l','6':'m','7':'n','8':'o','9':'p','0':'q','<':'r',':':'s',';':'t','/':'u','"':'v',"'":'w','[':'x','{':'y','>':'z','!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9',')':'0',']':' ','}':'.'}


# In[16]:


text=input('Enter your text: ')
print('1.Encode\n\n2.Decode')
text.lower()
n=int(input('Enter Choice: '))
if n==1:
    encode(text)
if n==2:
    decode(text)


# In[ ]:





# In[ ]:





# In[ ]:



        

