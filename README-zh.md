* MNIST-FCN-0: 0个隐藏层的全连接网络。
* MNIST-FCN-1: 1个隐藏层的全连接网络。
    * MNIST-FCN-1-activation: 在1个隐藏层的全连接网络上测试激活函数。
    * MNIST-FCN-1-normalization: 在1个隐藏层的全连接网络上测试归一化。
    * MNIST-FCN-1-learning-rates: 在1个隐藏层的全连接网络上测试learning rate。
* MNIST-FCN-2: 2个隐藏层的全连接网络。
    * MNIST-FCN-2-activation: 在2个隐藏层的全连接网络上测试激活函数。

# Learning Rates

从MNIST-FCN-1-learning-rates的实验可以得出以下结论：
1. learning rate的合理的取值不止是0.001、0.01这种数量级，还可以是1、10这种数量级。
2. learning rate对收敛速度有很大的影响。
3. 在固定优化轮数时，learning rate对训练效果有很大影响。

# 提升模型准确率的方法

1. 选择合适的learning rate，以得到优秀的收敛速度。
2. 训练足够长的时间，以确保模型在缓慢收敛阶段继续收敛，以榨取模型的潜力。最好的做法是不设定固定轮数，而是设定当模型在n的轮改进小于某个值时，才停止训练。
