# 科学绘图数据格式指南

本文档详细说明了科学绘图套件中每种图表类型所需的CSV数据格式。

## 📋 总体要求

- 所有数据文件必须是CSV格式
- 第一行必须包含列名（表头）
- 数值型数据不能包含非数字字符
- 字符串型数据可以包含中文和英文
- 缺失值请用空白或"NaN"表示

## 📊 图表类型和数据格式

### 1. 线图 (Line Charts)

#### 1.1 基础折线图
**文件路径**: `line_chart/data/basic_line_data.csv`

**必需列名**: `time`, `amplitude`

**数据格式**:
```csv
time,amplitude
0.0,0.05
0.2,0.19
0.4,0.46
0.6,0.73
0.8,0.95
```

**说明**:
- `time`: 时间序列数据 (数值型)
- `amplitude`: 对应的幅度值 (数值型)
- 用途: 展示单一变量随时间的变化趋势

#### 1.2 多系列折线图
**文件路径**: `line_chart/data/multiple_line_data.csv`

**必需列名**: `time`, `series_a`, `series_b`, `series_c`

**数据格式**:
```csv
time,series_a,series_b,series_c
0.0,0.05,0.95,0.02
0.2,0.19,0.81,0.09
0.4,0.46,0.54,0.23
0.6,0.73,0.27,0.36
```

**说明**:
- `time`: 时间序列数据 (数值型)
- `series_a`, `series_b`, `series_c`: 三个数据系列 (数值型)
- 用途: 比较多个变量随时间的变化趋势

#### 1.3 带置信区间的折线图
**文件路径**: `line_chart/data/confidence_interval_data.csv`

**必需列名**: `time`, `mean`, `lower_ci`, `upper_ci`

**数据格式**:
```csv
time,mean,lower_ci,upper_ci
0.0,0.05,-0.15,0.25
0.2,0.19,-0.01,0.39
0.4,0.46,0.26,0.66
0.6,0.73,0.53,0.93
```

**说明**:
- `time`: 时间序列数据 (数值型)
- `mean`: 平均值 (数值型)
- `lower_ci`: 置信区间下界 (数值型)
- `upper_ci`: 置信区间上界 (数值型)
- 用途: 展示数据的不确定性和置信区间

### 2. 柱状图 (Bar Charts)

#### 2.1 基础柱状图
**文件路径**: `bar_chart/data/basic_bar_data.csv`

**必需列名**: `category`, `value`

**数据格式**:
```csv
category,value
Method A,85
Method B,72
Method C,91
Method D,68
Method E,79
```

**说明**:
- `category`: 分类名称 (字符串型)
- `value`: 对应的数值 (数值型)
- 用途: 比较不同类别的数值大小

#### 2.2 分组柱状图
**文件路径**: `bar_chart/data/grouped_bar_data.csv`

**必需列名**: `category`, `group_a`, `group_b`, `group_c`

**数据格式**:
```csv
category,group_a,group_b,group_c
Q1,85,72,91
Q2,78,85,68
Q3,92,79,85
Q4,88,91,77
```

**说明**:
- `category`: 分类名称 (字符串型)
- `group_a`, `group_b`, `group_c`: 三个组的数值 (数值型)
- 用途: 比较多个组在不同类别下的表现

#### 2.3 堆叠柱状图
**文件路径**: `bar_chart/data/stacked_bar_data.csv`

**必需列名**: `category`, `part_a`, `part_b`, `part_c`

**数据格式**:
```csv
category,part_a,part_b,part_c
Product A,30,25,20
Product B,35,30,15
Product C,25,35,25
Product D,40,20,25
```

**说明**:
- `category`: 分类名称 (字符串型)
- `part_a`, `part_b`, `part_c`: 各部分的数值 (数值型)
- 用途: 展示整体中各部分的构成比例

#### 2.4 水平柱状图
**文件路径**: `bar_chart/data/horizontal_bar_data.csv`

**必需列名**: `item`, `score`

**数据格式**:
```csv
item,score
Algorithm A,92
Algorithm B,85
Algorithm C,78
Algorithm D,88
Algorithm E,91
```

