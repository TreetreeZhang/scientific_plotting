#!/usr/bin/env python3
"""
Horizontal Box Plot
===================

Creates a horizontal box plot for alternative layout.

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

def create_horizontal_box_plot():
    """
    Create a horizontal box plot for algorithm performance comparison.
    
    Required CSV: ../data/horizontal_box_data.csv
    Required columns: algorithm, execution_time
    
    Data format:
    - algorithm: Algorithm names (string)
    - execution_time: Execution times (float)
    
    Example CSV structure:
    algorithm,execution_time
    Algorithm A,0.25
    Algorithm A,0.28
    Algorithm A,0.23
    Algorithm B,0.45
    Algorithm B,0.48
    Algorithm B,0.42
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'horizontal_box_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['algorithm', 'execution_time']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create horizontal box plot
        sns.boxplot(data=data, y='algorithm', x='execution_time', ax=ax, 
                   palette='viridis', orient='h')
        
        # Customize plot
        ax.set_title('Horizontal Box Plot - Algorithm Performance', fontsize=14, fontweight='bold')
        ax.set_xlabel('Execution Time (seconds)', fontsize=12)
        ax.set_ylabel('Algorithms', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add statistics
        stats_text = f"Algorithms: {len(data['algorithm'].unique())}\nTotal runs: {len(data)}"
        ax.text(0.98, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'horizontal_box_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating horizontal box plot: {e}")
        print("📋 Required data format for horizontal_box_data.csv:")
        print("   Columns: algorithm, execution_time")
        print("   Example:")
        print("   algorithm,execution_time")
        print("   Algorithm A,0.25")
        print("   Algorithm A,0.28")
        print("   Algorithm B,0.45")
        return False
    except Exception as e:
        print(f"❌ Error creating horizontal box plot: {e}")
        return False


def main():
    """主函数"""
    return create_horizontal_box_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
