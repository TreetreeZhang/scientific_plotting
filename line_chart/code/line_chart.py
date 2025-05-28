#!/usr/bin/env python3
"""
Line Chart Plotting Module
==========================

This module creates various types of line charts based on CSV data files.
If CSV files don't exist, it will show error messages with data format requirements.

Chart types:
1. Basic Line Chart - 基础折线图
2. Multiple Line Chart - 多系列折线图  
3. Line Chart with Confidence Interval - 带置信区间的折线图

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

def create_basic_line_chart():
    """创建基础折线图"""
    print("\n1. Basic Line Chart")
    
    csv_path = "../data/basic_line_data.csv"
    required_columns = ['time', 'amplitude']
    data_description = """
基础折线图数据格式:
- time: 时间序列数据 (数值型)
- amplitude: 对应的幅度值 (数值型)

数据示例:
time,amplitude
0.0,0.05
0.2,0.19
0.4,0.46
0.6,0.73
...

用途: 展示单一变量随时间的变化趋势
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        
        # 绘制折线图
        ax.plot(df['time'], df['amplitude'], 'b-', linewidth=2, label='Amplitude')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        ax.set_title('Basic Line Chart')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/basic_line_chart.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建基础折线图: {str(e)}")
        return False
    
    return True

def create_multiple_line_chart():
    """创建多系列折线图"""
    print("\n2. Multiple Series Line Chart")
    
    csv_path = "../data/multiple_line_data.csv"
    required_columns = ['time', 'series_a', 'series_b', 'series_c']
    data_description = """
多系列折线图数据格式:
- time: 时间序列数据 (数值型)
- series_a: 第一个数据系列 (数值型)
- series_b: 第二个数据系列 (数值型)  
- series_c: 第三个数据系列 (数值型)

数据示例:
time,series_a,series_b,series_c
0.0,0.05,0.95,0.02
0.2,0.19,0.81,0.09
0.4,0.46,0.54,0.23
0.6,0.73,0.27,0.36
...

用途: 比较多个变量随时间的变化趋势
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(3)
        
        # 绘制多条折线
        ax.plot(df['time'], df['series_a'], color=colors[0], linewidth=2, label='Series A', marker='o', markersize=4)
        ax.plot(df['time'], df['series_b'], color=colors[1], linewidth=2, label='Series B', marker='s', markersize=4)
        ax.plot(df['time'], df['series_c'], color=colors[2], linewidth=2, label='Series C', marker='^', markersize=4)
        
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.set_title('Multiple Series Line Chart')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/multiple_line_chart.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建多系列折线图: {str(e)}")
        return False
    
    return True

def create_line_chart_with_ci():
    """创建带置信区间的折线图"""
    print("\n3. Line Chart with Confidence Interval")
    
    csv_path = "../data/confidence_interval_data.csv"
    required_columns = ['time', 'mean', 'lower_ci', 'upper_ci']
    data_description = """
带置信区间折线图数据格式:
- time: 时间序列数据 (数值型)
- mean: 平均值 (数值型)
- lower_ci: 置信区间下界 (数值型)
- upper_ci: 置信区间上界 (数值型)

数据示例:
time,mean,lower_ci,upper_ci
0.0,0.05,-0.15,0.25
0.2,0.19,-0.01,0.39
0.4,0.46,0.26,0.66
0.6,0.73,0.53,0.93
...

用途: 展示数据的不确定性和置信区间
"""
    
    try:
        # 尝试加载CSV数据
        df = check_and_load_csv(csv_path, required_columns, data_description)
        
        # 创建图形
        fig, ax = create_figure_with_style()
        colors = get_color_palette(1)
        
        # 绘制主线和置信区间
        ax.plot(df['time'], df['mean'], color=colors[0], linewidth=2, label='Mean')
        ax.fill_between(df['time'], df['lower_ci'], df['upper_ci'], 
                       color=colors[0], alpha=0.3, label='95% Confidence Interval')
        
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.set_title('Line Chart with Confidence Interval')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 保存图片
        save_plot(fig, "../plot/line_chart_with_ci.png")
        plt.close()
        
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ 无法创建带置信区间的折线图: {str(e)}")
        return False
    
    return True

def main():
    """主函数"""
    print("Creating Line Charts...")
    
    success_count = 0
    total_count = 3
    
    # 创建各种折线图
    if create_basic_line_chart():
        success_count += 1
    
    if create_multiple_line_chart():
        success_count += 1
        
    if create_line_chart_with_ci():
        success_count += 1
    
    print(f"\n📊 折线图创建完成: {success_count}/{total_count} 成功")
    
    if success_count == total_count:
        print("✅ All line charts created successfully!")
    else:
        print("⚠️ 部分折线图创建失败，请检查数据文件")
        print("\n💡 提示: 如果需要生成示例数据，请运行数据生成脚本")

if __name__ == "__main__":
    main() 