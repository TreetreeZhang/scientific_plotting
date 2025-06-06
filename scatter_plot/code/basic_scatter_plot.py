#!/usr/bin/env python3
"""
Basic Scatter Plot
==================

Creates a basic scatter plot for correlation analysis.

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

def create_basic_scatter_plot():
    """创建基础散点图"""
    print("\n1. Basic Scatter Plot")
    
    csv_path = "../data/basic_scatter_data.csv"
    required_columns = ['x', 'y']
    data_description = """
基础散点图数据格式:
- x: X轴数值 (数值型)
- y: Y轴数值 (数值型)

数据示例:
x,y
1.2,2.4
2.1,4.3
3.5,6.8
4.2,8.1
...

用途: 展示两个变量之间的关系和相关性
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(1)
        
        # 绘制散点图
        ax.scatter(df['x'], df['y'], color=colors[0], alpha=0.7, s=50)
        
        # 添加趋势线
        z = np.polyfit(df['x'], df['y'], 1)
        p = np.poly1d(z)
        ax.plot(df['x'], p(df['x']), "r--", alpha=0.8, linewidth=2, label=f'Trend line')
        
        # 计算相关系数
        correlation = np.corrcoef(df['x'], df['y'])[0, 1]
        ax.text(0.05, 0.95, f'r = {correlation:.3f}', transform=ax.transAxes, 
                bbox=dict(boxstyle="round", facecolor='white', alpha=0.8))
        
        ax.set_xlabel('X Variable')
        ax.set_ylabel('Y Variable')
        ax.set_title('Basic Scatter Plot')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/basic_scatter_plot.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建基础散点图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_basic_scatter_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
