import sys
from typing import Dict, Optional
from importlib.metadata import version, PackageNotFoundError


def compare_dependencies(installed_vers: Dict[str, Optional[str]],
                         descriptions: Dict[str, str]) -> bool:
    print("Comparing dependency management (pip vs Poetry)...\n")
    pip = {}
    poetry = {}
    try:
        with open("requirements.txt", "r") as pip_file:
            for line in pip_file:
                line = line.strip()
                if "==" in line:
                    name, pip_version = line.split("==")
                    pip[name] = pip_version
    except FileNotFoundError:
        pass
    try:
        in_dependencies = False
        with open("pyproject.toml", "r") as poetry_file:
            for line in poetry_file:
                line = line.strip()
                if line == "[tool.poetry.dependencies]":
                    in_dependencies = True
                    continue
                if in_dependencies and line.startswith("["):
                    in_dependencies = False
                if in_dependencies and line:
                    parts = line.split("=")
                    if len(parts) == 2:
                        name = parts[0].strip().replace('"', '')
                        poe_vers = parts[1].strip().strip('"').replace('^', '')
                        poetry[name] = poe_vers
    except FileNotFoundError:
        pass
    is_poetry = bool(poetry)
    current_deps = poetry if is_poetry else pip
    if not current_deps:
        print("[!] Error: No dependency file found "
              "(requirements.txt or pyproject.toml).")
        print("Execution aborted.\n")
        return False
    print(f"CURRENT ENVIRONMENT - {'POETRY' if is_poetry else 'PIP'}:")
    print("Checking dependencies:")
    all_ok = True
    for pkg, req_version in current_deps.items():
        real_version = installed_vers.get(pkg)
        desc = descriptions.get(pkg, "")
        if real_version is None:
            status = "[Missing]"
            all_ok = False
            print(f"{status} {pkg}: Required = {req_version} |"
                  f" Installed = {real_version}")
        elif req_version == real_version:
            status = "[OK]"
            print(f"{status} {pkg} ({real_version}) - {desc}")
        else:
            status = "[Mismatch]"
            all_ok = False
            print(f"{status} {pkg}: Required = {req_version} |"
                  f" Installed = {real_version}")
    if not all_ok:
        print("\n[!] Missing dependencies. Please install them.")
        if is_poetry:
            print("For poetry: 'poetry install'\n")
        else:
            print("For pip: 'pip install -r requirements.txt'\n")
    else:
        print("\nAll dependencies met!\n")
    return all_ok


def matrix_organiser() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    print("Analyzing Matrix data...")
    matrix_data = np.random.randint(1, 1001, size=(200, 2))
    print("Processing 1000 data points...")
    df = pd.DataFrame(data=matrix_data, columns=["Size_KB", "Speed_Mbps"])
    df['Latency'] = df['Size_KB'] / df['Speed_Mbps']
    print("Generating visualization...\n")
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Size_KB'], df['Latency'], color='green', alpha=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title("Performance Analysis: Matrix Data Stream")
    plt.xlabel("Size (KB)")
    plt.ylabel("Latency (SECs)")
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")
    plt.show()


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(
            "It's recommended to use a virtual environment before running this program.\n"
            "To enter the construct, run:\n"
            "python3 -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\n"
            "Then run this program again."
        )
        sys.exit(1)
    descriptions = {
        "numpy": "Numerical computation ready",
        "pandas": "Data manipulation ready",
        "matplotlib": "Visualization ready"
    }
    installed_vers: Dict[str, Optional[str]] = {}
    for pkg in descriptions.keys():
        try:
            installed_vers[pkg] = version(pkg)
        except PackageNotFoundError:
            installed_vers[pkg] = None
    print("\nLOADING STATUS: Loading programs...\n")
    if compare_dependencies(installed_vers, descriptions):
        matrix_organiser()
    else:
        print("Matrix simulation could not start.")
