# Project Dependencies

## Customer Personality Segmentation Project

The following additional dependencies are required for the Customer Personality Segmentation project:

### Installation

All dependencies can be installed with:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Additional Libraries for Customer Personality Project

- **yellowbrick>=1.5.0**: Machine learning visualizations and model diagnostics
  - Used for: KElbowVisualizer, SilhouetteVisualizer
  - Purpose: Visual clustering analysis and elbow method plots

### Core Dependencies

All core data science libraries are included in requirements.txt:
- NumPy, Pandas, SciPy
- Matplotlib, Seaborn, Plotly
- Scikit-learn
- Jupyter, ipykernel
- And more...

## Running the Notebooks

Make sure your virtual environment is activated:
```bash
source venv/bin/activate
```

Then select the `Python 3 (datascience-playground)` kernel in your notebook.

## Troubleshooting

If you encounter `ModuleNotFoundError`:
1. Check that the virtual environment is activated
2. Verify the kernel is using the correct Python environment
3. Run: `pip install -r requirements.txt`

