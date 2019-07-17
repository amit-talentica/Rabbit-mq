#!/usr/bin/env python
# coding: utf-8

# RabbitMQ::  RabbitMQ is a message broker: it accepts and forwards messages. You can think about it as a post office: when you put the mail that you want posting in a post box, you can be sure that Mr. or Ms. Mailperson will eventually deliver the mail to your recipient. In this analogy, RabbitMQ is a post box, a post office and a postman.
#
# The major difference between RabbitMQ and the post office is that it doesn't deal with paper, instead it accepts, stores and forwards binary blobs of data ‒ messages.

# # RabbitMQ libraries

# # (using the Pika Python client)

# In[1]:


import pika
import os,sys


# In[2]:


#The first thing we need to do is to establish a connection with RabbitMQ server.


# In[3]:


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


# In[4]:


#we need to make sure that RabbitMQ will never lose our queue. In order to do so, we need to declare it as durable


# In[5]:


channel.queue_declare(queue='task_queue', durable=True)


# In[6]:


message = ' '.join(sys.argv[1:]) or "How I can help you?"


# In[7]:


#At that point we're sure that the task_queue queue won't be lost even if RabbitMQ restarts. Now we need to mark our messages as persistent -
#by supplying a delivery_mode property with a value 2.


# In[8]:


channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))


# In[9]:


print(" [x] Sent %r" % message)
#connection.close()


# In[ ]:
