import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')

# Set global plotting style
def set_scientific_style():
    """Set scientific plotting style similar to Nature/Science journals"""
    plt.style.use('seaborn-v0_8-whitegrid')
    rcParams['font.family'] = 'Arial'
    rcParams['font.size'] = 12
    rcParams['axes.labelsize'] = 14
    rcParams['axes.titlesize'] = 16
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['legend.fontsize'] = 12
    rcParams['figure.titlesize'] = 18
    rcParams['axes.linewidth'] = 1.2
    rcParams['grid.alpha'] = 0.3
    rcParams['axes.spines.top'] = False
    rcParams['axes.spines.right'] = False

def get_color_palette(n_colors=6):
    """Get a scientific color palette"""
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    if n_colors <= len(colors):
        return colors[:n_colors]
    else:
        return sns.color_palette("husl", n_colors)

def save_plot(fig, filename, dpi=300, bbox_inches='tight'):
    """Save plot with high quality settings"""
    fig.savefig(filename, dpi=dpi, bbox_inches=bbox_inches, 
                facecolor='white', edgecolor='none')
    print(f"Plot saved as: {filename}")

def generate_sample_data(data_type, n_samples=100, **kwargs):
    """Generate sample data for different plot types"""
    np.random.seed(42)  # For reproducibility
    
    if data_type == 'time_series':
        x = np.linspace(0, 10, n_samples)
        y = np.sin(x) + 0.1 * np.random.randn(n_samples)
        return x, y
    
    elif data_type == 'multiple_series':
        x = np.linspace(0, 10, n_samples)
        y1 = np.sin(x) + 0.1 * np.random.randn(n_samples)
        y2 = np.cos(x) + 0.1 * np.random.randn(n_samples)
        y3 = np.sin(x + np.pi/4) + 0.1 * np.random.randn(n_samples)
        return x, y1, y2, y3
    
    elif data_type == 'categorical':
        categories = kwargs.get('categories', ['A', 'B', 'C', 'D', 'E'])
        values = np.random.randint(10, 100, len(categories))
        return categories, values
    
    elif data_type == 'scatter':
        x = np.random.randn(n_samples)
        y = 2 * x + np.random.randn(n_samples)
        return x, y
    
    elif data_type == 'multivariate_scatter':
        x = np.random.randn(n_samples)
        y = 2 * x + np.random.randn(n_samples)
        z = x + y + np.random.randn(n_samples)
        sizes = np.random.randint(20, 200, n_samples)
        return x, y, z, sizes
    
    elif data_type == 'distribution':
        return np.random.normal(0, 1, n_samples)
    
    elif data_type == 'multiple_distributions':
        group1 = np.random.normal(0, 1, n_samples)
        group2 = np.random.normal(2, 1.5, n_samples)
        group3 = np.random.normal(-1, 0.8, n_samples)
        return group1, group2, group3
    
    elif data_type == '3d_surface':
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))
        return X, Y, Z
    
    else:
        raise ValueError(f"Unknown data type: {data_type}")

def add_confidence_interval(ax, x, y, alpha=0.2, color=None):
    """Add confidence interval to a line plot"""
    if color is None:
        color = ax.get_lines()[-1].get_color()
    
    # Calculate confidence interval (simplified)
    std = np.std(y)
    ci_upper = y + 1.96 * std / np.sqrt(len(y))
    ci_lower = y - 1.96 * std / np.sqrt(len(y))
    
    ax.fill_between(x, ci_lower, ci_upper, alpha=alpha, color=color)
    return ax

def format_axes(ax, xlabel=None, ylabel=None, title=None):
    """Format axes with scientific style"""
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    return ax 