#!/usr/bin/env python
# coding: utf-8

f1=open('producer_message.txt', 'r')
f2=open('consumer_message.txt', 'r')
contents_f1=f1.read()
contents_f2=f2.read()

l1=[]
for word in contents_f1.split():
        l1.append(word)
s1=set(l1)

l2=[]
for word in contents_f2.split():
        l2.append(word)
s2=set(l2)

s3=s1.difference(s2)
l3=list(s3)

f3=open('data_loss.txt','w')



f3.write('\n'.join(str(line) for line in l3))


# In[104]:


f3.close()


# In[ ]:




