#!/usr/bin/env python3
"""
Categorical Scatter Plot
========================

Creates a scatter plot with categorical grouping.

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

def create_categorical_scatter_plot():
    """创建分类散点图"""
    print("\n4. Categorical Scatter Plot")
    
    csv_path = "../data/categorical_scatter_data.csv"
    required_columns = ['x', 'y', 'category']
    data_description = """
分类散点图数据格式:
- x: X轴数值 (数值型)
- y: Y轴数值 (数值型)
- category: 分类标签 (字符串型)

数据示例:
x,y,category
1.2,2.4,Group A
2.1,4.3,Group B
3.5,6.8,Group A
4.2,8.1,Group C
...

用途: 按类别展示数据点的分布，不同类别用不同颜色表示
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        
        # 获取唯一类别
        categories = df['category'].unique()
        colors = get_color_palette(len(categories))
        
        # 为每个类别绘制散点
        for i, category in enumerate(categories):
            mask = df['category'] == category
            ax.scatter(df[mask]['x'], df[mask]['y'], 
                      color=colors[i], label=category, alpha=0.7, s=60)
        
        ax.set_xlabel('X Variable')
        ax.set_ylabel('Y Variable')
        ax.set_title('Categorical Scatter Plot')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/categorical_scatter_plot.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建分类散点图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_categorical_scatter_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
