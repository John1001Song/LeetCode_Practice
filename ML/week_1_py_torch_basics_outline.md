# Week 1 – PyTorch Basics (Outline)

> 目标：**徒手写 PyTorch**。从张量 → 形状/广播 → 矩阵运算 → Autograd → 最小训练循环。完成后，你能不用现成模板，独立写出一个小模型并训练收敛。

---

## ✅ 学习产出（本周结束必须完成）
- 一份 `00_pytorch_basics.ipynb`（或 `.py`）包含：
  - 张量创建/设备/类型/形状变换/广播/索引/矩阵运算/`einsum` 的最小例子
  - Autograd 最小示例（手推梯度 vs PyTorch 梯度）
- 一个 **50 行级最小训练循环**（线性回归或 softmax 分类），loss 正常下降
- 三个 **自写函数**：`softmax_from_logits`、`nll_loss`、`cross_entropy_from_logits`
- 单元测试：形状一致性 + 数值一致性（误差 < 1e-6）

---

## 🧱 先决条件
- 安装：PyTorch（GPU 可选）、numpy、matplotlib、pytest、tensorboard
- `torch.cuda.is_available()` 为 True（如使用 GPU）

---

## 📅 建议进度（4 天）
- **D1**：张量 & 形状 & 广播 & 基本运算
- **D2**：矩阵运算（mm/matmul/bmm）& `einsum` & 索引/gather/scatter
- **D3**：Autograd & 数值稳定 & 手写 softmax / cross-entropy
- **D4**：50 行级最小训练循环（线性回归 → softmax MNIST）

> 备注：每天预留 15 分钟写“踩坑日志”。

---

## D1｜Tensor / Shape / Broadcasting

### 任务 A：张量与设备
**要求**：写 10 行以内的函数 `make_tensor(shape, dtype, device)`，创建全 1 张量并返回其 `shape/dtype/device`。
- 覆盖：`torch.tensor/zeros/ones/arange/linspace`，`to(device)`
- 练习：在 CPU/GPU 间移动；比较 `float32/float64` 对运算的影响

### 任务 B：形状操作
实现并测试以下片段（每个 3–5 行）：
- `view/reshape/permute` 与 `contiguous()` 的差异
- `unsqueeze/squeeze`、`expand/repeat` 的差异
- 写一个 `flatten_hw(x)`：把 `[B, C, H, W] → [B, C, HW]`

### 任务 C：广播规则
- 给 `x:[B,1,H,W]` 与 `y:[1,C,1,1]`，写出 `x+y` 的结果形状，
- 用 `keepdim=True` 重现按通道归一化：`(x - x.mean(dim=(0,2,3), keepdim=True)) / (x.std(...)+eps)`

**自检清单**
- [ ] 能描述广播三原则（尾维对齐、1 可扩展、维数不一致可左侧补 1）
- [ ] 知道什么时候需要 `contiguous()` 再 `view`

---

## D2｜矩阵运算 / einsum / 索引

### 任务 D：矩阵乘法三种写法
- 生成 `x:[B,I]`、`W:[I,O]`，用以下三种等价方式计算 `y:[B,O]`：
  1) `y = x @ W`
  2) `y = torch.matmul(x, W)`
  3) `y = torch.einsum('bi,io->bo', x, W)`
- 用 `torch.allclose` 验证三者一致，打印最大误差。

### 任务 E：批量矩阵乘（bmm）
- 生成 `A:[B,M,K]`、`B:[B,K,N]`，比较 `torch.bmm(A,B)` 与 `einsum('bmk,bkn->bmn',A,B)`。

### 任务 F：高级索引 / gather / scatter_
- 写 `index_select_topk(logits, k)`：返回每行 top‑k 的 **值** 和 **列索引**（不用 `torch.topk`，改用 `argsort` + 切片）。
- 写 `one_hot(indices, num_classes)`（**不用** `torch.nn.functional.one_hot`）。
- 用 `scatter_` 将 one‑hot 写入到 `[B, num_classes]` 张量。

**自检清单**
- [ ] `mm/matmul/@/bmm/einsum` 的使用场景与形状规则
- [ ] 能写出不依赖 `topk/one_hot` 的等价实现

