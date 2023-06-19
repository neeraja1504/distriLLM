import torch
from torch.utils.data import Dataset
from torchtext import datasets
import pandas as pd
from torch.utils.data import DataLoader

train_dataset=pd.read_csv("enter link here")
test_dataset = pd.read_csv("enter link here")

class CustomDataset(Dataset):
  def __init__(self,train):
    super().__init__()
    self.sequences = train['sequence']
    self.mus = train['mu']
    self.sigmas = train['sigma']

  def len(self):
    return len(self.mus)

  def getitem(self,idx):
    sequence = self.sequences[idx]
    mu = self.mus[idx]
    sigma = self.sigmas[idx]
    return sequence, mu, sigma

training_data = CustomDataset(train_dataset)
test_data = CustomDataset(test_dataset)

#Dataloader
train_dataloader = DataLoader(training_data,batch_size=64,drop_last=True)
test_dataloader = DataLoader(testing_data,batch_size=64,drop_last=True)