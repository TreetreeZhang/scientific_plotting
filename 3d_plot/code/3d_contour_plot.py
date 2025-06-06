#!/usr/bin/env python3
"""
3D Contour Plot
===============

Creates a 3D contour plot with level curves.

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

def create_3d_contour_plot():
    """
    Create a 3D contour plot.
    
    Required CSV: ../data/3d_contour_data.csv
    Required columns: x, y, z
    
    Data format:
    - x: X coordinates (float)
    - y: Y coordinates (float)
    - z: Z values for contour lines (float)
    
    Example CSV structure:
    x,y,z
    0.0,0.0,0.5
    0.1,0.0,0.6
    0.2,0.0,0.4
    0.0,0.1,0.7
    0.1,0.1,0.8
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_contour_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x', 'y', 'z']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig = plt.figure(figsize=(15, 6))
        
        # 3D contour plot
        ax1 = fig.add_subplot(121, projection='3d')
        
        # Prepare data
        x = data['x'].values
        y = data['y'].values
        z = data['z'].values
        
        # Try to create grid for contour
        try:
            x_unique = np.unique(x)
            y_unique = np.unique(y)
            X, Y = np.meshgrid(x_unique, y_unique)
            
            Z = np.zeros_like(X)
            for i, xi in enumerate(x_unique):
                for j, yi in enumerate(y_unique):
                    mask = (data['x'] == xi) & (data['y'] == yi)
                    if mask.any():
                        Z[j, i] = data.loc[mask, 'z'].iloc[0]
                    else:
                        Z[j, i] = np.mean(z)
            
            # Create 3D contour
            ax1.contour3D(X, Y, Z, 50, cmap='viridis')
            
            # 2D contour for comparison
            ax2 = fig.add_subplot(122)
            contour = ax2.contour(X, Y, Z, 20, cmap='viridis')
            ax2.clabel(contour, inline=True, fontsize=8)
            ax2.set_title('2D Contour (for comparison)', fontsize=12, fontweight='bold')
            ax2.set_xlabel('X Coordinate', fontsize=10)
            ax2.set_ylabel('Y Coordinate', fontsize=10)
            
        except Exception:
            # Fallback to scatter plot
            ax1.scatter(x, y, z, c=z, cmap='viridis', s=50)
            print("⚠️  Warning: Could not create contour grid, using scatter plot instead")
        
        # Customize 3D plot
        ax1.set_title('3D Contour Plot', fontsize=12, fontweight='bold')
        ax1.set_xlabel('X Coordinate', fontsize=10)
        ax1.set_ylabel('Y Coordinate', fontsize=10)
        ax1.set_zlabel('Z Coordinate', fontsize=10)
        
        # Add statistics text
        stats_text = f"Data points: {len(data)}\nZ range: [{z.min():.2f}, {z.max():.2f}]"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_contour_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D contour plot: {e}")
        print("📋 Required data format for 3d_contour_data.csv:")
        print("   Columns: x, y, z")
        print("   Example:")
        print("   x,y,z")
        print("   0.0,0.0,0.5")
        print("   0.1,0.0,0.6")
        print("   0.2,0.0,0.4")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D contour plot: {e}")
        return False


def main():
    """主函数"""
    return create_3d_contour_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