---

## D3｜Autograd / 数值稳定 / 手写 CE

### 任务 G：Autograd 最小例子
- 构造 `y = (Wx + b)^2`，其中 `W:[O,I]`、`x:[I]`、`b:[O]`，
- 用 `autograd.grad` 计算 `dy/dW, dy/db, dy/dx`，并与 **手推公式** 对比。

### 任务 H：数值稳定 Softmax & CE（手写）
- 实现
  - `logsumexp(x, dim)`: 通过 `x - x.max(keepdim=True)` 实现
  - `softmax_from_logits(logits, dim=-1)`（先减最大值）
  - `nll_loss(log_probs, target_idx)`（负对数似然）
  - `cross_entropy_from_logits(logits, target_idx)` = `-log_softmax[range(B), target]` 的平均
- 与官方实现对齐：
  - 随机 `logits`/`targets`，比较 `F.cross_entropy` 与自写函数的误差

### 任务 I：就地操作与梯度
- 举例 `relu_()` 与 `relu()` 的差别；展示一个因为就地操作导致 `RuntimeError` 的最小复现，并改正。

**自检清单**
- [ ] 解释 **为什么** CE 不能先 `softmax` 再 `log`（数值稳定）
- [ ] 了解 `requires_grad/with torch.no_grad()` 的边界

---

## D4｜50 行级最小训练循环

### 任务 J：线性回归（合成数据）
- 数据：随机生成 `x:[N,2]`，`y = x @ W* + b* + noise`
- 模型：`W:[2,1]`、`b:[1]`，初始化为 0
- 损失：MSE；优化器：SGD（手写参数更新或 `torch.optim.SGD` 均可）
- 要求：loss 单调下降，收敛后 `W ≈ W*`，`b ≈ b*`

### 任务 K：Softmax MNIST（Logistic Regression）
- 模型：`nn.Linear(28*28, 10)`（或手写权重矩阵），**不要**使用 CNN
- 损失：你手写的 `cross_entropy_from_logits`
- 训练：5 个 epoch，测试集 Top1 ≥ 90%
- 记录：`TensorBoard`/`matplotlib` 绘制 loss/acc 曲线

**自检清单**
- [ ] 解释 batch 化训练与 `DataLoader` 的作用
- [ ] 会做 `grad_clip` / `amp.autocast`（可作为加分项）

---

## 🧪 单元测试（最低配）
- `test_shapes_ops.py`：
  - `einsum`/`matmul` 一致性（误差 < 1e‑6）
  - `one_hot/scatter_` 输出形状与取值合法（0/1）
- `test_losses.py`：
  - `cross_entropy_from_logits` 与 `F.cross_entropy` 数值对齐

---

## 🧭 调试与排错清单
- 形状错：在关键张量后面加 `print(name, x.shape)`；使用 `assert x.dim()==...`
- 梯度为 `None`：检查参数是否在计算图中；是否 `no_grad()`；是否被就地覆盖
- Loss 不降：先用 **小数据** 或 **单个 batch 过拟合** 验证实现是否正确
- NaN：降低学习率；CE 中不要对 `softmax` 再 `log`；使用 `clamp` 防止 `log(0)`

---

## 🎯 过关标准（Rubric）
- **合格**：完成 D1–D4 所有打卡任务；MNIST ≥ 90%；三个自写函数与官方对齐
- **良好**：补充 AMP/Grad Clip；写出 `bmm` + `einsum` 的小对比基准
- **优秀**：写一版 **只用你自写 CE** 的最小多分类器并导出 ONNX；在 README 记录实验

---

## 📌 建议提交物与路径
- `notebooks/00_pytorch_basics.ipynb`：整合 D1–D3 的最小可运行单元
- `engine/miniloop.py`：D4 50 行训练循环
- `scripts/train_linear.sh`、`scripts/train_softmax_mnist.sh`
- `tests/test_shapes_ops.py`、`tests/test_losses.py`
- 在主仓库 README 的 Week1 章节贴上：曲线截图 + 指标表 + 踩坑总结

