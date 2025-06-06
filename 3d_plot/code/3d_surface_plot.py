#!/usr/bin/env python3
"""
3D Surface Plot
===============

Creates a 3D surface plot for mathematical functions.

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

def create_3d_surface_plot():
    """
    Create a 3D surface plot.
    
    Required CSV: ../data/3d_surface_data.csv
    Required columns: x, y, z
    
    Data format:
    - x: X coordinates (float)
    - y: Y coordinates (float)
    - z: Z coordinates/height values (float)
    
    Example CSV structure:
    x,y,z
    0.0,0.0,0.5
    0.1,0.0,0.6
    0.0,0.1,0.7
    0.1,0.1,0.8
    0.2,0.0,0.4
    
    Note: Data should form a grid for proper surface plotting.
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_surface_data.csv')
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
        
        # Prepare data for surface plot
        x = data['x'].values
        y = data['y'].values
        z = data['z'].values
        
        # Try to create a grid if data is not already gridded
        try:
            # Get unique x and y values
            x_unique = np.unique(x)
            y_unique = np.unique(y)
            
            # Create meshgrid
            X, Y = np.meshgrid(x_unique, y_unique)
            
            # Reshape Z to match the grid
            Z = np.zeros_like(X)
            for i, xi in enumerate(x_unique):
                for j, yi in enumerate(y_unique):
                    # Find corresponding z value
                    mask = (data['x'] == xi) & (data['y'] == yi)
                    if mask.any():
                        Z[j, i] = data.loc[mask, 'z'].iloc[0]
                    else:
                        # Interpolate if exact match not found
                        Z[j, i] = np.mean(z)
            
            # Create surface plot
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                                 linewidth=0.5, edgecolors='black')
            
        except Exception:
            # If gridding fails, use scatter plot as fallback
            ax.scatter(x, y, z, c=z, cmap='viridis', s=50)
            print("⚠️  Warning: Could not create surface grid, using scatter plot instead")
        
        # Customize plot
        ax.set_title('3D Surface Plot', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12)
        ax.set_ylabel('Y Coordinate', fontsize=12)
        ax.set_zlabel('Z Coordinate', fontsize=12)
        
        # Add colorbar if surface was created
        try:
            plt.colorbar(surf, ax=ax, shrink=0.5, aspect=20, label='Z Values')
        except:
            pass
        
        # Add statistics text
        stats_text = f"Data points: {len(data)}\nX range: [{x.min():.2f}, {x.max():.2f}]\nY range: [{y.min():.2f}, {y.max():.2f}]\nZ range: [{z.min():.2f}, {z.max():.2f}]"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_surface_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D surface plot: {e}")
        print("📋 Required data format for 3d_surface_data.csv:")
        print("   Columns: x, y, z")
        print("   Example:")
        print("   x,y,z")
        print("   0.0,0.0,0.5")
        print("   0.1,0.0,0.6")
        print("   0.0,0.1,0.7")
        print("   Note: Data should form a grid for proper surface plotting")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D surface plot: {e}")
        return False


def main():
    """主函数"""
    return create_3d_surface_plot()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
