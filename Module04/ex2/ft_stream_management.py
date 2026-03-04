import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        arch_id = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")
        print(f"\n[STANDARD] Archive status from {arch_id}: {status}",
              file=sys.stdout)
        print("[ALERT] System diagnostic: Communication channels verified",
              file=sys.stderr)
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print("\nThree-channel communication test successful.")
    except Exception as e:
        print(f"[ERROR] Communication failure: {e}", file=sys.stderr)


if __name__ == "__main__":
    ft_stream_management()
