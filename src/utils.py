"""
Utility functions for data science playground
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_sample_data():
    """
    Generate sample data for experimentation
    
    Returns:
        pd.DataFrame: Sample dataset
    """
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'age': np.random.randint(18, 80, n_samples),
        'income': np.random.normal(50000, 15000, n_samples),
        'education_years': np.random.randint(12, 20, n_samples),
        'satisfaction': np.random.randint(1, 11, n_samples)
    }
    
    return pd.DataFrame(data)


def setup_plotting_style():
    """
    Set up matplotlib and seaborn plotting style
    """
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 6)
    print("Plotting style configured!")


def display_data_info(df):
    """
    Display comprehensive information about a DataFrame
    
    Args:
        df (pd.DataFrame): The dataframe to analyze
    """
    print("=" * 60)
    print("DATA OVERVIEW")
    print("=" * 60)
    print(f"Shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("\n" + "-" * 60)
    print("COLUMN INFO")
    print("-" * 60)
    print(df.info())
    print("\n" + "-" * 60)
    print("STATISTICAL SUMMARY")
    print("-" * 60)
    print(df.describe())
    print("\n" + "-" * 60)
    print("NULL VALUES")
    print("-" * 60)
    print(df.isnull().sum())


if __name__ == "__main__":
    # Example usage
    df = load_sample_data()
    display_data_info(df)
    setup_plotting_style()

