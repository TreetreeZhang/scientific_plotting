#!/usr/bin/env python3
"""
Bar Chart Plotting Module
=========================

This module creates various types of bar charts based on CSV data files.
If CSV files don't exist, it will show error messages with data format requirements.

Chart types:
1. Basic Bar Chart - 基础柱状图
2. Grouped Bar Chart - 分组柱状图
3. Stacked Bar Chart - 堆叠柱状图
4. Horizontal Bar Chart - 水平柱状图

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

def create_basic_bar_chart():
    """创建基础柱状图"""
    print("\n1. Basic Bar Chart")
    
    csv_path = "../data/basic_bar_data.csv"
    required_columns = ['category', 'value']
    data_description = """
基础柱状图数据格式:
- category: 分类名称 (字符串型)
- value: 对应的数值 (数值型)

数据示例:
category,value
Method A,85
Method B,72
Method C,91
Method D,68
...

用途: 比较不同类别的数值大小
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(len(df))
        
        # 绘制柱状图
        bars = ax.bar(df['category'], df['value'], color=colors, alpha=0.8)
        
        # 添加数值标签
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height:.0f}', ha='center', va='bottom')
        
        ax.set_xlabel('Category')
        ax.set_ylabel('Value')
        ax.set_title('Basic Bar Chart')
        ax.grid(True, alpha=0.3, axis='y')
        
        # 保存图片
        save_plot(fig, "../plot/basic_bar_chart.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建基础柱状图: {str(e)}")
        return False
    
    return True

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

def create_horizontal_bar_chart():
    """创建水平柱状图"""
    print("\n4. Horizontal Bar Chart")
    
    csv_path = "../data/horizontal_bar_data.csv"
    required_columns = ['item', 'score']
    data_description = """
水平柱状图数据格式:
- item: 项目名称 (字符串型)
- score: 对应的分数 (数值型)

数据示例:
item,score
Algorithm A,92
Algorithm B,85
Algorithm C,78
Algorithm D,88
...

用途: 当类别名称较长时，水平显示更清晰
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 按分数排序
        df = df.sort_values('score', ascending=True)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(len(df))
        
        # 绘制水平柱状图
        bars = ax.barh(df['item'], df['score'], color=colors, alpha=0.8)
        
        # 添加数值标签
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2.,
                   f'{width:.0f}', ha='left', va='center')
        
        ax.set_xlabel('Score')
        ax.set_ylabel('Item')
        ax.set_title('Horizontal Bar Chart')
        ax.grid(True, alpha=0.3, axis='x')
        
        # 保存图片
        save_plot(fig, "../plot/horizontal_bar_chart.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建水平柱状图: {str(e)}")
        return False
    
    return True

def main():
    """主函数"""
    print("Creating Bar Charts...")
    
    success_count = 0
    total_count = 4
    
    # 创建各种柱状图
    if create_basic_bar_chart():
        success_count += 1
    
    if create_grouped_bar_chart():
        success_count += 1
        
    if create_stacked_bar_chart():
        success_count += 1
        
    if create_horizontal_bar_chart():
        success_count += 1
    
    print(f"\n📊 柱状图创建完成: {success_count}/{total_count} 成功")
    
    if success_count == total_count:
        print("✅ All bar charts created successfully!")
    else:
        print("⚠️ 部分柱状图创建失败，请检查数据文件")

if __name__ == "__main__":
    main() 