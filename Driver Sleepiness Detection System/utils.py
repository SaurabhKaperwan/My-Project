import numpy as np

def calci(x,y):
  return(np.linalg.norm(x-y))

def compute_eyes(e1,e2,e3,e4,e5,e6):
  up=calci(e2,e4)+calci(e3,e5)
  down=calci(e1,e6)

  ans=up/(2.0*down)
  if(ans>0.25):
    return 2
  elif(ans>0.21 and ans<=0.25):
    return 1
  else:
    return 0


def compute_lips(lips):
  upper_lip= lips[50:53]
  upper_lip=np.concatenate(upper_lip,lips[65:68])
  
  lower_lip=lips[56:59]
  lower_lip=np.concatenate(lower_lip,lips)
  
  mid1=np.mean(upper_lip,axis=0)
  mid2=np.mean(lower_lip,axis=0)
  
  return((abs(mid1[1]-mid2[1])))import numpy as np

def calci(x,y):
  return(np.linalg.norm(x-y))

def compute_eyes(e1,e2,e3,e4,e5,e6):
  up=calci(e2,e4)+calci(e3,e5)
  down=calci(e1,e6)

  ans=up/(2.0*down)
  if(ans>0.25):
    return 2
  elif(ans>0.21 and ans<=0.25):
    return 1
  else:
    return 0


def compute_lips(lips):
  upper_lip= lips[50:53]
  upper_lip=np.concatenate(upper_lip,lips[65:68])
  
  lower_lip=lips[56:59]
  lower_lip=np.concatenate(lower_lip,lips)
  
  mid1=np.mean(upper_lip,axis=0)
  mid2=np.mean(lower_lip,axis=0)
  
  return((abs(mid1[1]-mid2[1])))
