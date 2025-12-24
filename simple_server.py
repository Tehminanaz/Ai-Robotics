import sys
from pathlib import Path

# Add the backend directory to the Python path
project_root = Path(__file__).parent
backend_dir = project_root / "backend"
sys.path.insert(0, str(backend_dir))

# Import the app from the backend directory
import uvicorn
from backend.main import app

if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")