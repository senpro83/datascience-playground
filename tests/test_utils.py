"""
Unit tests for utility functions
"""

import unittest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from utils import load_sample_data, display_data_info, setup_plotting_style


class TestUtils(unittest.TestCase):
    """Test cases for utility functions"""

    def test_load_sample_data(self):
        """Test that sample data is loaded correctly"""
        df = load_sample_data()
        
        # Check that it returns a DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        
        # Check shape
        self.assertEqual(df.shape[0], 1000)
        
        # Check columns
        expected_columns = ['age', 'income', 'education_years', 'satisfaction']
        self.assertListEqual(list(df.columns), expected_columns)
        
        # Check data types
        self.assertTrue(df['age'].dtype in [np.int32, np.int64, int])
        self.assertTrue(df['education_years'].dtype in [np.int32, np.int64, int])

    def test_display_data_info(self):
        """Test that display function works without errors"""
        df = load_sample_data()
        
        # This should not raise an exception
        try:
            display_data_info(df)
        except Exception as e:
            self.fail(f"display_data_info raised {type(e).__name__}: {e}")

    def test_setup_plotting_style(self):
        """Test that plotting style setup works"""
        try:
            setup_plotting_style()
        except Exception as e:
            self.fail(f"setup_plotting_style raised {type(e).__name__}: {e}")


if __name__ == '__main__':
    unittest.main()

