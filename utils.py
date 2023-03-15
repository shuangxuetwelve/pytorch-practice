# Python imports
import random
import time

# PyTorch imports
import torchvision

def sample_MNIST_with_all_labels(dataset):
    images = {}
    while True:
        index = random.randint(0, len(dataset)-1)
        image, label = dataset[index]
        if label not in images:
            images[label] = image

        # If images of all labels are sampled, break.
        if len(images) == 10:
            break
    
    return images

class Timer():

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    # Get the duration in seconds.
    def getDuration(self):
        return self.end_time - self.start_time    
    
class MNIST(torchvision.datasets.MNIST):

    cache = {}

    def __init__(self, path, train=True, transform=None):

        super().__init__(path, download=True, train=train, transform=transform)

        # Access all samples to pre-cache them.
        for idx in range(self.__len__()):
            self.__getitem__(idx)

    def __len__(self):

        return super().__len__()
    
    def __getitem__(self, idx):

        if idx in self.cache:
            return self.cache[idx]
        else:
            self.cache[idx] = super().__getitem__(idx)
            return self.cache[idx]
