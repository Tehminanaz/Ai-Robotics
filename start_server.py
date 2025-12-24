import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Add the backend directory to the Python path
backend_dir = project_root / "backend"
sys.path.insert(0, str(backend_dir))

# Change to the backend directory
os.chdir(backend_dir)

def run_server():
    try:
        import uvicorn
        # Run the FastAPI app
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=False  # Set to False for production
        )
    except ImportError:
        print("Error: uvicorn is not installed. Please install it with: pip install uvicorn")
    except Exception as e:
        print(f"Error running the server: {e}")

if __name__ == "__main__":
    run_server()