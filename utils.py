import random

def sample_MNIST_with_all_labels(dataset):
    images = {}
    while True:
        index = random.randint(0, len(dataset))
        image, label = dataset[index]
        if label not in images:
            images[label] = image

        # If images of all labels are sampled, break.
        if len(images) == 10:
            break
    
    return images
