import sys
import os
from pathlib import Path

# Get the project root directory (where run_server.py is located)
project_root = Path(__file__).parent

# Change to the backend directory to import the main module
backend_dir = project_root / "backend"
sys.path.insert(0, str(backend_dir))
os.chdir(backend_dir)

# Now import and run the app
import uvicorn
from main import app

if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")