#!/usr/bin/env python3
"""
Distribution Comparison
=======================

Creates histogram with statistical distribution overlays.

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

def create_distribution_comparison():
    """
    Create histograms comparing different statistical distributions.
    
    Required CSV: ../data/distribution_comparison_data.csv
    Required columns: observed, theoretical
    
    Data format:
    - observed: Observed values (float)
    - theoretical: Theoretical values (float)
    
    Example CSV structure:
    observed,theoretical
    23.5,24.1
    25.1,25.8
    22.8,23.2
    28.3,28.9
    30.1,29.7
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'distribution_comparison_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['observed', 'theoretical']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(2)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Overlapping histograms
        observed = data['observed'].dropna()
        theoretical = data['theoretical'].dropna()
        
        ax1.hist(observed, bins=25, alpha=0.6, label='Observed', color=colors[0], 
                density=True, edgecolor='black', linewidth=0.5)
        ax1.hist(theoretical, bins=25, alpha=0.6, label='Theoretical', color=colors[1], 
                density=True, edgecolor='black', linewidth=0.5)
        
        ax1.set_title('Distribution Comparison', fontsize=12, fontweight='bold')
        ax1.set_xlabel('Values', fontsize=10)
        ax1.set_ylabel('Density', fontsize=10)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Q-Q plot for comparison
        from scipy.stats import probplot
        probplot(observed, dist="norm", plot=ax2)
        ax2.set_title('Q-Q Plot (Observed vs Normal)', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        # Add statistics text
        stats_text = f"Observed: n={len(observed)}, μ={observed.mean():.2f}, σ={observed.std():.2f}\n"
        stats_text += f"Theoretical: n={len(theoretical)}, μ={theoretical.mean():.2f}, σ={theoretical.std():.2f}"
        
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'distribution_comparison.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating distribution comparison: {e}")
        print("📋 Required data format for distribution_comparison_data.csv:")
        print("   Columns: observed, theoretical")
        print("   Example:")
        print("   observed,theoretical")
        print("   23.5,24.1")
        print("   25.1,25.8")
        print("   22.8,23.2")
        return False
    except Exception as e:
        print(f"❌ Error creating distribution comparison: {e}")
        return False


def main():
    """主函数"""
    return create_distribution_comparison()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
