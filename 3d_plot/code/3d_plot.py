"""
3D Plot Module for Scientific Plotting Suite

This module creates various types of 3D plots for scientific data visualization.
All plots depend on CSV data files and will raise errors if files are missing.

Chart types:
- 3D surface plot
- 3D scatter plot
- 3D wireframe plot
- 3D bar plot
- 3D contour plot
- Parametric 3D plot
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from common_utils import set_scientific_style, get_color_palette, save_plot

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

def create_3d_scatter_plot():
    """
    Create a 3D scatter plot with groups.
    
    Required CSV: ../data/3d_scatter_data.csv
    Required columns: x, y, z, group
    
    Data format:
    - x, y, z: 3D coordinates (float)
    - group: Group labels (string)
    
    Example CSV structure:
    x,y,z,group
    1.2,2.4,3.1,Group A
    2.1,4.3,2.8,Group B
    3.5,6.8,4.2,Group A
    4.2,8.1,3.7,Group C
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_scatter_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x', 'y', 'z', 'group']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Get unique groups and colors
        groups = data['group'].unique()
        colors = get_color_palette(len(groups))
        
        # Create scatter plot for each group
        for i, group in enumerate(groups):
            group_data = data[data['group'] == group]
            ax.scatter(group_data['x'], group_data['y'], group_data['z'], 
                      c=colors[i], label=group, s=60, alpha=0.7)
        
        # Customize plot
        ax.set_title('3D Scatter Plot by Groups', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Coordinate', fontsize=12)
        ax.set_ylabel('Y Coordinate', fontsize=12)
        ax.set_zlabel('Z Coordinate', fontsize=12)
        ax.legend()
        
        # Add statistics text
        stats_text = f"Groups: {len(groups)}\nTotal points: {len(data)}"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_scatter_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D scatter plot: {e}")
        print("📋 Required data format for 3d_scatter_data.csv:")
        print("   Columns: x, y, z, group")
        print("   Example:")
        print("   x,y,z,group")
        print("   1.2,2.4,3.1,Group A")
        print("   2.1,4.3,2.8,Group B")
        print("   3.5,6.8,4.2,Group A")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D scatter plot: {e}")
        return False

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

def create_3d_bar_plot():
    """
    Create a 3D bar plot.
    
    Required CSV: ../data/3d_bar_data.csv
    Required columns: x_pos, y_pos, height
    
    Data format:
    - x_pos: X position (integer)
    - y_pos: Y position (integer)
    - height: Bar height (float)
    
    Example CSV structure:
    x_pos,y_pos,height
    0,0,5.2
    1,0,7.8
    2,0,3.4
    0,1,6.1
    1,1,8.9
    2,1,4.7
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '3d_bar_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x_pos', 'y_pos', 'height']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Prepare data
        xpos = data['x_pos'].values
        ypos = data['y_pos'].values
        zpos = np.zeros_like(xpos)
        dx = np.ones_like(xpos) * 0.8
        dy = np.ones_like(ypos) * 0.8
        dz = data['height'].values
        
        # Create color map based on height
        colors = plt.cm.viridis(dz / dz.max())
        
        # Create 3D bar plot
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8)
        
        # Customize plot
        ax.set_title('3D Bar Plot', fontsize=14, fontweight='bold')
        ax.set_xlabel('X Position', fontsize=12)
        ax.set_ylabel('Y Position', fontsize=12)
        ax.set_zlabel('Height', fontsize=12)
        
        # Add statistics text
        stats_text = f"Bars: {len(data)}\nHeight range: [{dz.min():.2f}, {dz.max():.2f}]\nMean height: {dz.mean():.2f}"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '3d_bar_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 3D bar plot: {e}")
        print("📋 Required data format for 3d_bar_data.csv:")
        print("   Columns: x_pos, y_pos, height")
        print("   Example:")
        print("   x_pos,y_pos,height")
        print("   0,0,5.2")
        print("   1,0,7.8")
        print("   2,0,3.4")
        return False
    except Exception as e:
        print(f"❌ Error creating 3D bar plot: {e}")
        return False

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
    """Main function to create all 3D plots."""
    print("🎯 Creating 3D Plots...")
    
    # List of plot creation functions
    plot_functions = [
        ("3D Surface Plot", create_3d_surface_plot),
        ("3D Scatter Plot", create_3d_scatter_plot),
        ("3D Wireframe Plot", create_3d_wireframe_plot),
        ("3D Bar Plot", create_3d_bar_plot),
        ("3D Contour Plot", create_3d_contour_plot),
        ("Parametric 3D Plot", create_parametric_3d_plot)
    ]
    
    successful_plots = 0
    
    for plot_name, plot_func in plot_functions:
        print(f"📊 Creating {plot_name}...")
        if plot_func():
            print(f"✅ {plot_name} created successfully!")
            successful_plots += 1
        else:
            print(f"❌ Failed to create {plot_name}")
        print()
    
    print(f"📈 3D Plot Summary: {successful_plots}/{len(plot_functions)} plots created successfully!")
    return successful_plots == len(plot_functions)

if __name__ == "__main__":
    main() 