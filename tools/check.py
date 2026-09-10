from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys


LEVEL_NAMES = {
    1: "Setup and page",
    2: "HTML + JavaScript",
    3: "Form validation",
    4: "GET /hello",
    5: "POST /login",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one workshop checkpoint or the complete suite."
    )
    parser.add_argument("level", choices=["1", "2", "3", "4", "5", "all"])
    parser.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
        help=argparse.SUPPRESS,
    )
    return parser.parse_args()


def run_level(level: int, project: Path, repo_root: Path) -> bool:
    env = os.environ.copy()
    env["WEBDEV_PROJECT_ROOT"] = str(project.resolve())
    env["PYTHONPATH"] = str(project.resolve())

    print(f"\nLEVEL {level}: {LEVEL_NAMES[level]}", flush=True)
    print("=" * (9 + len(LEVEL_NAMES[level])), flush=True)
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(repo_root / "tests"),
            "-m",
            f"level{level}",
            "-q",
            "--tb=short",
            "--disable-warnings",
            "--screenshot=only-on-failure",
            "--tracing=retain-on-failure",
            "--output",
            str(project / "test-results" / f"level-{level}"),
        ],
        cwd=project,
        env=env,
        check=False,
    )
    return result.returncode == 0


def write_github_summary(results: dict[int, bool]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    rows = ["## Web development checkpoints", "", "| Level | Topic | Result |", "|---|---|---|"]
    for level, passed in results.items():
        result = "✅ Passed" if passed else "❌ Needs work"
        rows.append(f"| {level} | {LEVEL_NAMES[level]} | {result} |")
    with Path(summary_path).open("a", encoding="utf-8") as summary:
        summary.write("\n".join(rows) + "\n")


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    project = args.project.resolve()

    required = (project / "main.py", project / "static" / "index.html")
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        print("[ERROR] This does not look like the workshop project.")
        for path in missing:
            print(f"  Missing: {path}")
        return 2

    levels = list(LEVEL_NAMES) if args.level == "all" else [int(args.level)]
    results = {level: run_level(level, project, repo_root) for level in levels}
    write_github_summary(results)

    print("\nCHECKPOINT SUMMARY")
    print("------------------")
    for level, passed in results.items():
        icon = "PASS" if passed else "TODO"
        print(f"[{icon}] Level {level}: {LEVEL_NAMES[level]}")

    if all(results.values()):
        print("\nGreat work — every selected checkpoint passed!")
        return 0
    print("\nRead the first failure above, make one small change, and run this check again.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
