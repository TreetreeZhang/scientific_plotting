#!/usr/bin/env python3
"""
Scientific Plotting Suite - Main Runner
========================================

This script runs all the plotting modules to generate comprehensive
scientific visualizations based on the PDF requirements.

Chart types included:
1. Line Charts (折线图)
2. Bar Charts (柱状图) 
3. Scatter Plots (散点图)
4. Box Plots (箱线图)
5. Histograms (直方图)
6. 3D Plots (三维图)

Author: Scientific Plotting Team
Date: 2025
"""

import os
import sys
import subprocess
import time

def run_plotting_module(module_path, module_name):
    """Run a plotting module and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running {module_name}...")
    print(f"{'='*60}")
    
    try:
        # Change to the module directory
        original_dir = os.getcwd()
        module_dir = os.path.dirname(module_path)
        os.chdir(module_dir)
        
        # Run the module
        result = subprocess.run([sys.executable, os.path.basename(module_path)], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✅ {module_name} completed successfully!")
            if result.stdout:
                print("Output:", result.stdout)
        else:
            print(f"❌ {module_name} failed!")
            if result.stderr:
                print("Error:", result.stderr)
        
        # Return to original directory
        os.chdir(original_dir)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print(f"⏰ {module_name} timed out!")
        os.chdir(original_dir)
        return False
    except Exception as e:
        print(f"💥 Error running {module_name}: {str(e)}")
        os.chdir(original_dir)
        return False

def main():
    """Main function to run all plotting modules"""
    print("🎨 Scientific Plotting Suite")
    print("=" * 60)
    print("Generating all chart types based on PDF requirements...")
    print("=" * 60)
    
    # Define all plotting modules
    modules = [
        ("line_chart/code/line_chart.py", "Line Charts (折线图)"),
        ("bar_chart/code/bar_chart.py", "Bar Charts (柱状图)"),
        ("scatter_plot/code/scatter_plot.py", "Scatter Plots (散点图)"),
        ("box_plot/code/box_plot.py", "Box Plots (箱线图)"),
        ("histogram/code/histogram.py", "Histograms (直方图)"),
        ("3d_plot/code/3d_plot.py", "3D Plots (三维图)")
    ]
    
    # Track results
    results = {}
    start_time = time.time()
    
    # Run each module
    for module_path, module_name in modules:
        success = run_plotting_module(module_path, module_name)
        results[module_name] = success
        
        # Small delay between modules
        time.sleep(1)
    
    # Summary
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n{'='*60}")
    print("📊 SUMMARY REPORT")
    print(f"{'='*60}")
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Modules run: {len(modules)}")
    
    successful = sum(results.values())
    failed = len(modules) - successful
    
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    
    print(f"\n📁 Generated files are organized in:")
    print("   📂 Each chart type folder contains:")
    print("      📁 data/    - CSV data files")
    print("      📁 plot/    - PNG image files")
    print("      📁 code/    - Python source code")
    print("   📁 utils/      - Common utilities")
    
    if failed == 0:
        print(f"\n🎉 All plotting modules completed successfully!")
        print("🖼️  Check the 'plot' folders for generated images")
        print("📊 Check the 'data' folders for generated datasets")
    else:
        print(f"\n⚠️  {failed} module(s) had issues. Check the output above for details.")
    
    print(f"\n{'='*60}")
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 