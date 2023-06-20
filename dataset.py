import numpy as np
mu, sigma = 0, 0.1
s = np.random.default_rng().normal(mu, sigma, 10)
print(s)

mega_list=[]
mu_sigma_list=[]
list1=[]
pos=[]
sequence=[]
for i in range(0,50):
  mu = np.random.rand()*10
  sigma = abs(np.random.rand()*10)
  for j in range(0,140):
    list1 = np.random.default_rng().normal(mu, sigma, 128)
    mega_list.append(list1)
    temp=[mu,sigma]
    mu_sigma_list.append(temp)
for i in range(128):
  pos.append(i/128)
for i in mega_list:
  temp=[i,pos]
  sequence.append(temp)
    
    

print(mega_list)
print(mu_sigma_list)