#!/usr/bin/env python3
"""
Basic Box Plot
==============

Creates a basic box plot for distribution comparison.

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

def create_basic_box_plot():
    """
    Create a basic box plot comparing distributions across groups.
    
    Required CSV: ../data/basic_box_data.csv
    Required columns: group, value
    
    Data format:
    - group: Group names (string)
    - value: Numerical values (float)
    
    Example CSV structure:
    group,value
    Group A,23.5
    Group A,25.1
    Group A,22.8
    Group B,28.3
    Group B,30.1
    Group B,27.9
    
    Note: Each group should have multiple data points for meaningful box plots.
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'basic_box_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['group', 'value']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(len(data['group'].unique()))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create box plot
        box_plot = ax.boxplot([data[data['group'] == group]['value'].values 
                              for group in data['group'].unique()],
                             labels=data['group'].unique(),
                             patch_artist=True,
                             notch=False,
                             showmeans=True)
        
        # Color the boxes
        for patch, color in zip(box_plot['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        # Customize plot
        ax.set_title('Basic Box Plot - Distribution Comparison', fontsize=14, fontweight='bold')
        ax.set_xlabel('Groups', fontsize=12)
        ax.set_ylabel('Values', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add statistics text
        stats_text = f"Groups: {len(data['group'].unique())}\nTotal samples: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'basic_box_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating basic box plot: {e}")
        print("📋 Required data format for basic_box_data.csv:")
        print("   Columns: group, value")
        print("   Example:")
        print("   group,value")
        print("   Group A,23.5")
        print("   Group A,25.1")
        print("   Group B,28.3")
        print("   Group B,30.1")
        return False
    except Exception as e:
        print(f"❌ Error creating basic box plot: {e}")
        return False


def main():
    """主函数"""
    return create_basic_box_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
