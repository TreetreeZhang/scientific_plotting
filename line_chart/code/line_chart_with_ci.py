#!/usr/bin/env python3
"""
Line Chart with CI
==================

Creates a line chart with confidence interval bands to show data uncertainty.

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
    return create_line_chart_with_ci()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
