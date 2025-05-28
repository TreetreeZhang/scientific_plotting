#!/usr/bin/env python3
"""
Scatter Plot Plotting Module
============================

This module creates various types of scatter plots based on CSV data files.
If CSV files don't exist, it will show error messages with data format requirements.

Chart types:
1. Basic Scatter Plot - 基础散点图
2. Colored Scatter Plot - 彩色散点图
3. Sized Scatter Plot - 大小变化散点图
4. Categorical Scatter Plot - 分类散点图
5. Correlation Matrix Scatter Plot - 相关性矩阵散点图

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
from scipy import stats

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
    print("Creating Scatter Plots...")
    
    success_count = 0
    total_count = 5
    
    # 创建各种散点图
    if create_basic_scatter_plot():
        success_count += 1
    
    if create_colored_scatter_plot():
        success_count += 1
        
    if create_sized_scatter_plot():
        success_count += 1
        
    if create_categorical_scatter_plot():
        success_count += 1
        
    if create_correlation_matrix_scatter():
        success_count += 1
    
    print(f"\n📊 散点图创建完成: {success_count}/{total_count} 成功")
    
    if success_count == total_count:
        print("✅ All scatter plots created successfully!")
    else:
        print("⚠️ 部分散点图创建失败，请检查数据文件")

if __name__ == "__main__":
    main() 