**说明**:
- `item`: 项目名称 (字符串型)
- `score`: 对应的分数 (数值型)
- 用途: 当类别名称较长时，水平显示更清晰

### 3. 散点图 (Scatter Plots)

#### 3.1 基础散点图
**文件路径**: `scatter_plot/data/basic_scatter_data.csv`

**必需列名**: `x`, `y`

**数据格式**:
```csv
x,y
1.2,2.4
2.1,4.3
3.5,6.8
4.2,8.1
5.0,9.9
```

**说明**:
- `x`: X轴数值 (数值型)
- `y`: Y轴数值 (数值型)
- 用途: 展示两个变量之间的关系和相关性

#### 3.2 彩色散点图
**文件路径**: `scatter_plot/data/colored_scatter_data.csv`

**必需列名**: `x`, `y`, `color_value`

**数据格式**:
```csv
x,y,color_value
1.2,2.4,10.5
2.1,4.3,15.2
3.5,6.8,8.7
4.2,8.1,20.1
```

**说明**:
- `x`: X轴数值 (数值型)
- `y`: Y轴数值 (数值型)
- `color_value`: 用于颜色映射的第三变量 (数值型)
- 用途: 同时展示三个变量的关系，第三变量通过颜色表示

#### 3.3 大小变化散点图
**文件路径**: `scatter_plot/data/sized_scatter_data.csv`

**必需列名**: `x`, `y`, `size_value`

**数据格式**:
```csv
x,y,size_value
1.2,2.4,50
2.1,4.3,120
3.5,6.8,80
4.2,8.1,200
```

**说明**:
- `x`: X轴数值 (数值型)
- `y`: Y轴数值 (数值型)
- `size_value`: 用于大小映射的第三变量 (数值型)
- 用途: 同时展示三个变量的关系，第三变量通过点的大小表示

#### 3.4 分类散点图
**文件路径**: `scatter_plot/data/categorical_scatter_data.csv`

**必需列名**: `x`, `y`, `category`

**数据格式**:
```csv
x,y,category
1.2,2.4,Group A
2.1,4.3,Group B
3.5,6.8,Group A
4.2,8.1,Group C
```

**说明**:
- `x`: X轴数值 (数值型)
- `y`: Y轴数值 (数值型)
- `category`: 分类标签 (字符串型)
- 用途: 按类别展示数据点的分布，不同类别用不同颜色表示

#### 3.5 相关性矩阵散点图
**文件路径**: `scatter_plot/data/correlation_matrix_data.csv`

**必需列名**: `var1`, `var2`, `var3`, `var4`

**数据格式**:
```csv
var1,var2,var3,var4
1.2,2.4,3.1,4.5
2.1,4.3,2.8,3.9
3.5,6.8,4.2,5.1
4.2,8.1,3.7,4.8
```

**说明**:
- `var1`, `var2`, `var3`, `var4`: 四个变量 (数值型)
- 用途: 展示多个变量之间的两两相关关系

### 4. 箱线图 (Box Plots)

#### 4.1 基础箱线图
**文件路径**: `box_plot/data/basic_box_data.csv`

**必需列名**: `group`, `value`

**数据格式**:
```csv
group,value
Group A,23.5
Group A,25.1
Group A,22.8
Group B,28.3
Group B,30.1
Group B,27.9
Group C,31.2
Group C,33.5
Group C,29.8
```

**说明**:
- `group`: 分组名称 (字符串型)
- `value`: 数值 (数值型)
- 用途: 比较不同组的数据分布
- 注意: 每个组需要多个数据点

#### 4.2 小提琴图
**文件路径**: `box_plot/data/violin_plot_data.csv`

**必需列名**: `category`, `measurement`

**数据格式**:
```csv
category,measurement
Type A,15.2
Type A,16.8
Type A,14.9
Type B,18.5
Type B,19.2
Type B,17.8
```

**说明**:
- `category`: 类别名称 (字符串型)
- `measurement`: 测量值 (数值型)
- 用途: 展示数据的密度分布

#### 4.3 分组箱线图
**文件路径**: `box_plot/data/grouped_box_data.csv`

