#!/usr/bin/env python
# coding: utf-8

# ### Cool Dank L33t Sp3aK Language BROOO
# Changes letters to numbers to create Brian's stupid "hacker language," also known as "Leet Speak."

# In[1]:


def hacker(text):
    for ch in ['a', 'e', 'i', 'o', 'u', 's']:
        if ch in text:
            text = text.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('u', 'V').replace('s', '$')
    return text


# In[2]:


text = input("Type in a sentence and we'll l33t-i-fy it for you: ")


# In[3]:


print (hacker(text))

