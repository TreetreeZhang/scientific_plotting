#!/usr/bin/env python3
"""
Grouped Bar Chart
=================

Creates a grouped bar chart to compare multiple groups across categories.

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

def create_grouped_bar_chart():
    """创建分组柱状图"""
    print("\n2. Grouped Bar Chart")
    
    csv_path = "../data/grouped_bar_data.csv"
    required_columns = ['category', 'group_a', 'group_b', 'group_c']
    data_description = """
分组柱状图数据格式:
- category: 分类名称 (字符串型)
- group_a: 第一组数值 (数值型)
- group_b: 第二组数值 (数值型)
- group_c: 第三组数值 (数值型)

数据示例:
category,group_a,group_b,group_c
Q1,85,72,91
Q2,78,85,68
Q3,92,79,85
Q4,88,91,77
...

用途: 比较多个组在不同类别下的表现
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style(figsize=(12, 6))
        colors = get_color_palette(3)
        
        # 设置柱子位置
        x = np.arange(len(df['category']))
        width = 0.25
        
        # 绘制分组柱状图
        ax.bar(x - width, df['group_a'], width, label='Group A', color=colors[0], alpha=0.8)
        ax.bar(x, df['group_b'], width, label='Group B', color=colors[1], alpha=0.8)
        ax.bar(x + width, df['group_c'], width, label='Group C', color=colors[2], alpha=0.8)
        
        ax.set_xlabel('Category')
        ax.set_ylabel('Value')
        ax.set_title('Grouped Bar Chart')
        ax.set_xticks(x)
        ax.set_xticklabels(df['category'])
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        
        # 保存图片
        save_plot(fig, "../plot/grouped_bar_chart.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建分组柱状图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_grouped_bar_chart()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