**必需列名**: `time_point`, `condition`, `response`

**数据格式**:
```csv
time_point,condition,response
T1,Control,12.5
T1,Control,13.2
T1,Treatment,15.8
T1,Treatment,16.1
T2,Control,14.2
T2,Treatment,18.5
```

**说明**:
- `time_point`: 时间点 (字符串型)
- `condition`: 实验条件 (字符串型)
- `response`: 响应值 (数值型)
- 用途: 多因子分析

#### 4.4 带缺口的箱线图
**文件路径**: `box_plot/data/notched_box_data.csv`

**必需列名**: `method`, `performance`

**数据格式**:
```csv
method,performance
Method 1,85.2
Method 1,87.1
Method 1,84.5
Method 2,78.9
Method 2,80.3
Method 2,77.8
```

**说明**:
- `method`: 方法名称 (字符串型)
- `performance`: 性能指标 (数值型)
- 用途: 统计显著性比较

#### 4.5 水平箱线图
**文件路径**: `box_plot/data/horizontal_box_data.csv`

**必需列名**: `algorithm`, `execution_time`

**数据格式**:
```csv
algorithm,execution_time
Algorithm A,0.25
Algorithm A,0.28
Algorithm A,0.23
Algorithm B,0.45
Algorithm B,0.48
Algorithm B,0.42
```

**说明**:
- `algorithm`: 算法名称 (字符串型)
- `execution_time`: 执行时间 (数值型)
- 用途: 算法性能比较

### 5. 直方图 (Histograms)

#### 5.1 基础直方图
**文件路径**: `histogram/data/basic_histogram_data.csv`

**必需列名**: `values`

**数据格式**:
```csv
values
23.5
25.1
22.8
28.3
30.1
27.9
31.2
```

**说明**:
- `values`: 数值数据 (数值型)
- 用途: 展示单一变量的分布

#### 5.2 多重直方图
**文件路径**: `histogram/data/multiple_histogram_data.csv`

**必需列名**: `group_a`, `group_b`, `group_c`

**数据格式**:
```csv
group_a,group_b,group_c
23.5,28.3,31.2
25.1,30.1,33.5
22.8,27.9,29.8
24.2,29.5,32.1
```

**说明**:
- `group_a`, `group_b`, `group_c`: 三组数据 (数值型)
- 用途: 比较多个组的分布
- 注意: 可以有不同的行数，空值用NaN表示

#### 5.3 堆叠直方图
**文件路径**: `histogram/data/stacked_histogram_data.csv`

**必需列名**: `value`, `category`

**数据格式**:
```csv
value,category
23.5,Type A
25.1,Type A
28.3,Type B
30.1,Type B
31.2,Type C
33.5,Type C
```

**说明**:
- `value`: 数值 (数值型)
- `category`: 类别 (字符串型)
- 用途: 展示分类数据的分布

#### 5.4 二维直方图
**文件路径**: `histogram/data/2d_histogram_data.csv`

**必需列名**: `x`, `y`

**数据格式**:
```csv
x,y
1.2,2.4
2.1,4.3
3.5,6.8
4.2,8.1
5.0,9.9
```

**说明**:
- `x`: X轴数值 (数值型)
- `y`: Y轴数值 (数值型)
- 用途: 展示二维数据的密度分布

#### 5.5 分布比较直方图
**文件路径**: `histogram/data/distribution_comparison_data.csv`

**必需列名**: `observed`, `theoretical`

**数据格式**:
```csv
observed,theoretical
23.5,24.1
25.1,25.8
22.8,23.2
28.3,28.9
30.1,29.7
```

**说明**:
- `observed`: 观测值 (数值型)
- `theoretical`: 理论值 (数值型)
- 用途: 比较观测分布与理论分布

### 6. 三维图 (3D Plots)

#### 6.1 三维表面图
**文件路径**: `3d_plot/data/3d_surface_data.csv`

**必需列名**: `x`, `y`, `z`

**数据格式**:
```csv
x,y,z
0.0,0.0,0.5
0.1,0.0,0.6
0.0,0.1,0.7
0.1,0.1,0.8
0.2,0.0,0.4
```

