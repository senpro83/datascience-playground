# Data Science Playground 🎯

A comprehensive Python project for data science experimentation and learning. This playground provides a structured environment with essential tools, utilities, and examples to help you explore, analyze, and model data effectively.

## 📁 Project Structure

```
datascience-playground/
│
├── data/                  # Store your datasets here
├── notebooks/             # Jupyter notebooks for analysis
│   └── getting_started.ipynb
├── plots/                 # Generated visualizations
├── src/                   # Python source code
│   ├── __init__.py
│   └── utils.py          # Utility functions
├── tests/                 # Unit tests
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── setup.py              # Package setup
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd datascience-playground
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package in development mode:**
   ```bash
   pip install -e .
   ```

### Running Jupyter Notebooks

1. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Open the getting started notebook:**
   - Navigate to `notebooks/getting_started.ipynb`
   - Run the cells to see examples of data exploration, visualization, and modeling

## 📚 Features

### Core Libraries Included

- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **Plotly**: Interactive visualizations
- **Scikit-learn**: Machine learning algorithms
- **SciPy**: Scientific computing
- **Statsmodels**: Statistical modeling

### Utility Functions

The project includes helper functions in `src/utils.py`:

- `load_sample_data()`: Generate sample datasets for experimentation
- `setup_plotting_style()`: Configure matplotlib and seaborn styling
- `display_data_info()`: Comprehensive data overview

## 🎓 Example Workflow

1. **Load your data** or use the sample data generator
2. **Explore** with descriptive statistics and info display
3. **Visualize** distributions, correlations, and relationships
4. **Model** using machine learning algorithms
5. **Evaluate** model performance and insights

## 📝 Usage Examples

### Using Utility Functions

```python
from src.utils import load_sample_data, setup_plotting_style, display_data_info
import matplotlib.pyplot as plt
import pandas as pd

# Setup plotting
setup_plotting_style()

# Load data
df = load_sample_data()

# Display information
display_data_info(df)
```

### Creating Visualizations

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure
plt.figure(figsize=(10, 6))
plt.hist(df['column_name'], bins=30, edgecolor='black')
plt.title('Distribution Plot')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Machine Learning

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Prepare data
X = df[['feature1', 'feature2']]
y = df['target']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
```

## 🔧 Customization

- **Add your own datasets** in the `data/` folder
- **Create new notebooks** for different experiments
- **Extend utility functions** in `src/utils.py`
- **Add new models** and analysis techniques

## 📊 Project Goals

- Learn and experiment with data science tools
- Build reusable analysis workflows
- Explore different datasets and techniques
- Share insights through visualizations
- Develop machine learning models

## 🤝 Contributing

Feel free to:
- Add more utility functions
- Create additional notebooks
- Improve documentation
- Share interesting findings

## 📄 License

This is a learning project. Feel free to use and modify as needed.

## 🎯 Next Steps

1. Run the `getting_started.ipynb` notebook
2. Explore the sample data
3. Create your own analysis notebooks
4. Load and analyze your own datasets
5. Experiment with different models and techniques

**Happy Data Exploring! 🚀**

