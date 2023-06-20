import torch
from torch import nn

if torch.cuda.is_available():
  device="cuda"
else:
  device="cpu"

print(device)

from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import AutoTokenizer, AutoModel, BertConfig, BertModel

class BertModelwithLinearLayer(nn.Module):
  def __init__(self):
    super().__init__()
    self.config= BertConfig()
    self.config.update({'hidden_size': 3})
    self.config.update({'num_attention_heads': 1})
    self.config.update({'max_position_embeddings': 3})
    print(self.config)
    # self.model=AutoModel.from_pretrained("bert-base-uncased")
    self.model=BertModel(config=self.config)
    self.linear=nn.Linear(3,2)  #output dim is 2 because we need mu and sigma

  def forward(self,x):
    x = self.model(inputs_embeds=x).pooler_output
    print(x)
    x= self.linear(x)
    return x

# config = BertConfig.from_pretrained("bert-base-uncased")
# config.update({'hidden_size': 2})
# config.update({'num_attention_heads': 1})
# config.update({'max_position_embeddings': 128})
# print(config)
model = BertModelwithLinearLayer().to(device)