# BUG处理及安装总结

1. Tensorflow GPU 环境配置
- [Win10 安装Tensorflow GPU](https://zhuanlan.zhihu.com/p/37086409)
- [Win10 X64安装CUDA后使用nvcc -V报错](https://bbs.csdn.net/topics/392479444)
- n个小时失败的尝试后妥协，用conda了。注意版本匹配 9.0 CUDA + 7.3.0 CUDNN没毛病

2. XGBoost Softmax 与 Softprob 结果不一致
- XGBoost input label是整数值，不能是one-hot， 即使softprob的output是one-hot。

3. [虚拟机ping不通主机，但是主机可以ping通虚拟机](https://blog.csdn.net/qq_22073849/article/details/54938949)
- 防火墙高级设置ICMPv4-in 设置成ENABLE
