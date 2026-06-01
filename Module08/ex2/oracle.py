import os
import sys


def load_config() -> bool:
    original_env = dict(os.environ)
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        raise RuntimeError(
            "Could not find 'dotenv' package.\n"
            "To install: 'pip install python-dotenv'"
        )
    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    success = True
    print("Configuration loaded:")
    if mode not in ("production", "development"):
        print("[WARNING] MATRIX_MODE missing. Must be 'development' "
              "or 'production'.\n"
              "Defaulting to 'development'\n")
        mode = "development"
    print(f"Mode: {mode}")
    if mode == "development":
        if not db:
            print("[WARNING] DATABASE_URL not found. Using default: local")
            db = "local"
        print(f"Database: Connected to {db} instance")
        if not api:
            print("[WARNING] API_KEY not found. Using default: Authenticated")
            api = "Authenticated"
        print("API Access: Authenticated")
        if not log:
            print("[WARNING] LOG_LEVEL not found. Using default: DEBUG")
            log = "DEBUG"
        print(f"Log Level: {log}")
        if not zion:
            print("[WARNING] ZION_ENDPOINT not found. Using default: Online")
            zion = "Online"
        print(f"Zion Network: {zion}")
    elif mode == "production":
        if not db:
            print("[ERROR] DATABASE_URL missing in production!")
            success = False
        else:
            print(f"Database: Connected to {db} instance")
        if not api:
            print("[ERROR] API_KEY missing in production!")
            success = False
        else:
            print("API Access: Authenticated")
        if not log:
            print("[WARNING] LOG_LEVEL not found. Using default: DEBUG")
            log = "DEBUG"
        print(f"Log Level: {log}")
        if not zion:
            print("[ERROR] ZION_ENDPOINT missing in production!")
            success = False
        else:
            print(f"Zion Network: {zion}")
    print()
    print("Environment security check:")
    if api:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] No API_KEY detected")
    required = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": db,
        "API_KEY": api,
        "LOG_LEVEL": log,
        "ZION_ENDPOINT": zion
    }
    missing = []
    for key in required:
        if key not in os.environ:
            missing.append(key)
    if os.path.exists(".env") and not missing:
        print("[OK] .env file properly configured")
    elif not os.path.exists(".env"):
        print("[WARNING] .env file missing")
    else:
        print(f"[WARNING] Missing config values: {', '.join(missing)}")
    check_overrides = []
    for key in ["MATRIX_MODE", "DATABASE_URL",
                "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]:
        if key in original_env:
            check_overrides.append(key)
    if check_overrides:
        print(f"[INFO] Environment overrides detected: "
              f"{', '.join(check_overrides)}")
    else:
        print("[OK] Production overrides available")
    return success


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(
            "It's recommended to use a virtual environment "
            "before running this program.\n"
            "To enter the construct, run:\n"
            "python3 -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\n"
            "Then run this program again."
        )
        sys.exit(1)
    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        if load_config():
            print("\nThe Oracle sees all configurations.")
        else:
            print("\nThe Oracle cannot see all configurations")
    except Exception as e:
        print(f"ERROR: {e}")
