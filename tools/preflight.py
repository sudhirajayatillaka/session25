from __future__ import annotations

import importlib
import platform
import subprocess
import sys


def main() -> int:
    print("\nWorkshop setup check")
    print("--------------------")
    print(f"Python: {platform.python_version()}")

    failed = False
    for package in ("fastapi", "uvicorn", "pytest", "playwright"):
        try:
            importlib.import_module(package)
            print(f"[OK] {package}")
        except ImportError:
            failed = True
            print(f"[MISSING] {package}")

    browser_check = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "--list"],
        capture_output=True,
        text=True,
        check=False,
    )
    if "chromium" in browser_check.stdout.lower():
        print("[OK] Chromium test browser")
    else:
        failed = True
        print("[MISSING] Chromium test browser")

    if failed:
        print("\nSetup is incomplete. Ask an instructor for help with the item above.")
        return 1

    print("\nSetup complete. Run check.bat 1 to test the starter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

