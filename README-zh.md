* MNIST-FCN-0: 0个隐藏层的全连接网络。
* MNIST-FCN-1: 1个隐藏层的全连接网络。
    * MNIST-FCN-1-activation: 在1个隐藏层的全连接网络上测试激活函数。
    * MNIST-FCN-1-normalization: 在1个隐藏层的全连接网络上测试归一化。
    * MNIST-FCN-1-learning-rates: 在1个隐藏层的全连接网络上测试learning rate。
* MNIST-FCN-2: 2个隐藏层的全连接网络。
    * MNIST-FCN-2-activation: 在2个隐藏层的全连接网络上测试激活函数。

# Activation

从MNIST-FCN-1-activation的实验可以得出以下结论：
1. 激活函数的使用可以提升模型的能力，但会使模型的收敛速度下降。即使只有一层hidden layer，无论是ReLU还是Sigmoid，都可以使模型的能力超过其线性版本。
2. 在模型没有收敛到一定程度之前，不使用激活函数的线性模型也许比使用了激活函数的模型效果更好。
3. 在不使用normalization的情况下，Sigmoid激活函数的收敛性能比ReLU要差许多。

# Normalization

从MNIST-FCN-1-normalization的实验可以得出以下结论：
1. 使用batch normalization可以使模型更快地收敛。

# Learning Rates

从MNIST-FCN-1-learning-rates的实验可以得出以下结论：
1. learning rate的合理的取值不止是0.001、0.01这种数量级，还可以是1、10这种数量级。
2. learning rate对收敛速度有很大的影响。
3. 在固定优化轮数时，learning rate对训练效果有很大影响。

# Epochs

从MNIST-FCN-1-epochs的实验可以得出以下结论：
1. 不要小看缓慢改善阶段。10-50 epochs使learning rate为10的模型的training准确率从98.5%上升到99.6%、使learning rate为0.01的模型的training准确率从91.5%上升到96%。50-200 epochs使learning rate为10的模型的training准确率从99.6%上升到99.7%、使learning rate为0.01的模型的training准确率从96%上升到98.7%，200-500 epochs使learning rate为10的模型的training准确率从99.7%上升到99.8%、使learning rate为0.01的模型的training准确率从98.7%上升到99.5%。
2. 不同的learning rate，缓慢改善所需要的epoch是不同的。learning rate越大，缓慢改善所需要的epoch就越少。

# 提升模型准确率的方法

1. 挑选合适的激活函数，并且ReLU的优先级要高于Sigmoid函数。
2. 使用Normalization加速收敛。
3. 选择合适的learning rate，以得到优秀的收敛速度。目前来看，learning rate越大越好，因为越大的learning rate，缓慢改善所需要的epoch就越少。但过大的learning rate会导致模型不能收敛，或在接近收敛时发生振荡。
4. 训练足够长的时间，以确保模型在缓慢收敛阶段继续收敛，以榨取模型的潜力。最好的做法是不设定固定轮数，而是根据对准确率的需求，设定当模型在n的轮改进小于某个值时，才停止训练。
