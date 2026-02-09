def ft_achievement_tracker() -> None:
    """Track and analyse player achievements."""
    print("=== Achievement Tracker System ===\n")
    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                   'perfectionist'])
    print(
        f"Player alice achievements: {alice}\n"
        f"Player bob achievements: {bob}\n"
        f"Player charlie achievements: {charlie}\n"
    )
    print("=== Achievement Analytics ===")
    all_uniq_ach = alice.union(bob, charlie)
    print(
        f"All unique achievements: {all_uniq_ach}\n"
        f"Total unique achievements: {len(all_uniq_ach)}\n"
    )
    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")
    rare_alice = alice.difference(bob, charlie)
    rare_bob = bob.difference(alice, charlie)
    rare_charlie = charlie.difference(alice, bob)
    rare_ach = rare_alice.union(rare_bob, rare_charlie)
    print(
        f"Rare achievements (1 player): {rare_ach}\n"
        f"\nAlice vs Bob common: {alice.intersection(bob)}\n"
        f"Alice unique: {alice.difference(bob)}\n"
        f"Bob unique: {bob.difference(alice)}"
    )


if __name__ == "__main__":
    ft_achievement_tracker()
