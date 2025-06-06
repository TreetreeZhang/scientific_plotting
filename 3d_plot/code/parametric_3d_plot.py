#!/usr/bin/env python3
"""
Parametric 3D Plot
==================

Creates a parametric 3D plot for mathematical curves.

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

def create_parametric_3d_plot():
    """
    Create a parametric 3D plot.
    
    Required CSV: ../data/parametric_3d_data.csv
    Required columns: t, x, y, z, curve_type
    
    Data format:
    - t: Parameter values (float)
    - x, y, z: 3D coordinates (float)
    - curve_type: Type of curve (string)
    
    Example CSV structure:
    t,x,y,z,curve_type
    0.0,1.0,0.0,0.0,helix
    0.1,0.95,0.31,0.1,helix
    0.2,0.81,0.59,0.2,helix
    0.0,1.0,0.0,0.0,spiral
    0.1,0.90,0.28,0.0,spiral
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'parametric_3d_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['t', 'x', 'y', 'z', 'curve_type']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Get unique curve types
        curve_types = data['curve_type'].unique()
        colors = get_color_palette(len(curve_types))
        
        # Plot each curve type
        for i, curve_type in enumerate(curve_types):
            curve_data = data[data['curve_type'] == curve_type].sort_values('t')
            ax.plot(curve_data['x'], curve_data['y'], curve_data['z'], 
                   color=colors[i], linewidth=2, label=curve_type, alpha=0.8)
        
        # Customize plot
        ax.set_title('Parametric 3D Plot', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12)
        ax.set_ylabel('Y Coordinate', fontsize=12)
        ax.set_zlabel('Z Coordinate', fontsize=12)
        ax.legend()
        
        # Add statistics text
        stats_text = f"Curve types: {len(curve_types)}\nTotal points: {len(data)}\nParameter range: [{data['t'].min():.2f}, {data['t'].max():.2f}]"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'parametric_3d_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating parametric 3D plot: {e}")
        print("📋 Required data format for parametric_3d_data.csv:")
        print("   Columns: t, x, y, z, curve_type")
        print("   Example:")
        print("   t,x,y,z,curve_type")
        print("   0.0,1.0,0.0,0.0,helix")
        print("   0.1,0.95,0.31,0.1,helix")
        print("   0.0,1.0,0.0,0.0,spiral")
        return False
    except Exception as e:
        print(f"❌ Error creating parametric 3D plot: {e}")
        return False


def main():
    """主函数"""
    return create_parametric_3d_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
