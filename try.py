import sys

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
        tmpnum=float(x[i])/float(num)

      nums.append(x[i])

      if calc(exclude(x,i),tmpnum) :return True
      else: 
        stack.pop()
        nums.pop()
  return False

def getlevel(opitem):
  try:
    
    res=op.index(opitem)/2
    
    return res
  except:
    return 4


levels=[]

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
  print(outstr) 
else:
  print(' False.')
        
      
   
