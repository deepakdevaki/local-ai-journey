
---

## 📄 2. `setup.bat`

```bat
@echo off
echo 📦 Setting up Local AI Environment...

python -m venv ai_env
call ai_env\Scripts\activate

pip install --upgrade pip
pip install tensorflow scikit-learn matplotlib pandas numpy ollama chromadb sentence-transformers pillow

echo.
echo ✅ Setup complete!
echo Run: python run_hub.py
pause