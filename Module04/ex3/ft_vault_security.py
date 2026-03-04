def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    file_name = "classified_data.txt"
    s_file = "security_protocols.txt"
    s_entry = "[CLASSIFIED] New security protocols archived"
    try:
        with open(file_name, "r") as vault:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(vault.read())
        with open(s_file, "w") as sec:
            print("\nSECURE PRESERVATION:")
            print(s_entry)
            sec.write(s_entry)
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print(
            f"ERROR: Vault file '{file_name}' not found. "
            "Run data generator first.\n"
            "Remember: secure archivists always verify vaults before access."
        )
    except OSError:
        print("Error: An unexpected system anomaly "
              "occurred during vault operations.")


if __name__ == "__main__":
    ft_vault_security()
