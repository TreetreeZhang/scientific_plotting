#!/usr/bin/env python3
"""
3D Wireframe Plot
=================

Creates a 3D wireframe plot for mesh visualization.

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

def create_3d_wireframe_plot():
    """
    Create a 3D wireframe plot.
    
    Required CSV: ../data/3d_wireframe_data.csv
    Required columns: x, y, z
    
    Data format:
    - x: X coordinates (float)
    - y: Y coordinates (float)
    - z: Z coordinates (float)
    
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
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_wireframe_data.csv')
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
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Prepare data for wireframe plot
        x = data['x'].values
        y = data['y'].values
        z = data['z'].values
        
        # Try to create a grid
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
            
            # Create wireframe plot
            ax.plot_wireframe(X, Y, Z, color='blue', alpha=0.7, linewidth=1)
            
        except Exception:
            # Fallback to scatter plot
            ax.scatter(x, y, z, c='blue', s=50)
            print("⚠️  Warning: Could not create wireframe grid, using scatter plot instead")
        
        # Customize plot
        ax.set_title('3D Wireframe Plot', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12)
        ax.set_ylabel('Y Coordinate', fontsize=12)
        ax.set_zlabel('Z Coordinate', fontsize=12)
        
        # Add statistics text
        stats_text = f"Data points: {len(data)}\nX range: [{x.min():.2f}, {x.max():.2f}]\nY range: [{y.min():.2f}, {y.max():.2f}]\nZ range: [{z.min():.2f}, {z.max():.2f}]"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_wireframe_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D wireframe plot: {e}")
        print("📋 Required data format for 3d_wireframe_data.csv:")
        print("   Columns: x, y, z")
        print("   Example:")
        print("   x,y,z")
        print("   0.0,0.0,0.5")
        print("   0.1,0.0,0.6")
        print("   0.2,0.0,0.4")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D wireframe plot: {e}")
        return False


def main():
    """主函数"""
    return create_3d_wireframe_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
