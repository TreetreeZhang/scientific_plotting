#!/usr/bin/env python3
"""
Colored Scatter Plot
====================

Creates a scatter plot with color-coded third variable.

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

def create_colored_scatter_plot():
    """创建彩色散点图"""
    print("\n2. Colored Scatter Plot")
    
    csv_path = "../data/colored_scatter_data.csv"
    required_columns = ['x', 'y', 'color_value']
    data_description = """
彩色散点图数据格式:
- x: X轴数值 (数值型)
- y: Y轴数值 (数值型)
- color_value: 用于颜色映射的第三变量 (数值型)

数据示例:
x,y,color_value
1.2,2.4,10.5
2.1,4.3,15.2
3.5,6.8,8.7
4.2,8.1,20.1
...

用途: 同时展示三个变量的关系，第三变量通过颜色表示
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        
        # 绘制彩色散点图
        scatter = ax.scatter(df['x'], df['y'], c=df['color_value'], 
                           cmap='viridis', alpha=0.7, s=60)
        
        # 添加颜色条
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Color Value')
        
        ax.set_xlabel('X Variable')
        ax.set_ylabel('Y Variable')
        ax.set_title('Colored Scatter Plot')
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/colored_scatter_plot.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建彩色散点图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_colored_scatter_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
