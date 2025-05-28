"""
Histogram Module for Scientific Plotting Suite

This module creates various types of histograms for data distribution visualization.
All plots depend on CSV data files and will raise errors if files are missing.

Chart types:
- Basic histogram with normal distribution overlay
- Multiple overlapping histograms
- Stacked histogram
- 2D histogram (heatmap and hexbin)
- Distribution comparison histogram
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from common_utils import set_scientific_style, get_color_palette, save_plot

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

def create_multiple_histograms():
    """
    Create overlapping histograms for multiple groups.
    
    Required CSV: ../data/multiple_histogram_data.csv
    Required columns: group_a, group_b, group_c
    
    Data format:
    - group_a, group_b, group_c: Numerical values for three groups (float)
    - Note: Groups can have different lengths, use NaN for missing values
    
    Example CSV structure:
    group_a,group_b,group_c
    23.5,28.3,31.2
    25.1,30.1,33.5
    22.8,27.9,29.8
    24.2,29.5,32.1
    ,31.0,
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'multiple_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['group_a', 'group_b', 'group_c']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(3)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Create overlapping histograms
        groups = ['group_a', 'group_b', 'group_c']
        labels = ['Group A', 'Group B', 'Group C']
        
        for i, (group, label, color) in enumerate(zip(groups, labels, colors)):
            values = data[group].dropna()
            ax.hist(values, bins=25, alpha=0.6, label=label, color=color, 
                   density=True, edgecolor='black', linewidth=0.5)
        
        # Customize plot
        ax.set_title('Multiple Overlapping Histograms', fontsize=14, fontweight='bold')
        ax.set_xlabel('Values', fontsize=12)
        ax.set_ylabel('Density', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Add statistics text
        stats_text = ""
        for group, label in zip(groups, labels):
            values = data[group].dropna()
            stats_text += f"{label}: n={len(values)}, μ={values.mean():.2f}\n"
        
        ax.text(0.02, 0.98, stats_text.strip(), transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'multiple_histograms.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating multiple histograms: {e}")
        print("📋 Required data format for multiple_histogram_data.csv:")
        print("   Columns: group_a, group_b, group_c")
        print("   Example:")
        print("   group_a,group_b,group_c")
        print("   23.5,28.3,31.2")
        print("   25.1,30.1,33.5")
        print("   22.8,27.9,29.8")
        print("   Note: Use NaN or empty cells for missing values")
        return False
    except Exception as e:
        print(f"❌ Error creating multiple histograms: {e}")
        return False

def create_stacked_histogram():
    """
    Create a stacked histogram for categorical data.
    
    Required CSV: ../data/stacked_histogram_data.csv
    Required columns: value, category
    
    Data format:
    - value: Numerical values (float)
    - category: Category labels (string)
    
    Example CSV structure:
    value,category
    23.5,Type A
    25.1,Type A
    28.3,Type B
    30.1,Type B
    31.2,Type C
    33.5,Type C
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'stacked_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['value', 'category']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Prepare data for stacked histogram
        categories = data['category'].unique()
        colors = get_color_palette(len(categories))
        
        # Create stacked histogram
        values_by_category = [data[data['category'] == cat]['value'].values for cat in categories]
        
        ax.hist(values_by_category, bins=20, label=categories, color=colors, 
               alpha=0.7, stacked=True, edgecolor='black', linewidth=0.5)
        
        # Customize plot
        ax.set_title('Stacked Histogram by Category', fontsize=14, fontweight='bold')
        ax.set_xlabel('Values', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Add statistics text
        stats_text = f"Categories: {len(categories)}\nTotal samples: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'stacked_histogram.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating stacked histogram: {e}")
        print("📋 Required data format for stacked_histogram_data.csv:")
        print("   Columns: value, category")
        print("   Example:")
        print("   value,category")
        print("   23.5,Type A")
        print("   25.1,Type A")
        print("   28.3,Type B")
        return False
    except Exception as e:
        print(f"❌ Error creating stacked histogram: {e}")
        return False

def create_2d_histogram():
    """
    Create a 2D histogram (heatmap and hexbin plot).
    
    Required CSV: ../data/2d_histogram_data.csv
    Required columns: x, y
    
    Data format:
    - x: X-axis values (float)
    - y: Y-axis values (float)
    
    Example CSV structure:
    x,y
    1.2,2.4
    2.1,4.3
    3.5,6.8
    4.2,8.1
    5.0,9.9
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', '2d_histogram_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['x', 'y']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 2D Histogram (Heatmap)
        x, y = data['x'], data['y']
        
        # Create 2D histogram
        hist, xedges, yedges = np.histogram2d(x, y, bins=20)
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        
        im1 = ax1.imshow(hist.T, extent=extent, origin='lower', cmap='Blues', aspect='auto')
        ax1.set_title('2D Histogram (Heatmap)', fontsize=12, fontweight='bold')
        ax1.set_xlabel('X Values', fontsize=10)
        ax1.set_ylabel('Y Values', fontsize=10)
        plt.colorbar(im1, ax=ax1, label='Frequency')
        
        # Hexagonal binning
        hb = ax2.hexbin(x, y, gridsize=20, cmap='Reds', mincnt=1)
        ax2.set_title('2D Histogram (Hexbin)', fontsize=12, fontweight='bold')
        ax2.set_xlabel('X Values', fontsize=10)
        ax2.set_ylabel('Y Values', fontsize=10)
        plt.colorbar(hb, ax=ax2, label='Frequency')
        
        # Add statistics text
        stats_text = f"Data points: {len(data)}\nX range: [{x.min():.2f}, {x.max():.2f}]\nY range: [{y.min():.2f}, {y.max():.2f}]"
        fig.text(0.02, 0.98, stats_text, transform=fig.transFigure, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', '2d_histogram.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating 2D histogram: {e}")
        print("📋 Required data format for 2d_histogram_data.csv:")
        print("   Columns: x, y")
        print("   Example:")
        print("   x,y")
        print("   1.2,2.4")
        print("   2.1,4.3")
        print("   3.5,6.8")
        return False
    except Exception as e:
        print(f"❌ Error creating 2D histogram: {e}")
        return False

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
    """Main function to create all histograms."""
    print("🎯 Creating Histograms...")
    
    # List of plot creation functions
    plot_functions = [
        ("Basic Histogram", create_basic_histogram),
        ("Multiple Histograms", create_multiple_histograms),
        ("Stacked Histogram", create_stacked_histogram),
        ("2D Histogram", create_2d_histogram),
        ("Distribution Comparison", create_distribution_comparison)
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
    
    print(f"📈 Histogram Summary: {successful_plots}/{len(plot_functions)} plots created successfully!")
    return successful_plots == len(plot_functions)

if __name__ == "__main__":
    main() 