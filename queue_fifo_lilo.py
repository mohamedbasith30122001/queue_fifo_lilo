Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import collections
q_r=collections.deque()
q_l=collections.deque()

def insert_right_queue():
  print("First in")
  element=input()
  q_r.append(element)
  print(q_r)

def remove_left_queue():
  if not q_r:
    print("Queue is empty!")
  else:
    print("First out")
    q_r.popleft()
    print(q_r)


def insert_left_queue():
  print("Last in")
  element=input()
  q_l.appendleft(element)
  print(q_l)

def remove_right_queue():
  if not q_l:
    print("Queue is empty!")
  else:
    print("Last out")
    q_l.pop()
    print(q_l)

while True:
  print("select the option")
  print("1-FIFO \n2-LILO \n0-EXIT")
  option=int(input())
  if option==1:
    while True:
      print("select the option")
      print("1-ENQUEUE(first insert) \n2-DEQUEUE(first delete) \n0-EXIT")
      select=int(input("enter the selection:"))
      if select==1:
        insert_right_queue()
      elif select==2:
        remove_left_queue()
      elif select==0:
        break
      else:print("enter correct selection")
  elif option==2:
    while True:
      print("select the option")
      print("1-ENQUEUE(last insert) \n2-DEQUEUE(last delete) \n0-EXIT")
      selection=int(input("enter the selection:"))
      if selection==1:
        insert_left_queue()
      elif selection==2:
        remove_right_queue()
      elif selection==0:
        break
      else:print("enter correct selection")
  elif option==0:
    break
  else:print("enter the correct option")
