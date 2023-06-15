import numpy as np
mu, sigma = 0, 0.1
s = np.random.default_rng().normal(mu, sigma, 10)
print(s)

mega_list=[]
mu_list=[]
sigma_list=[]
list1=[]
for i in range(0,50):
  mu = np.random.randn()*10
  sigma = abs(np.random.randn()*10)
  for j in range(0,140):
    list1 = np.random.default_rng().normal(mu, sigma, 128)
    mega_list.append(list1)
    mu_list.append(mu)
    sigma_list.append(sigma)
    
print(mu_list)
print(sigma_list)
print(mega_list)