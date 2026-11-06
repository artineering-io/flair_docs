"""Build and serve the Flair docs locally.

Asks whether to serve a full build with search, or the live-reloading dev server.
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def npm(*args: str) -> None:
    """Runs an npm command in the docs root; exits if it fails."""
    # shutil.which finds npm.cmd on Windows, which subprocess can't run from a bare "npm".
    exe = shutil.which("npm")
    if exe is None:
        sys.exit("npm not found. Install Node.js LTS, then open a new terminal.")
    result = subprocess.run([exe, *args], cwd=ROOT)
    if result.returncode != 0:
        sys.exit(result.returncode)


def ask_search() -> bool:
    """Asks whether to serve the full build with search."""
    while True:
        answer = input("Serve with search (full build, no live reload)? [y/n]: ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"


def main() -> None:
    if not (ROOT / "node_modules").is_dir():
        print("Installing dependencies...")
        npm("install")
    # Starlight only enables Pagefind search in production builds, so testing search
    # needs build + preview. The dev server reloads on save but has no search.
    if ask_search():
        npm("run", "build")
        npm("run", "preview")
    else:
        npm("run", "dev")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+C is the normal way to stop the server, so skip the traceback.
        pass
