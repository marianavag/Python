def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")
    vault = None
    try:
        vault = open(file_name, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(vault.read())
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(
            "ERROR: Storage vault not found. Run data generator first.\n"
            "Remember: a good archivist always checks if the vault exists\n"
            "before attempting access. Trying to read non-existent files is\n"
            "like trying to open a door that isn't there—it never ends well."
        )
    except Exception:
        print("ERROR: An unexpected corruption occurred.")
    finally:
        if vault is not None:
            vault.close()


if __name__ == "__main__":
    ft_ancient_text()
