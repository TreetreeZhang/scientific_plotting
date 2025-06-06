#!/usr/bin/env python3
"""
Multiple Line Chart
===================

Creates a line chart with multiple data series for comparison.

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


def main():
    """主函数"""
    return create_multiple_line_chart()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
