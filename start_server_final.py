import subprocess
import sys
from pathlib import Path

def start_server():
    # Get the backend directory
    project_root = Path(__file__).parent
    backend_dir = project_root / "backend"

    # Run uvicorn from the backend directory with the proper module path
    cmd = [
        sys.executable, "-c",
        f"import sys; sys.path.insert(0, '{str(project_root)}'); "
        f"import uvicorn; "
        f"from backend.main import app; "
        f"uvicorn.run(app, host='0.0.0.0', port=8000, log_level='info')"
    ]

    print("Starting server on http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")

    try:
        result = subprocess.run(cmd, cwd=backend_dir, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        return e.returncode
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        return 0

if __name__ == "__main__":
    exit_code = start_server()
    sys.exit(exit_code)