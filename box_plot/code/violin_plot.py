#!/usr/bin/env python3
"""
Violin Plot
===========

Creates a violin plot showing distribution density.

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

def create_violin_plot():
    """
    Create a violin plot showing distribution density.
    
    Required CSV: ../data/violin_plot_data.csv
    Required columns: category, measurement
    
    Data format:
    - category: Category names (string)
    - measurement: Numerical measurements (float)
    
    Example CSV structure:
    category,measurement
    Type A,15.2
    Type A,16.8
    Type A,14.9
    Type B,18.5
    Type B,19.2
    Type B,17.8
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'violin_plot_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['category', 'measurement']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create violin plot
        sns.violinplot(data=data, x='category', y='measurement', ax=ax, palette='Set2')
        
        # Customize plot
        ax.set_title('Violin Plot - Distribution Density', fontsize=14, fontweight='bold')
        ax.set_xlabel('Categories', fontsize=12)
        ax.set_ylabel('Measurements', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add statistics
        stats_text = f"Categories: {len(data['category'].unique())}\nTotal measurements: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'violin_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating violin plot: {e}")
        print("📋 Required data format for violin_plot_data.csv:")
        print("   Columns: category, measurement")
        print("   Example:")
        print("   category,measurement")
        print("   Type A,15.2")
        print("   Type A,16.8")
        print("   Type B,18.5")
        return False
    except Exception as e:
        print(f"❌ Error creating violin plot: {e}")
        return False


def main():
    """主函数"""
    return create_violin_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
