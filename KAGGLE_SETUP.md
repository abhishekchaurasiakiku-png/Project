# Kaggle Dataset Setup Guide 🎯

## Quick Start

### Step 1: Verify Kaggle API is Configured ✅
Your Kaggle API key should be at:
```
C:\Users\Abhishek\.kaggle\kaggle.json
```

If you already set it up in PowerShell, you're good!

### Step 2: Install Required Package
```powershell
pip install kaggle
```

### Step 3: Run the Download Script
```powershell
cd "C:\Users\Abhishek\OneDrive\Desktop\Intern_project"
python download_kaggle_data.py
```

This will:
- ✅ Verify your Kaggle API key
- 📥 Download the Housing dataset
- 📦 Extract the CSV files
- 📂 Organize them in the correct folder

### Step 4: Verify the Setup
```powershell
cd "Data_analysis_Project\data\House_Price_Prediction"
python house_price.py
```

---

## Dataset Information 📊

**Dataset**: Housing Prices Dataset  
**Location**: `/data/House_Price_Prediction/data/`  
**File**: `Housing.csv` (or similar)

The dataset contains:
- House prices and features
- Multiple columns for analysis
- Suitable for regression analysis

---

## Troubleshooting 🔧

### Issue: "Kaggle API key not found"
**Solution:**
1. Go to https://www.kaggle.com/settings/account
2. Click "Create New API Token"
3. This downloads `kaggle.json`
4. Move it to `C:\Users\Abhishek\.kaggle\`

### Issue: "Dataset not found or permission denied"
**Solution:**
- Check dataset name in `download_kaggle_data.py`
- Try a different dataset from https://www.kaggle.com/datasets
- Update line in script: `dataset_name = "new-dataset-name"`

### Issue: "SSL certificate error"
**Solution:**
```powershell
pip install --upgrade certifi
```

---

## Available Dataset Options 🔄

If the housing dataset doesn't work, try one of these:

1. **House Price Prediction**
   ```
   dataset_name = "harlfoxem/housesalesprediction"
   ```

2. **Boston Housing**
   ```
   dataset_name = "prasadj9/housing-prices-dataset"
   ```

3. **Real Estate Price Prediction**
   ```
   dataset_name = "quantbruce/real-estate-price-prediction"
   ```

---

## Project Structure 📁

```
Data_analysis_Project/
├── data/
│   ├── sample_data.csv
│   └── House_Price_Prediction/
│       ├── data/              ← CSV files go here ✅
│       ├── models/            ← Trained models
│       ├── notebooks/         ← Jupyter notebooks
│       └── house_price.py     ← Main analysis script
└── analysis.py
```

---

## Next Steps 🚀

1. ✅ Download the dataset using the script
2. ✅ Run `house_price.py` to verify
3. ✅ Start your analysis and modeling!

Good luck! 🎉
