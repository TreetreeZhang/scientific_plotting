#!/usr/bin/env python3
"""
Grouped Box Plot
================

Creates a grouped box plot for multi-factor analysis.

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

def create_grouped_box_plot():
    """
    Create a grouped box plot for multi-factor analysis.
    
    Required CSV: ../data/grouped_box_data.csv
    Required columns: time_point, condition, response
    
    Data format:
    - time_point: Time points (string)
    - condition: Experimental conditions (string)
    - response: Response values (float)
    
    Example CSV structure:
    time_point,condition,response
    T1,Control,12.5
    T1,Control,13.2
    T1,Treatment,15.8
    T1,Treatment,16.1
    T2,Control,14.2
    T2,Treatment,18.5
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'grouped_box_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['time_point', 'condition', 'response']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Create grouped box plot
        sns.boxplot(data=data, x='time_point', y='response', hue='condition', ax=ax, palette='Set1')
        
        # Customize plot
        ax.set_title('Grouped Box Plot - Multi-Factor Analysis', fontsize=14, fontweight='bold')
        ax.set_xlabel('Time Points', fontsize=12)
        ax.set_ylabel('Response Values', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend(title='Condition', loc='upper left')
        
        # Add statistics
        stats_text = f"Time points: {len(data['time_point'].unique())}\nConditions: {len(data['condition'].unique())}\nTotal samples: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'grouped_box_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating grouped box plot: {e}")
        print("📋 Required data format for grouped_box_data.csv:")
        print("   Columns: time_point, condition, response")
        print("   Example:")
        print("   time_point,condition,response")
        print("   T1,Control,12.5")
        print("   T1,Treatment,15.8")
        print("   T2,Control,14.2")
        return False
    except Exception as e:
        print(f"❌ Error creating grouped box plot: {e}")
        return False


def main():
    """主函数"""
    return create_grouped_box_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
