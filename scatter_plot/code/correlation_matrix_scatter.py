#!/usr/bin/env python3
"""
Correlation Matrix Scatter
==========================

Creates a correlation matrix visualization with scatter plots.

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

def create_correlation_matrix_scatter():
    """创建相关性矩阵散点图"""
    print("\n5. Correlation Matrix Scatter Plot")
    
    csv_path = "../data/correlation_matrix_data.csv"
    required_columns = ['var1', 'var2', 'var3', 'var4']
    data_description = """
相关性矩阵散点图数据格式:
- var1: 第一个变量 (数值型)
- var2: 第二个变量 (数值型)
- var3: 第三个变量 (数值型)
- var4: 第四个变量 (数值型)

数据示例:
var1,var2,var3,var4
1.2,2.4,3.1,4.5
2.1,4.3,2.8,3.9
3.5,6.8,4.2,5.1
4.2,8.1,3.7,4.8
...

用途: 展示多个变量之间的两两相关关系
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, axes = plt.subplots(len(required_columns), len(required_columns), 
                               figsize=(12, 12))
        fig.suptitle('Correlation Matrix Scatter Plot', fontsize=16)
        
        # 设置科学样式
        set_scientific_style()
        colors = get_color_palette(1)
        
        for i, var1 in enumerate(required_columns):
            for j, var2 in enumerate(required_columns):
                ax = axes[i, j]
                
                if i == j:
                    # 对角线显示直方图
                    ax.hist(df[var1], bins=20, color=colors[0], alpha=0.7, edgecolor='black')
                    ax.set_title(f'{var1}')
                else:
                    # 非对角线显示散点图
                    ax.scatter(df[var2], df[var1], color=colors[0], alpha=0.6, s=30)
                    
                    # 计算相关系数
                    correlation = np.corrcoef(df[var2], df[var1])[0, 1]
                    ax.text(0.05, 0.95, f'r={correlation:.2f}', transform=ax.transAxes,
                           bbox=dict(boxstyle="round", facecolor='white', alpha=0.8))
                
                # 设置标签
                if i == len(required_columns) - 1:
                    ax.set_xlabel(var2)
                if j == 0:
                    ax.set_ylabel(var1)
                
                ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # 保存图片
        save_plot(fig, "../plot/correlation_matrix_scatter.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建相关性矩阵散点图: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    return create_correlation_matrix_scatter()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
