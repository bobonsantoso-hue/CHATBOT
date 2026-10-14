@echo off
echo ========================================
echo  StudyBuddy Setup Script
echo ========================================
echo.

echo [1/3] Installing dependencies...
pip install -r requirements.txt
echo.

echo [2/3] Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo .env file created! Please edit it and add your Gemini API key.
    echo Get your free API key from: https://makersuite.google.com/app/apikey
) else (
    echo .env file already exists.
)
echo.

echo [3/3] Setup complete!
echo.
echo ========================================
echo  Next Steps:
echo ========================================
echo 1. Edit .env file and add your Gemini API key
echo 2. Run: streamlit run app.py
echo 3. Open browser at: http://localhost:8501
echo.
echo Happy Learning with StudyBuddy! 
echo ========================================
pause
