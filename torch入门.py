import numpy as  np
import torch
torch.cuda.is_available()  #看看是否支持cuda

np_array=np.arange(6).reshape((2,3))
torch_array=torch.Tensor([[1.0],[2.0]])
print(np_array,'\n')
print(torch_array)

from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad = True)
y = x + 2
y.creator

# y 是作为一个操作的结果创建的因此y有一个creator
z = y * y * 3
out = z.mean()

# 现在我们来使用反向传播
out.backward()

# out.backward()和操作out.backward(torch.Tensor([1.0]))是等价的
# 在此处输出 d(out)/dx
x.grad


open()



file=open('word.txt','r')
file.readline(limit=10)

import pandas as pd

pd.DataFrame(index=[],columns=[])