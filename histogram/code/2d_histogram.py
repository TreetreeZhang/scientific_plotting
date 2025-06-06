#!/usr/bin/env python3
"""
2D Histogram
============

Creates a 2D histogram for bivariate distribution analysis.

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

def create_2d_histogram():
    """
    Create a 2D histogram (heatmap and hexbin plot).
    
    Required CSV: ../data/2d_histogram_data.csv
    Required columns: x, y
    
    Data format:
    - x: X-axis values (float)
    - y: Y-axis values (float)
    
    Example CSV structure:
    x,y
    1.2,2.4
    2.1,4.3
    3.5,6.8
    4.2,8.1
    5.0,9.9
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '2d_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x', 'y']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 2D Histogram (Heatmap)
        x, y = data['x'], data['y']
        
        # Create 2D histogram
        hist, xedges, yedges = np.histogram2d(x, y, bins=20)
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        
        im1 = ax1.imshow(hist.T, extent=extent, origin='lower', cmap='Blues', aspect='auto')
        ax1.set_title('2D Histogram (Heatmap)', fontsize=12, fontweight='bold')
        ax1.set_xlabel('X Values', fontsize=10)
        ax1.set_ylabel('Y Values', fontsize=10)
        plt.colorbar(im1, ax=ax1, label='Frequency')
        
        # Hexagonal binning
        hb = ax2.hexbin(x, y, gridsize=20, cmap='Reds', mincnt=1)
        ax2.set_title('2D Histogram (Hexbin)', fontsize=12, fontweight='bold')
        ax2.set_xlabel('X Values', fontsize=10)
        ax2.set_ylabel('Y Values', fontsize=10)
        plt.colorbar(hb, ax=ax2, label='Frequency')
        
        # Add statistics text
        stats_text = f"Data points: {len(data)}\nX range: [{x.min():.2f}, {x.max():.2f}]\nY range: [{y.min():.2f}, {y.max():.2f}]"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '2d_histogram.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 2D histogram: {e}")
        print("📋 Required data format for 2d_histogram_data.csv:")
        print("   Columns: x, y")
        print("   Example:")
        print("   x,y")
        print("   1.2,2.4")
        print("   2.1,4.3")
        print("   3.5,6.8")
        return False
    except Exception as e:
        print(f"❌ Error creating 2D histogram: {e}")
        return False


def main():
    """主函数"""
    return create_2d_histogram()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
