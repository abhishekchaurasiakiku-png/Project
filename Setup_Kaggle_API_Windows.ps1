# Kaggle API Setup Script for Windows (PowerShell)
# This script helps you set up the Kaggle API properly

Write-Host "=" * 60
Write-Host "🎯 Kaggle API Setup for Windows" -ForegroundColor Cyan
Write-Host "=" * 60
Write-Host ""

# Step 1: Check if .kaggle directory exists
$kaggleDir = "$env:USERPROFILE\.kaggle"

if (Test-Path $kaggleDir) {
    Write-Host "✅ .kaggle directory exists at: $kaggleDir" -ForegroundColor Green
    
    # Check for kaggle.json
    $kaggleJsonPath = "$kaggleDir\kaggle.json"
    if (Test-Path $kaggleJsonPath) {
        Write-Host "✅ kaggle.json found!" -ForegroundColor Green
        Write-Host "   Location: $kaggleJsonPath" -ForegroundColor Green
    } else {
        Write-Host "❌ kaggle.json not found in .kaggle directory" -ForegroundColor Red
        Write-Host "   You need to download it from Kaggle" -ForegroundColor Yellow
    }
} else {
    Write-Host "📁 Creating .kaggle directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $kaggleDir -Force | Out-Null
    Write-Host "✅ Created: $kaggleDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "📝 SETUP INSTRUCTIONS:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1️⃣  Go to: https://www.kaggle.com/settings/account" -ForegroundColor Yellow
Write-Host "   (You must be logged in to Kaggle)" -ForegroundColor DarkGray
Write-Host ""
Write-Host "2️⃣  Click: 'Create New API Token'" -ForegroundColor Yellow
Write-Host "   (This will download 'kaggle.json')" -ForegroundColor DarkGray
Write-Host ""
Write-Host "3️⃣  Move the downloaded kaggle.json to:" -ForegroundColor Yellow
Write-Host "   $kaggleDir" -ForegroundColor Cyan
Write-Host ""
Write-Host "4️⃣  Verify setup by running:" -ForegroundColor Yellow
Write-Host "   kaggle datasets list" -ForegroundColor Cyan
Write-Host ""
Write-Host "=" * 60
Write-Host "📦 Installing/Verifying kaggle-api package..." -ForegroundColor Cyan
Write-Host "=" * 60

# Check if kaggle is installed
try {
    $kaggleVersion = pip show kaggle | Select-String "Version:"
    Write-Host "✅ kaggle-api is already installed:" -ForegroundColor Green
    Write-Host "   $kaggleVersion" -ForegroundColor DarkGray
} catch {
    Write-Host "📥 Installing kaggle-api..." -ForegroundColor Yellow
    pip install kaggle
    Write-Host "✅ kaggle-api installed successfully" -ForegroundColor Green
}

Write-Host ""
Write-Host "=" * 60
Write-Host "🚀 NEXT STEPS:" -ForegroundColor Cyan
Write-Host "=" * 60
Write-Host ""
Write-Host "1. Download kaggle.json from https://www.kaggle.com/settings/account"
Write-Host "2. Place it in: $kaggleDir"
Write-Host "3. Run: python download_kaggle_data.py"
Write-Host ""
Write-Host "Once kaggle.json is in place, you can use these commands:"
Write-Host ""
Write-Host "  kaggle datasets list                    # See available datasets"
Write-Host "  kaggle datasets search housing          # Search for housing datasets"
Write-Host "  kaggle datasets download -d USERNAME/DATASET  # Download a dataset"
Write-Host ""
Write-Host "=" * 60
