# Notebook Kernel Setup in VS Code/Cursor

Your Data Science Playground kernel is now registered and ready to use!

## How to Select the Kernel

When you open a `.ipynb` notebook file:

1. **Look for the kernel selector** in the top right corner of the notebook
2. **Click on it** to see available kernels
3. **Select**: `Python 3 (datascience-playground)`

Or use the Command Palette:
1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type: "Notebook: Select Kernel"
3. Choose: `Python 3 (datascience-playground)`

## Verify Installation

After selecting the kernel, you should see:
- `datascience-playground` in the kernel selector
- No import errors when running cells
- All data science libraries available

## Troubleshooting

If you don't see the kernel:
1. Make sure the virtual environment exists: `ls -la venv/`
2. Reactivate the venv: `source venv/bin/activate`
3. Reinstall the kernel: 
   ```bash
   python -m ipykernel install --user --name=datascience-playground --display-name "Python 3 (datascience-playground)"
   ```

## Quick Test

Run this in the first cell:
```python
import numpy as np
import pandas as pd
print("✅ Everything works!", np.__version__, pd.__version__)
```

You should see output without errors!

