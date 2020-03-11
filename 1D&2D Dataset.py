import numpy as np
from torch.utils import data

class Dataset1D(data.Dataset):
    def __init__(self):
        super().__init__()
        self.sample_array = np.random.rand(30,)
        print(self.sample_array)

    def __len__(self):
        return len(self.sample_array)

    def __getitem__(self,index):
        item = self.sample_array[index]
        return item

class Dataset2D(data.Dataset):
    def __init__(self):
        super().__init__()
        self.sample_npy = np.random.rand(10,20)
        # print(self.sample_npy)
    
    def __len__(self):
        return len(self.sample_npy)
    
    def __getitem__(self, index) :
        item = self.sample_npy[index, :]
        return item

myDataset = Dataset1D()
data_generator = data.DataLoader(myDataset, batch_size = 2)
for batch in data_generator:
    print(batch)
    