#!/usr/bin/env python3
"""
Basic Line Chart
================

Creates a basic line chart showing single variable trend over time.

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


def main():
    """主函数"""
    return create_basic_line_chart()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
