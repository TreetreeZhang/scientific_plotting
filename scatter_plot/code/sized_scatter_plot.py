#!/usr/bin/env python3
"""
Sized Scatter Plot
==================

Creates a bubble chart with size-coded third variable.

Author: Scientific Plotting Team
"""

import sys
import os
sys.path.append('../../utils')

from common_utils import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_sized_scatter_plot():
    """创建大小变化散点图"""
    print("\n3. Sized Scatter Plot")
    
    csv_path = "../data/sized_scatter_data.csv"
    required_columns = ['x', 'y', 'size_value']
    data_description = """
大小变化散点图数据格式:
- x: X轴数值 (数值型)
- y: Y轴数值 (数值型)
- size_value: 用于大小映射的第三变量 (数值型)

数据示例:
x,y,size_value
1.2,2.4,50
2.1,4.3,120
3.5,6.8,80
4.2,8.1,200
...

用途: 同时展示三个变量的关系，第三变量通过点的大小表示
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(1)
        
        # 标准化大小值
        sizes = (df['size_value'] - df['size_value'].min()) / (df['size_value'].max() - df['size_value'].min()) * 200 + 20
        
        # 绘制大小变化散点图
        ax.scatter(df['x'], df['y'], s=sizes, color=colors[0], alpha=0.6, edgecolors='black', linewidth=0.5)
        
        # 添加大小图例
        legend_sizes = [df['size_value'].min(), df['size_value'].mean(), df['size_value'].max()]
        legend_labels = [f'{size:.1f}' for size in legend_sizes]
        legend_points = []
        
        for size in legend_sizes:
            norm_size = (size - df['size_value'].min()) / (df['size_value'].max() - df['size_value'].min()) * 200 + 20
            legend_points.append(plt.scatter([], [], s=norm_size, color=colors[0], alpha=0.6, edgecolors='black'))
        
        ax.legend(legend_points, legend_labels, title='Size Value', loc='upper left')
        
        ax.set_xlabel('X Variable')
        ax.set_ylabel('Y Variable')
        ax.set_title('Sized Scatter Plot (Bubble Chart)')
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/sized_scatter_plot.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建大小变化散点图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_sized_scatter_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
