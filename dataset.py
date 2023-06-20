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
    list1.sort()
    mega_list.append(list1)
    temp=[mu,sigma]
    mu_sigma_list.append(temp)
for i in range(128):
  pos.append(i/128)
for i in mega_list:
  temp=[i,pos]
  sequence.append(temp)

sequence_train=[]
sequence_val=[]
sequence_test=[]
mu_sigma_train=[]
mu_sigma_val=[]
mu_sigma_test=[]


sequence_train=sequence[:5000]
sequence_val=sequence[5000:6000]
sequence_test=sequence[6000:7000]

mu_sigma_train=mu_sigma_list[:5000]
mu_sigma_val=mu_sigma_list[5000:6000]
mu_sigma_test=mu_sigma_list[6000:7000]
    

print(mega_list)
print(mu_sigma_list)