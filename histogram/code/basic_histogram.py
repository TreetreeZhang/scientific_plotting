#!/usr/bin/env python3
"""
Basic Histogram
===============

Creates a basic histogram for single distribution analysis.

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

def create_basic_histogram():
    """
    Create a basic histogram with normal distribution overlay.
    
    Required CSV: ../data/basic_histogram_data.csv
    Required columns: values
    
    Data format:
    - values: Numerical values (float)
    
    Example CSV structure:
    values
    23.5
    25.1
    22.8
    28.3
    30.1
    27.9
    31.2
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'basic_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['values']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create histogram
        values = data['values'].dropna()
        n, bins, patches = ax.hist(values, bins=30, density=True, alpha=0.7, 
                                  color=get_color_palette(1)[0], edgecolor='black', linewidth=0.5)
        
        # Fit and plot normal distribution
        mu, sigma = stats.norm.fit(values)
        x = np.linspace(values.min(), values.max(), 100)
        y = stats.norm.pdf(x, mu, sigma)
        ax.plot(x, y, 'r-', linewidth=2, label=f'Normal fit (μ={mu:.2f}, σ={sigma:.2f})')
        
        # Customize plot
        ax.set_title('Basic Histogram with Normal Distribution Overlay', fontsize=14, fontweight='bold')
        ax.set_xlabel('Values', fontsize=12)
        ax.set_ylabel('Density', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Add statistics text
        stats_text = f"Samples: {len(values)}\nMean: {values.mean():.2f}\nStd: {values.std():.2f}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'basic_histogram.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating basic histogram: {e}")
        print("📋 Required data format for basic_histogram_data.csv:")
        print("   Columns: values")
        print("   Example:")
        print("   values")
        print("   23.5")
        print("   25.1")
        print("   22.8")
        return False
    except Exception as e:
        print(f"❌ Error creating basic histogram: {e}")
        return False


def main():
    """主函数"""
    return create_basic_histogram()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
