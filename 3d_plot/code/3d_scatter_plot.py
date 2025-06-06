#!/usr/bin/env python3
"""
3D Scatter Plot
===============

Creates a 3D scatter plot for three-dimensional data.

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

def create_3d_scatter_plot():
    """
    Create a 3D scatter plot with groups.
    
    Required CSV: ../data/3d_scatter_data.csv
    Required columns: x, y, z, group
    
    Data format:
    - x, y, z: 3D coordinates (float)
    - group: Group labels (string)
    
    Example CSV structure:
    x,y,z,group
    1.2,2.4,3.1,Group A
    2.1,4.3,2.8,Group B
    3.5,6.8,4.2,Group A
    4.2,8.1,3.7,Group C
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_scatter_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x', 'y', 'z', 'group']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Get unique groups and colors
        groups = data['group'].unique()
        colors = get_color_palette(len(groups))
        
        # Create scatter plot for each group
        for i, group in enumerate(groups):
            group_data = data[data['group'] == group]
            ax.scatter(group_data['x'], group_data['y'], group_data['z'], 
                      c=colors[i], label=group, s=60, alpha=0.7)
        
        # Customize plot
        ax.set_title('3D Scatter Plot by Groups', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12)
        ax.set_ylabel('Y Coordinate', fontsize=12)
        ax.set_zlabel('Z Coordinate', fontsize=12)
        ax.legend()
        
        # Add statistics text
        stats_text = f"Groups: {len(groups)}\nTotal points: {len(data)}"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_scatter_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D scatter plot: {e}")
        print("📋 Required data format for 3d_scatter_data.csv:")
        print("   Columns: x, y, z, group")
        print("   Example:")
        print("   x,y,z,group")
        print("   1.2,2.4,3.1,Group A")
        print("   2.1,4.3,2.8,Group B")
        print("   3.5,6.8,4.2,Group A")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D scatter plot: {e}")
        return False


def main():
    """主函数"""
    return create_3d_scatter_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
