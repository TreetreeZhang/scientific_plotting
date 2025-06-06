#!/usr/bin/env python3
"""
Stacked Histogram
=================

Creates a stacked histogram with categorical breakdown.

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

def create_stacked_histogram():
    """
    Create a stacked histogram for categorical data.
    
    Required CSV: ../data/stacked_histogram_data.csv
    Required columns: value, category
    
    Data format:
    - value: Numerical values (float)
    - category: Category labels (string)
    
    Example CSV structure:
    value,category
    23.5,Type A
    25.1,Type A
    28.3,Type B
    30.1,Type B
    31.2,Type C
    33.5,Type C
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'stacked_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['value', 'category']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Prepare data for stacked histogram
        categories = data['category'].unique()
        colors = get_color_palette(len(categories))
        
        # Create stacked histogram
        values_by_category = [data[data['category'] == cat]['value'].values for cat in categories]
        
        ax.hist(values_by_category, bins=20, label=categories, color=colors, 
               alpha=0.7, stacked=True, edgecolor='black', linewidth=0.5)
        
        # Customize plot
        ax.set_title('Stacked Histogram by Category', fontsize=14, fontweight='bold')
        ax.set_xlabel('Values', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Add statistics text
        stats_text = f"Categories: {len(categories)}\nTotal samples: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'stacked_histogram.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating stacked histogram: {e}")
        print("📋 Required data format for stacked_histogram_data.csv:")
        print("   Columns: value, category")
        print("   Example:")
        print("   value,category")
        print("   23.5,Type A")
        print("   25.1,Type A")
        print("   28.3,Type B")
        return False
    except Exception as e:
        print(f"❌ Error creating stacked histogram: {e}")
        return False


def main():
    """主函数"""
    return create_stacked_histogram()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
