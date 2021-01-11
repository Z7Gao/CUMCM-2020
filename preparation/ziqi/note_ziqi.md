# Week1

## 线性规划

决策变量、目标函数、约束条件

### Matlab标准形式

$$
min\ z = f^Tx\\
s.t.
\begin{cases}
A\cdot x\leq b\\
Aeq\cdot x = beq\\
lb \leq x \leq ub
\end{cases}
$$

### Matlab命令

linprog

### 1998年A题

#### 符号规定

$i = 0$ 存入银行

$x_i$ 投资项目$s_i$的定金S 

$a$   投资风险度

$Q$  总体收益

#### 基本假设

总体风险用投资项目中最大的一个$s_i$来衡量（题干）

$s_i$ 相互独立

#### 模型建立

1. 总体风险用投资项目中最大的一个$s_i$来衡量

$$
max\{q_ix_i | i = 1,2,...,n\}
$$

2. 交易费是个分段函数

$$
交易费 =
\begin{cases}
p_ix_i,x>u_i,\\
p_iu_i,x\leq ui
\end{cases}
$$

​	而题干中给到的$u_i$相对”相当大“的$M$很小，$p_iu_i$更小，故简化为
$$
交易费 = p_ix_i
$$
​	则净收益为$(r_i-p_i)x_i$.

3. 题干中：“净收益尽可能大，总体风险尽可能小“ --> 多目标规划

   目标函数：

$$
\begin{cases}
max\sum ^n_{i=0}(r_i-p_i)x_i\\
min\{max\{q_ix_i\}| i = 1,2,...,n\}
\end{cases}
$$

​		约束条件：
$$
\begin{cases}
\sum^{n}_{i=0}(1+p_i)x_i= M\\
x_i \geq 0, i = 0,1,...,n
\end{cases}
$$

4. 模型简化

   ① 固定风险水平（最高期望风险率不大于a），极大化收益.

   目标函数：
   $$
   max\sum ^n_{i=0}(r_i-p_i)x_i
   $$
   约束条件 ：
   
   
$$
\begin{cases}
\frac{x_iq_i}{M}\leq  a，i = 0,1,...,n\\
\sum^{n}_{i=0}(1+p_i)x_i= M\\
x_i \geq 0, i = 0,1,...,n
\end{cases}
$$
② 固定盈利水平（期望总盈利水平不大于k），极小化风险.

目标函数：
$$
min\{max\{q_ix_i\}| i = 1,2,...,n\}
$$
约束条件：
$$
   \begin{cases}
   \sum ^n_{i=0}(r_i-p_i)x_i \geq k\\
   \sum^{n}_{i=0}(1+p_i)x_i= M\\
   x_i \geq 0, i = 0,1,...,n\\
   \end{cases}
$$
③ 对风险收益赋予权重$s$, $1-s$, $s(0<s\leq1)$ 称为投资偏好系数.

目标函数：
$$
   min\ [s\{max\{q_ix_i\}\} - (1-s)\sum ^n_{i=0}(r_i-p_i)x_i]
$$
约束条件：
$$
   \begin{cases}
   \sum^{n}_{i=0}(1+p_i)x_i= M\\
   x_i \geq 0, i = 0,1,...,n
   \end{cases}
$$
#### 模型求解

matlab得出最优决策边界

#### 模型分析

灵敏度分析

## 整数规划

### 基本内容

决策变量取值完全/部分为整数；

三种可能：最优解均为整数，不变；整数范围内无可行解；有可行解，最优解值变差；

求解方法：分枝定界法、割平面法；隐枚举法（过滤、分枝）；匈牙利（解决指派问题）；monte carlo。

### 0-1整数规划

决策变量取值只能为0/1。

一般用于将存在各种情况需要讨论的数学规划问题统一在一个问题之中，类似于“指示变量”。

#### 应用场景

1. 不互相独立的决策变量

   例：投资问题（1998A 变体）

   至少两个，只选一个，先修条件……

2. 互相排斥的约束条件

   不是原有决策变量本身只能取0/1，而是引入另一个决策变量，该变量为0-1变量。

   例：船运对应约束条件 $5x_1+4x_2 \leq 20$ ，空运对应约束条件$3x_1+7x_2\leq45$ ，船运空运只能选一样的。

   引入0-1变量  $y  = bool(选船运)$, M充分大。

   约束条件改写为：

$$
\begin{cases}
   5x_1+4x_2 \leq 20 +(1-y)M\\
   3x_1+7x_2\leq45 + yM\\
   y = 0或1
   \end{cases}
$$
   	实际求解中 y = 0或1转化为非线性规划 $y(1-y) = 0$.

​	   可以拓展到n个互相排斥的约束条件的场景，yi。

3. 固定成本问题

   模型：多种选择， 都可以选，每种选择都对应不同的固定成本，但不选就没有。

   例：投资问题（1998A变体）

   每种投资都对应一种固定的手续费$k_i$，不买没有。

   目标函数修改为：

$$
\begin{cases}
   max\sum ^n_{i=0}[(r_i-p_i)x_i+y_ik_i]\\
   min\{max\{q_ix_i\}| i = 1,2,...,n\}
   \end{cases}
$$
   	其中$y_i = bool(x_i>0)$

​	   实际计算中可以转化成等价的式子
$$
y_i\epsilon\leq x_i \leq y_iM
$$
​		$\epsilon$足够小的正常数，M足够大。

​		(等价是因为$x_i>0 => y_i = 1$; $x_i=0 => y_i = 0$)(好像是废话)

4. 指派问题/运输问题

   直接转化为网络流问题就行

### 蒙特卡洛法

用于解决一般的整数规划问题。

整数范围内穷举法 + 蒙特卡洛法随机取部分点 => 高可信度的满意解。【随机算法精确性证明】


matlab随机数生成：unifrnd, rand, randi...

### 2005年B题

word

## 非线性规划

### Matlab标准形式

$$
min\ f(x)\\
s.t.
\begin{cases}
A\cdot x\leq b\\
Aeq\cdot x = beq\\
lb \leq x \leq ub\\
c(x) \leq 0 \\
ceq(x) = 0
\end{cases}
$$

$c(x)\leq0,ceq(x)=0,f(x)$ 是非线性向量函数，matlab命令里要用xxx.m定义

### Matlab命令

fmincon

没有的约束就改成[]，多个约束 e.g.多个非线性等式约束就写在一个数组里



### 无约束极值问题

（单独一大节，但不知道有什么用？？）

#### 符号解

数分题，丢matlab

#### 数值解

fminunc, fminsearch.可以提供多种option例如梯度、二阶导数等，以提高精度和计算速度。

#### 零点和方程组的解

fsolve（数值）, solve（符号）, roots



### 约束极值问题

（同不知道有什么用)

#### 二次规划

##### Matlab标准形式

约束条件是线性，目标函数是二次
$$
min\ z = \frac{1}{2}x^THx+ f^Tx\\
s.t.
\begin{cases}
A\cdot x\leq b\\
Aeq\cdot x = beq\\
lb \leq x \leq ub
\end{cases}
$$
H是二次型里面矩阵形式里那个矩阵再全部乘二

##### Matlab命令

quadprog

#### 罚函数法（SUMT)

 将非线性规划问题转化成无约束极值问题，通过对约束条件进行惩罚（乘充分大实数）来构建一个增广目标函数

#### Matlab求约束极值

对应不同的标准形式，fminbnd（单变量非线性函数区间极小值）、fseminf（多了x以外的其他附加变量）、fminmax（min max F_i(x)）（函数族/绝对值函数族+option=MinAbsMax）、option+梯度提精度

工具箱：optimtool