**说明**:
- `x`: X坐标 (数值型)
- `y`: Y坐标 (数值型)
- `z`: Z坐标/高度值 (数值型)
- 用途: 展示三维函数关系

#### 6.2 三维散点图
**文件路径**: `3d_plot/data/3d_scatter_data.csv`

**必需列名**: `x`, `y`, `z`, `group`

**数据格式**:
```csv
x,y,z,group
1.2,2.4,3.1,Group A
2.1,4.3,2.8,Group B
3.5,6.8,4.2,Group A
4.2,8.1,3.7,Group C
```

**说明**:
- `x`, `y`, `z`: 三维坐标 (数值型)
- `group`: 分组标签 (字符串型)
- 用途: 三维空间中的点分布

#### 6.3 三维线框图
**文件路径**: `3d_plot/data/3d_wireframe_data.csv`

**必需列名**: `x`, `y`, `z`

**数据格式**:
```csv
x,y,z
0.0,0.0,0.5
0.1,0.0,0.6
0.2,0.0,0.4
0.0,0.1,0.7
0.1,0.1,0.8
```

**说明**:
- `x`: X坐标 (数值型)
- `y`: Y坐标 (数值型)
- `z`: Z坐标 (数值型)
- 用途: 三维网格结构展示

#### 6.4 三维柱状图
**文件路径**: `3d_plot/data/3d_bar_data.csv`

**必需列名**: `x_pos`, `y_pos`, `height`

**数据格式**:
```csv
x_pos,y_pos,height
0,0,5.2
1,0,7.8
2,0,3.4
0,1,6.1
1,1,8.9
2,1,4.7
```

**说明**:
- `x_pos`: X位置 (整数型)
- `y_pos`: Y位置 (整数型)
- `height`: 柱子高度 (数值型)
- 用途: 三维分类数据展示

#### 6.5 三维等高线图
**文件路径**: `3d_plot/data/3d_contour_data.csv`

**必需列名**: `x`, `y`, `z`

**数据格式**:
```csv
x,y,z
0.0,0.0,0.5
0.1,0.0,0.6
0.2,0.0,0.4
0.0,0.1,0.7
0.1,0.1,0.8
```

**说明**:
- `x`: X坐标 (数值型)
- `y`: Y坐标 (数值型)
- `z`: Z值/等高线值 (数值型)
- 用途: 等高线和三维表面结合展示

#### 6.6 参数化三维图
**文件路径**: `3d_plot/data/parametric_3d_data.csv`

**必需列名**: `t`, `x`, `y`, `z`, `curve_type`

**数据格式**:
```csv
t,x,y,z,curve_type
0.0,1.0,0.0,0.0,helix
0.1,0.95,0.31,0.1,helix
0.2,0.81,0.59,0.2,helix
0.0,1.0,0.0,0.0,spiral
0.1,0.90,0.28,0.0,spiral
```

**说明**:
- `t`: 参数值 (数值型)
- `x`, `y`, `z`: 三维坐标 (数值型)
- `curve_type`: 曲线类型 (字符串型)
- 用途: 参数化曲线和螺旋线

## 🔧 数据准备建议

1. **数据清洗**: 确保数值列不包含文本，文本列格式一致
2. **缺失值处理**: 用NaN或空白表示缺失值
3. **数据范围**: 确保数值在合理范围内
4. **编码格式**: 使用UTF-8编码保存CSV文件
5. **列名规范**: 使用英文列名，避免特殊字符

## ❗ 常见错误

1. **列名不匹配**: 确保CSV文件包含所有必需的列名
2. **数据类型错误**: 数值列包含非数字字符
3. **文件路径错误**: 确保CSV文件在正确的路径下
4. **编码问题**: 使用UTF-8编码保存文件
5. **空文件**: CSV文件不能为空，至少要有表头

## 💡 使用提示

- 如果CSV文件不存在，程序会显示详细的错误信息和数据格式要求
- 可以参考现有的数据文件作为模板
- 建议先用小数据集测试，确认格式正确后再使用完整数据
- 每种图表类型都有对应的示例数据文件可供参考 