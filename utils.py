# Python imports.
import random
import time

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
