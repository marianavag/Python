def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]
    arch_creation = None
    try:
        arch_creation = open(file_name, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for entry in entries:
            print(entry)
            arch_creation.write(f"{entry}\n")
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except OSError:
        print("Error: There was an unexpected anomaly.")
    finally:
        if arch_creation is not None:
            arch_creation.close()


if __name__ == "__main__":
    ft_archive_creation()
