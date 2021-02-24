import sys
from copy import copy
# usage: python try.py 1 2 3 4
s=[]
for i in range(4):
  s.append(int(sys.argv[1+i]))

stack=[]

op=['+','-','*','/']

nums=[]


def exclude(x,index):
  out=[]
  for i in range(len(x)):
    if i!=index:
      out.append(x[i])
  return out

def multi(listx):
  res=1
  for item in listx:
    res*=item
  return res

def enum(a):
  if len(a)==1:return [a]
 
  current=[]
  new_current=[]
  all_list=[]
  #print(a)
  for i in range(len(a)):
    current.append(a[i])
    x=enum(exclude(a,i))
    #print(x)
    for item_list in x:
      new_current=copy(current)
      for item in item_list:
        new_current.append(item)
      all_list.append(new_current)
    current=[]
  #print(all_list)
  return all_list


def calc(x,num):
  if len(x)==1:
    if abs(x[0]-num)<0.001:
      nums.append(x[0])
      return True
    else:return False

  if multi(x)<num:
    return False
  res=0
  
  for i in range(len(x)):    
    for opi in range(4):
      stack.append(op[opi])
      
      if opi==0:
        tmpnum=num-x[i]
        if tmpnum<0:
          stack.pop()
          stack.append('-')
          tmpnum=x[i]-num
    
      elif opi==1:
        tmpnum=x[i]-num
      elif opi==2:
        tmpnum=float(num)/float(x[i])
      else:
        if num==0: 
          stack.pop() 
          break
        else:tmpnum=float(x[i])/float(num)
      nums.append(x[i])
      if calc(exclude(x,i),tmpnum) :return True
      else: 
        stack.pop()
        nums.pop()
  return False


def op_type(a,b,i):
  if i==0:
    return a+b
  elif i==1:
    return a-b
  elif i==2:
    return a*b
  elif i==3:
    if b==0:return 99999
    else:return float(a)/float(b)

def basic(listx):
 # print(listx)
  a,b,c,d=listx
  outstr='False.'
  for i in range(4):
    for j in range(4):
      for k in range(4):
        if (getlevel(op[i])==getlevel(op[k])) and not( getlevel(op[i])==getlevel(op[j]) ) and op_type(op_type(a,b,i),op_type(c,d,k),j)==24:
          outstr='('+str(a)+op[i]+str(b)+')'+op[j]+'('+str(c)+op[k]+str(d)+') = '+str(op_type(op_type(a,b,i),op_type(c,d,k),j))
          print(outstr)
          sys.exit(1)

def calc_enum(s):
  all_list=enum([0,1,2,3])
  for listx in all_list:
    cur=[]
    for i in range(4):
      cur.append(s[listx[i]])
    basic(cur)
  return



def getlevel(opitem):
  try:
    res=op.index(opitem)/2
    return res
  except:
    return 4


levels=[]

calc_enum(s)

if calc(s,24):
  si=0
  ni=0

  outstr=''
  tmpstr=''+str(nums[0])+stack[0]
  ni+=1
  si+=1
  currentlevel=0
  oldlevel=getlevel(stack[0])
  pro=0
  
  while(si<=2):
    
    currentop=stack[si]
    si+=1
    currentlevel=getlevel(currentop)
    currentnum=str(nums[ni])
    ni+=1
    
    if currentlevel<oldlevel or (currentlevel==oldlevel and ( currentop=='-' or currentop=='/')) :
      tmpstr+='('
      pro+=1
    tmpstr+=currentnum
    tmpstr+=currentop    
   
    outstr+=tmpstr
    tmpstr=''
    oldlevel=currentlevel
   
  outstr+=str(nums[3])
  for i in range(pro):
    outstr+=')'
  outstr+=' = 24'
  print(outstr) 
else:
  print(' False.')
        
      

