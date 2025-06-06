#!/usr/bin/env python3
"""
Basic Bar Chart
===============

Creates a basic bar chart for categorical data comparison.

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


def main():
    """主函数"""
    return create_basic_bar_chart()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
