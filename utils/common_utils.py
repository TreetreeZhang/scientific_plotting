import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from pathlib import Path

def set_scientific_style():
    """设置科学绘图样式"""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.titlesize': 16,
        'font.family': 'serif',
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight'
    })

def get_color_palette(n_colors=10):
    """获取科学绘图配色方案"""
    return sns.color_palette("husl", n_colors)

def save_plot(fig, filename, dpi=300):
    """保存图片到指定路径"""
    # 确保目录存在
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"Plot saved as: {filename}")

def check_and_load_csv(csv_path, required_columns, data_description):
    """
    检查CSV文件是否存在，如果存在则加载，如果不存在则报错并说明数据格式要求
    
    Parameters:
    -----------
    csv_path : str
        CSV文件路径
    required_columns : list
        必需的列名列表
    data_description : str
        数据描述和格式要求
    
    Returns:
    --------
    pd.DataFrame
        加载的数据
    """
    if not os.path.exists(csv_path):
        error_msg = f"""
❌ 数据文件不存在: {csv_path}

📋 数据格式要求:
{data_description}

📝 必需的列名: {', '.join(required_columns)}

💡 请创建包含以上列的CSV文件，或运行数据生成脚本来创建示例数据。

示例CSV格式:
{','.join(required_columns)}
[数据行1]
[数据行2]
...
"""
        print(error_msg)
        raise FileNotFoundError(f"数据文件不存在: {csv_path}")
    
    try:
        df = pd.read_csv(csv_path)
        
        # 检查必需的列是否存在
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            error_msg = f"""
❌ CSV文件缺少必需的列: {', '.join(missing_columns)}

📋 当前文件列名: {', '.join(df.columns.tolist())}
📋 必需的列名: {', '.join(required_columns)}

💡 请确保CSV文件包含所有必需的列名。
"""
            print(error_msg)
            raise ValueError(f"CSV文件缺少必需的列: {missing_columns}")
        
        print(f"✅ 成功加载数据文件: {csv_path}")
        print(f"📊 数据形状: {df.shape}")
        return df
        
    except pd.errors.EmptyDataError:
        error_msg = f"❌ CSV文件为空: {csv_path}"
        print(error_msg)
        raise ValueError(error_msg)
    except Exception as e:
        error_msg = f"❌ 读取CSV文件时出错: {csv_path}\n错误信息: {str(e)}"
        print(error_msg)
        raise

def generate_sample_data(csv_path, data_generator_func, description="示例数据"):
    """
    生成示例数据并保存到CSV文件
    
    Parameters:
    -----------
    csv_path : str
        CSV文件保存路径
    data_generator_func : function
        数据生成函数
    description : str
        数据描述
    """
    print(f"🔄 生成{description}: {csv_path}")
    
    # 确保目录存在
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    # 生成数据
    df = data_generator_func()
    
    # 保存数据
    df.to_csv(csv_path, index=False)
    print(f"✅ {description}已保存: {csv_path}")
    print(f"📊 数据形状: {df.shape}")
    
    return df

def create_figure_with_style(figsize=(10, 6)):
    """创建带有科学样式的图形"""
    set_scientific_style()
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax

# 数据生成函数（用于创建示例数据）
def generate_time_series_data(n_points=50):
    """生成时间序列数据"""
    np.random.seed(42)
    time = np.linspace(0, 10, n_points)
    amplitude = np.sin(time) + 0.1 * np.random.randn(n_points)
    return pd.DataFrame({'time': time, 'amplitude': amplitude})

def generate_multiple_series_data(n_points=50):
    """生成多系列数据"""
    np.random.seed(42)
    time = np.linspace(0, 10, n_points)
    series_a = np.sin(time) + 0.1 * np.random.randn(n_points)
    series_b = np.cos(time) + 0.1 * np.random.randn(n_points)
    series_c = 0.5 * np.sin(2*time) + 0.1 * np.random.randn(n_points)
    
    return pd.DataFrame({
        'time': time,
        'series_a': series_a,
        'series_b': series_b,
        'series_c': series_c
    })

def generate_categorical_data(categories=None):
    """生成分类数据"""
    if categories is None:
        categories = ['Method A', 'Method B', 'Method C', 'Method D', 'Method E']
    
    np.random.seed(42)
    values = np.random.randint(20, 100, len(categories))
    
    return pd.DataFrame({
        'category': categories,
        'value': values
    })

def generate_scatter_data(n_points=100):
    """生成散点图数据"""
    np.random.seed(42)
    x = np.random.randn(n_points)
    y = 2 * x + np.random.randn(n_points)
    
    return pd.DataFrame({'x': x, 'y': y})

def generate_distribution_data(n_samples=1000):
    """生成分布数据"""
    np.random.seed(42)
    data = np.random.normal(0, 1, n_samples)
    
    return pd.DataFrame({'values': data}) 