"""
Kaggle Dataset Download and Setup Script
Downloads housing price data from Kaggle and organizes it properly
"""

import os
import subprocess
import sys
from pathlib import Path

def download_kaggle_dataset():
    """Download Housing dataset from Kaggle using API"""
    
    # Define paths
    project_root = Path(__file__).parent
    data_dir = project_root / "Data_analysis_Project" / "data" / "House_Price_Prediction" / "data"
    
    # Create data directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)
    
    print("🔍 Searching for Kaggle API configuration...")
    
    # Check if kaggle.json exists
    kaggle_config = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_config.exists():
        print("❌ Kaggle API key not found!")
        print(f"Expected location: {kaggle_config}")
        print("\n📝 Steps to fix:")
        print("1. Go to https://www.kaggle.com/settings/account")
        print("2. Click 'Create New API Token' - this downloads kaggle.json")
        print(f"3. Move kaggle.json to: {Path.home() / '.kaggle'}")
        print("4. Run: chmod 600 ~/.kaggle/kaggle.json (on Linux/Mac)")
        return False
    
    print("✅ Kaggle API key found!")
    
    # Check if kaggle package is installed
    try:
        import kaggle
        print("✅ kaggle-api is installed")
    except ImportError:
        print("📦 Installing kaggle-api...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle"])
        import kaggle
    
    print(f"\n📥 Downloading dataset to: {data_dir}")
    
    try:
        # Download Housing dataset (Popular housing price prediction dataset)
        # You can change the dataset name here
        dataset_name = "yasserh/housing-prices-dataset"  # Housing prices dataset
        
        print(f"Dataset: {dataset_name}")
        os.chdir(data_dir)
        
        # Download using kaggle API
        subprocess.run(
            [sys.executable, "-m", "kaggle", "datasets", "download", "-d", dataset_name, "-q"],
            check=True
        )
        
        print("✅ Download completed!")
        
        # Extract zip file if it exists
        import zipfile
        zip_files = list(data_dir.glob("*.zip"))
        if zip_files:
            for zip_file in zip_files:
                print(f"📦 Extracting {zip_file.name}...")
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    zip_ref.extractall(data_dir)
                # Remove zip file after extraction
                zip_file.unlink()
                print(f"✅ Extracted and removed {zip_file.name}")
        
        # List downloaded files
        print("\n📂 Files in data directory:")
        csv_files = list(data_dir.glob("*.csv"))
        for file in csv_files:
            size_mb = file.stat().st_size / (1024 * 1024)
            print(f"   - {file.name} ({size_mb:.2f} MB)")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading dataset: {e}")
        print("\n💡 Common issues:")
        print("1. Dataset name might be wrong - check https://www.kaggle.com/datasets")
        print("2. API key might not have permission")
        print("3. Check your internet connection")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🎯 Kaggle Dataset Download Setup")
    print("=" * 60)
    
    success = download_kaggle_dataset()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ Setup completed successfully!")
        print("=" * 60)
        print("\n📝 Next steps:")
        print("1. Update your house_price.py to use the correct CSV file")
        print("2. Run your analysis script")
    else:
        print("\n" + "=" * 60)
        print("❌ Setup failed - please fix the issues above")
        print("=" * 60)
