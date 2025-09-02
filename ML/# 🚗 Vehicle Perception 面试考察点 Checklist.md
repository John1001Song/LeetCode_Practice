# 🚗 Vehicle Perception 面试考察点 Checklist

## 1. Coding 基础
- **语言**
  - Python（数据处理、模型实现）
  - C++（实时系统、ROS、优化）
- **框架**
  - PyTorch（核心建模）
  - TensorRT（部署优化）
- **考察方式**
  - LeetCode风格 coding 题（数组/链表/二分/动态规划）
  - 写一个数据预处理 pipeline（点云读取 → 投影 → 归一化）

---

## 2. Data Processing & Sensors
- **传感器数据特点**
  - Radar: 稀疏点云, Range-Doppler map, micro-Doppler
  - LiDAR: 稠密点云, intensity channel, BEV投影
  - Camera: 2D图像, 光照/遮挡问题, depth估计
- **多传感器处理**
  - extrinsic & intrinsic calibration
  - 时间同步（event-trigger, GPS/IMU）
- **考察方式**
  - 给一段 nuScenes/KITTI 数据，问如何对齐 radar+camera
  - 写一个数据增强方法（随机旋转点云 + 投影到图像）

---

## 3. Model Architecture
- **点云模型**：PointNet/++, VoxelNet, Point Transformer
- **图像模型**：ResNet, ViT, CNN-Transformer hybrid
- **Fusion 模型**：BEVFusion, TransFusion, DeepFusion
- **任务**
  - 3D object detection
  - semantic/instance segmentation
  - tracking & motion forecasting
  - occupancy prediction
- **考察方式**
  - 解释 PointNet 如何处理 permutation-invariant
  - BEVFusion 为什么比 early fusion 稳定？

---

## 4. Evaluation & Analysis
- **指标**
  - Detection: mAP, IoU, nuScenes Detection Score (NDS)
  - Tracking: MOTA, MOTP
  - Segmentation: mIoU
- **分析能力**
  - Ablation study：如果 radar branch 去掉会怎样？
  - Failure case：模型在夜间/雨天失效的原因？
- **考察方式**
  - 给一组结果，问你怎么分析为什么车检测失败
  - 如何比较两个模型的性能差异（速度 vs 精度）

---

## 5. System & Deployment
- **工具链**：ROS, Docker, Open3D, OpenCV
- **优化**：TensorRT, ONNX, CUDA kernel
- **平台**：NVIDIA Jetson, Thor, Orin
- **考察方式**
  - 如何让模型从 10 FPS 提升到 30 FPS？
  - 解释 real-time perception 的瓶颈

---

## 6. 加分项
- **研究经历**：发表过 radar/lidar/camera 相关论文
- **工程经验**：参与过自动驾驶/机器人项目
- **创新点**：自己设计过 fusion 模块 / attention 机制
- **考察方式**
  - 介绍一个你自己做的 project
  - 说说你如何把研究成果应用到工业系统
