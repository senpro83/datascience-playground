# Kernel Troubleshooting Guide

## Issue: ModuleNotFoundError when running notebooks

If you see `ModuleNotFoundError: No module named 'yellowbrick'` or similar errors, follow these steps:

### Step 1: Verify Kernel Selection

Make sure you've selected the correct kernel:
1. Look at the top-right corner of your notebook
2. Click on the kernel selector
3. Choose: **"Python 3 (datascience-playground)"**

### Step 2: Restart the Kernel

After changing the kernel, you MUST restart it:
1. Go to: `Kernel` → `Restart Kernel`
2. Or use the toolbar: Click the restart button (🔄)
3. Re-run your cells

### Step 3: Verify Installation

Check that yellowbrick is installed in the venv:
```bash
source venv/bin/activate
python -c "import yellowbrick; print('✅ OK')"
```

### Step 4: Reinstall Kernel (if needed)

If the kernel still doesn't work:
```bash
cd datascience-playground
source venv/bin/activate
python -m ipykernel install --user --name=datascience-playground --display-name "Python 3 (datascience-playground)" --force
```

Then restart your notebook kernel.

### Step 5: Verify Package Installation

Make sure all packages are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Fix Checklist

- [ ] Kernel is "Python 3 (datascience-playground)"
- [ ] Kernel has been restarted after selection
- [ ] Virtual environment is activated
- [ ] All packages installed: `pip install -r requirements.txt`
- [ ] Notebook cells re-run from the top

## Common Mistakes

❌ **Don't**: Run cells with the wrong kernel selected
❌ **Don't**: Forget to restart the kernel after changing it
❌ **Don't**: Use system Python instead of venv Python

✅ **Do**: Always select the correct kernel first
✅ **Do**: Restart kernel after selection
✅ **Do**: Run all cells from the top after restart
