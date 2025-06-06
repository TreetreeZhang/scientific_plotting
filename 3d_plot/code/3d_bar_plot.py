#!/usr/bin/env python3
"""
3D Bar Plot
===========

Creates a 3D bar plot for categorical three-dimensional data.

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

def create_3d_bar_plot():
    """
    Create a 3D bar plot.
    
    Required CSV: ../data/3d_bar_data.csv
    Required columns: x_pos, y_pos, height
    
    Data format:
    - x_pos: X position (integer)
    - y_pos: Y position (integer)
    - height: Bar height (float)
    
    Example CSV structure:
    x_pos,y_pos,height
    0,0,5.2
    1,0,7.8
    2,0,3.4
    0,1,6.1
    1,1,8.9
    2,1,4.7
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_bar_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x_pos', 'y_pos', 'height']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Prepare data
        xpos = data['x_pos'].values
        ypos = data['y_pos'].values
        zpos = np.zeros_like(xpos)
        dx = np.ones_like(xpos) * 0.8
        dy = np.ones_like(ypos) * 0.8
        dz = data['height'].values
        
        # Create color map based on height
        colors = plt.cm.viridis(dz / dz.max())
        
        # Create 3D bar plot
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8)
        
        # Customize plot
        ax.set_title('3D Bar Plot', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Position', fontsize=12)
        ax.set_ylabel('Y Position', fontsize=12)
        ax.set_zlabel('Height', fontsize=12)
        
        # Add statistics text
        stats_text = f"Bars: {len(data)}\nHeight range: [{dz.min():.2f}, {dz.max():.2f}]\nMean height: {dz.mean():.2f}"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_bar_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D bar plot: {e}")
        print("📋 Required data format for 3d_bar_data.csv:")
        print("   Columns: x_pos, y_pos, height")
        print("   Example:")
        print("   x_pos,y_pos,height")
        print("   0,0,5.2")
        print("   1,0,7.8")
        print("   2,0,3.4")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D bar plot: {e}")
        return False


def main():
    """主函数"""
    return create_3d_bar_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
