# UNO Live Table

Vercel-ready Flask UNO web game based on the supplied Python rules.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python api/index.py
```

Open http://127.0.0.1:5000

## Deploy to Vercel
1. Push this folder to GitHub.
2. Import the repository into Vercel.
3. Vercel detects `vercel.json` and the Python API.
4. Deploy.

The browser handles presentation/animation; the Flask endpoint applies the game rules.
