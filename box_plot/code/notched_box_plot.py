#!/usr/bin/env python3
"""
Notched Box Plot
================

Creates a notched box plot with statistical significance indicators.

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

def create_notched_box_plot():
    """
    Create a notched box plot for statistical significance comparison.
    
    Required CSV: ../data/notched_box_data.csv
    Required columns: method, performance
    
    Data format:
    - method: Method names (string)
    - performance: Performance values (float)
    
    Example CSV structure:
    method,performance
    Method 1,85.2
    Method 1,87.1
    Method 1,84.5
    Method 2,78.9
    Method 2,80.3
    Method 2,77.8
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'notched_box_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['method', 'performance']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(len(data['method'].unique()))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create notched box plot
        box_plot = ax.boxplot([data[data['method'] == method]['performance'].values 
                              for method in data['method'].unique()],
                             labels=data['method'].unique(),
                             patch_artist=True,
                             notch=True,  # Add notches for confidence intervals
                             showmeans=True)
        
        # Color the boxes
        for patch, color in zip(box_plot['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        # Customize plot
        ax.set_title('Notched Box Plot - Statistical Significance', fontsize=14, fontweight='bold')
        ax.set_xlabel('Methods', fontsize=12)
        ax.set_ylabel('Performance', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add explanation text
        explanation = "Notches show 95% confidence intervals\nNon-overlapping notches suggest significant difference"
        ax.text(0.02, 0.02, explanation, transform=ax.transAxes, 
                verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'notched_box_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating notched box plot: {e}")
        print("📋 Required data format for notched_box_data.csv:")
        print("   Columns: method, performance")
        print("   Example:")
        print("   method,performance")
        print("   Method 1,85.2")
        print("   Method 1,87.1")
        print("   Method 2,78.9")
        return False
    except Exception as e:
        print(f"❌ Error creating notched box plot: {e}")
        return False


def main():
    """主函数"""
    return create_notched_box_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
