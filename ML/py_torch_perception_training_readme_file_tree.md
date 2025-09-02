# PyTorch Perception Training – README

A hands‑on, four‑week program to turn PyTorch skills into **vehicle perception** muscle memory. The **main page** gives a concise roadmap. Each **week has its own detailed page** with exercises, TODOs, and pitfalls.

---

## 🚀 Goals
- 写得出：徒手实现 `Dataset/DataLoader/collate_fn`、训练循环、常见损失/指标。
- 讲得清：能解释模型结构、损失设计、实验消融与指标。
- 跑得动：能在本机/GPU 上复现实验，导出 ONNX/TensorRT。

---

## 📦 Repo 结构（文件树，简略版）
```text
pytorch-perception/
├─ README.md                 # 主页面（简略）
├─ week1_basics.md           # Week1 详细内容
├─ week2_engineering.md      # Week2 详细内容
├─ week3_detection.md        # Week3 详细内容
├─ week4_3d_fusion.md        # Week4 详细内容
├─ configs/ ...              # 配置
├─ datasets/ ...             # 数据集包装
├─ models/ ...               # 模型
├─ engine/ ...               # 训练循环/损失/指标
├─ utils/ ...                # 工具函数
├─ scripts/ ...              # 启动脚本
└─ notebooks/ ...            # 练习 Notebook
```

---

## 🗓️ 四周训练路线图（概要）

### [Week 1｜PyTorch 基础 + 训练循环](week1_basics.md)
- 张量操作：矩阵乘法/加法/广播/索引
- Autograd 基础：梯度计算、反向传播
- 最小训练循环：线性回归、MNIST softmax 分类

### [Week 2｜工程化 & 可复现 & DDP 性能](week2_engineering.md)
- 配置化（YAML + CLI 覆盖）
- 断点续训、随机种子固定
- DDP 单机多卡、性能调优

### [Week 3｜2D 检测小项目 + 自定义损失/指标](week3_detection.md)
- 实现轻量检测基线（COCO 子集）
- 自定义 Focal Loss / Smooth L1 / IoU
- 可视化误检/漏检，绘制 PR 曲线

### [Week 4｜单目 3D / Radar-Camera 融合](week4_3d_fusion.md)
- 任务 A：单目 3D 检测 / 深度估计（KITTI-mini）
- 任务 B：Radar ↔ Camera 融合 Demo（mid/BEV 融合层）
- 消融实验：camera-only vs +radar

---

## 📊 结果记录（简略）
| 周次 | 任务 | 指标 | 结果 |
|---|---|---|---|
| Week1 | 线性回归 / Softmax MNIST | MSE / Top1 | >90% / 收敛 |
| Week2 | CIFAR10 分类 | Top1 | ~87% |
| Week3 | COCO-small 检测 | mAP@0.5 | ~0.4 |
| Week4 | Mono3D / 融合 | BEV IoU / NDS | 提升 +X% |

---

👉 每周的详细练习、代码片段和常见坑位，请点击对应的 **独立页面**。

