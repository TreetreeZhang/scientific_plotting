#!/usr/bin/env python3
"""
Horizontal Bar Chart
====================

Creates a horizontal bar chart for better label readability.

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
    return create_horizontal_bar_chart()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
