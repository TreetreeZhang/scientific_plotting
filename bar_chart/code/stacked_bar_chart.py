#!/usr/bin/env python3
"""
Stacked Bar Chart
=================

Creates a stacked bar chart to show composition of categories.

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

def create_stacked_bar_chart():
    """创建堆叠柱状图"""
    print("\n3. Stacked Bar Chart")
    
    csv_path = "../data/stacked_bar_data.csv"
    required_columns = ['category', 'part_a', 'part_b', 'part_c']
    data_description = """
堆叠柱状图数据格式:
- category: 分类名称 (字符串型)
- part_a: 第一部分数值 (数值型)
- part_b: 第二部分数值 (数值型)
- part_c: 第三部分数值 (数值型)

数据示例:
category,part_a,part_b,part_c
Product A,30,25,20
Product B,35,30,15
Product C,25,35,25
Product D,40,20,25
...

用途: 展示整体中各部分的构成比例
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(3)
        
        # 绘制堆叠柱状图
        ax.bar(df['category'], df['part_a'], label='Part A', color=colors[0], alpha=0.8)
        ax.bar(df['category'], df['part_b'], bottom=df['part_a'], 
               label='Part B', color=colors[1], alpha=0.8)
        ax.bar(df['category'], df['part_c'], 
               bottom=df['part_a'] + df['part_b'], 
               label='Part C', color=colors[2], alpha=0.8)
        
        ax.set_xlabel('Category')
        ax.set_ylabel('Value')
        ax.set_title('Stacked Bar Chart')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        
        # 保存图片
        save_plot(fig, "../plot/stacked_bar_chart.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建堆叠柱状图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_stacked_bar_chart()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
