"""
Box Plot Module for Scientific Plotting Suite

This module creates various types of box plots for statistical data visualization.
All plots depend on CSV data files and will raise errors if files are missing.

Chart types:
- Basic box plot
- Violin plot  
- Grouped box plot
- Notched box plot
- Horizontal box plot
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from common_utils import set_scientific_style, get_color_palette, save_plot

def create_basic_box_plot():
    """
    Create a basic box plot comparing distributions across groups.
    
    Required CSV: ../data/basic_box_data.csv
    Required columns: group, value
    
    Data format:
    - group: Group names (string)
    - value: Numerical values (float)
    
    Example CSV structure:
    group,value
    Group A,23.5
    Group A,25.1
    Group A,22.8
    Group B,28.3
    Group B,30.1
    Group B,27.9
    
    Note: Each group should have multiple data points for meaningful box plots.
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'basic_box_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['group', 'value']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(len(data['group'].unique()))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create box plot
        box_plot = ax.boxplot([data[data['group'] == group]['value'].values 
                              for group in data['group'].unique()],
                             labels=data['group'].unique(),
                             patch_artist=True,
                             notch=False,
                             showmeans=True)
        
        # Color the boxes
        for patch, color in zip(box_plot['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        # Customize plot
        ax.set_title('Basic Box Plot - Distribution Comparison', fontsize=14, fontweight='bold')
        ax.set_xlabel('Groups', fontsize=12)
        ax.set_ylabel('Values', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add statistics text
        stats_text = f"Groups: {len(data['group'].unique())}\nTotal samples: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'basic_box_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating basic box plot: {e}")
        print("📋 Required data format for basic_box_data.csv:")
        print("   Columns: group, value")
        print("   Example:")
        print("   group,value")
        print("   Group A,23.5")
        print("   Group A,25.1")
        print("   Group B,28.3")
        print("   Group B,30.1")
        return False
    except Exception as e:
        print(f"❌ Error creating basic box plot: {e}")
        return False

def create_violin_plot():
    """
    Create a violin plot showing distribution density.
    
    Required CSV: ../data/violin_plot_data.csv
    Required columns: category, measurement
    
    Data format:
    - category: Category names (string)
    - measurement: Numerical measurements (float)
    
    Example CSV structure:
    category,measurement
    Type A,15.2
    Type A,16.8
    Type A,14.9
    Type B,18.5
    Type B,19.2
    Type B,17.8
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'violin_plot_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['category', 'measurement']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create violin plot
        sns.violinplot(data=data, x='category', y='measurement', ax=ax, palette='Set2')
        
        # Customize plot
        ax.set_title('Violin Plot - Distribution Density', fontsize=14, fontweight='bold')
        ax.set_xlabel('Categories', fontsize=12)
        ax.set_ylabel('Measurements', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add statistics
        stats_text = f"Categories: {len(data['category'].unique())}\nTotal measurements: {len(data)}"
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'violin_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating violin plot: {e}")
        print("📋 Required data format for violin_plot_data.csv:")
        print("   Columns: category, measurement")
        print("   Example:")
        print("   category,measurement")
        print("   Type A,15.2")
        print("   Type A,16.8")
        print("   Type B,18.5")
        return False
    except Exception as e:
        print(f"❌ Error creating violin plot: {e}")
        return False

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

def create_notched_box_plot():
    """
    Create a notched box plot for statistical significance comparison.
    
    Required CSV: ../data/notched_box_data.csv
    Required columns: method, performance
    
    Data format:
    - method: Method names (string)
    - performance: Performance values (float)
    
    Example CSV structure:
    method,performance
    Method 1,85.2
    Method 1,87.1
    Method 1,84.5
    Method 2,78.9
    Method 2,80.3
    Method 2,77.8
    """
    try:
        # Check for required CSV file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'notched_box_data.csv')
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Required CSV file not found: {csv_path}")
        
        # Load and validate data
        data = pd.read_csv(csv_path)
        required_columns = ['method', 'performance']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
        
        # Set style and create plot
        set_scientific_style()
        colors = get_color_palette(len(data['method'].unique()))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create notched box plot
        box_plot = ax.boxplot([data[data['method'] == method]['performance'].values 
                              for method in data['method'].unique()],
                             labels=data['method'].unique(),
                             patch_artist=True,
                             notch=True,  # Add notches for confidence intervals
                             showmeans=True)
        
        # Color the boxes
        for patch, color in zip(box_plot['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        # Customize plot
        ax.set_title('Notched Box Plot - Statistical Significance', fontsize=14, fontweight='bold')
        ax.set_xlabel('Methods', fontsize=12)
        ax.set_ylabel('Performance', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add explanation text
        explanation = "Notches show 95% confidence intervals\nNon-overlapping notches suggest significant difference"
        ax.text(0.02, 0.02, explanation, transform=ax.transAxes, 
                verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
        
        plt.tight_layout()
        save_plot(fig, os.path.join(os.path.dirname(__file__), '..', 'plot', 'notched_box_plot.png'))
        plt.close()
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error creating notched box plot: {e}")
        print("📋 Required data format for notched_box_data.csv:")
        print("   Columns: method, performance")
        print("   Example:")
        print("   method,performance")
        print("   Method 1,85.2")
        print("   Method 1,87.1")
        print("   Method 2,78.9")
        return False
    except Exception as e:
        print(f"❌ Error creating notched box plot: {e}")
        return False

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
    """Main function to create all box plots."""
    print("🎯 Creating Box Plots...")
    
    # List of plot creation functions
    plot_functions = [
        ("Basic Box Plot", create_basic_box_plot),
        ("Violin Plot", create_violin_plot),
        ("Grouped Box Plot", create_grouped_box_plot),
        ("Notched Box Plot", create_notched_box_plot),
        ("Horizontal Box Plot", create_horizontal_box_plot)
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
    
    print(f"📈 Box Plot Summary: {successful_plots}/{len(plot_functions)} plots created successfully!")
    return successful_plots == len(plot_functions)

if __name__ == "__main__":
    main() 