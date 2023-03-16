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
