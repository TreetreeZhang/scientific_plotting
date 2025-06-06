#!/usr/bin/env python3
"""
Multiple Histograms
===================

Creates overlapping histograms for distribution comparison.

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

def create_multiple_histograms():
    """
    Create overlapping histograms for multiple groups.
    
    Required CSV: ../data/multiple_histogram_data.csv
    Required columns: group_a, group_b, group_c
    
    Data format:
    - group_a, group_b, group_c: Numerical values for three groups (float)
    - Note: Groups can have different lengths, use NaN for missing values
    
    Example CSV structure:
    group_a,group_b,group_c
    23.5,28.3,31.2
    25.1,30.1,33.5
    22.8,27.9,29.8
    24.2,29.5,32.1
    ,31.0,
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'multiple_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['group_a', 'group_b', 'group_c']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(3)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Create overlapping histograms
        groups = ['group_a', 'group_b', 'group_c']
        labels = ['Group A', 'Group B', 'Group C']
        
        for i, (group, label, color) in enumerate(zip(groups, labels, colors)):
            values = data[group].dropna()
            ax.hist(values, bins=25, alpha=0.6, label=label, color=color, 
                   density=True, edgecolor='black', linewidth=0.5)
        
        # Customize plot
        ax.set_title('Multiple Overlapping Histograms', fontsize=14, fontweight='bold')
        ax.set_xlabel('Values', fontsize=12)
        ax.set_ylabel('Density', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Add statistics text
        stats_text = ""
        for group, label in zip(groups, labels):
            values = data[group].dropna()
            stats_text += f"{label}: n={len(values)}, μ={values.mean():.2f}\n"
        
        ax.text(0.02, 0.98, stats_text.strip(), transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'multiple_histograms.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating multiple histograms: {e}")
        print("📋 Required data format for multiple_histogram_data.csv:")
        print("   Columns: group_a, group_b, group_c")
        print("   Example:")
        print("   group_a,group_b,group_c")
        print("   23.5,28.3,31.2")
        print("   25.1,30.1,33.5")
        print("   22.8,27.9,29.8")
        print("   Note: Use NaN or empty cells for missing values")
        return False
    except Exception as e:
        print(f"❌ Error creating multiple histograms: {e}")
        return False


def main():
    """主函数"""
    return create_multiple_histograms()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
