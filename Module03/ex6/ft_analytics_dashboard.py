def list_comp(game_data: list) -> None:
    """Demonstrate list comprehensions for filter and transform player data."""
    print("=== List Comprehension Examples ===")
    try:
        high_scorers = [
            player["name"]
            for player in game_data
            if player["score"] > 2000
        ]
        scores_doubled = [
            player["score"] * 2
            for player in game_data
        ]
        active_players = [
            player["name"]
            for player in game_data
            if player["active"]
        ]
        print(f"High scorers (>2000): {high_scorers}")
        print(f"Scores doubled: {scores_doubled}")
        print(f"Active players: {active_players}")
    except Exception:
        print("Error while generating the List Comprehension Examples")


def dict_comp(game_data: list) -> None:
    """Demonstrate dict comprehensions for building mapping and aggregation."""
    print("\n=== Dict Comprehension Examples ===")
    try:
        player_scores = {
            player["name"]: player["score"]
            for player in game_data
            if player["active"]
        }
        score_cat = {
            "high": sum(
                1 for player in game_data
                if player["score"] >= 2000),
            "medium": sum(
                1 for player in game_data
                if 2000 <= player["score"] < 2200),
            "low": sum(
                1 for player in game_data
                if player["score"] < 2000)
        }
        ach_count = {
            player["name"]: len(player["achievements"])
            for player in game_data
            if player["active"]
        }
        print(f"Player scores: {player_scores}")
        print(f"Score categories: {score_cat}")
        print(f"Achievement counts: {ach_count}")
    except Exception:
        print("Error while generating the Dict Comprehension Examples")


def set_comp(game_data: list) -> None:
    """Demonstrate set comprehensions for extracting unique values."""
    print("\n=== Set Comprehension Examples ===")
    try:
        uni_players = sorted({
            player["name"]
            for player in game_data
        })
        uni_ach = {
            achievement
            for player in game_data
            for achievement in player["achievements"]
        }
        uni_region = {
            player["region"]
            for player in game_data
        }
        print(f"Unique players: {uni_players}")
        print(f"Unique achievements: {uni_ach}")
        print(f"Active regions: {uni_region}")
    except Exception:
        print("Error while generating the Set Comprehension Examples")


def comb_analysis(game_data) -> None:
    """Combine comprehensions to compute summary analytics."""
    print("\n=== Combined Analysis ===")
    try:
        total_players = len(game_data)
        all_scores = [
            player["score"]
            for player in game_data
        ]
        average_score = sum(all_scores) / len(all_scores)
        uniq_ach = {
            achievement
            for player in game_data
            for achievement in player["achievements"]
        }
        total_uniq_ach = len(uniq_ach)
        top_score = max(all_scores)
        top_player = [
            player
            for player in game_data
            if player["score"] == top_score
        ]
        winner = top_player[0]
        print(f"Total players: {total_players}")
        print(f"Total unique achievements: {total_uniq_ach}")
        print(f"Average score: {average_score}")
        print(f"Top performer: {winner['name']} ({winner['score']} points, "
              f"{len(winner['achievements'])} achievements)")
    except Exception:
        print("Error while generating the Combined Analysis")


def ft_analytics_dashboard() -> None:
    """Run analytics dashboard showcasing list, dict & set comprehensions."""
    print("=== Game Analytics Dashboard ===\n")
    game_data = [
        {
            "name": "alice",
            "score": 2300,
            "region": "north",
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "treasure_hunter", "speed_demon"],
            "active": True
        },
        {
            "name": "bob",
            "score": 1800,
            "region": "east",
            "achievements": ["first_kill", "level_10", "collector"],
            "active": True
        },
        {
            "name": "charlie",
            "score": 2150,
            "region": "north",
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "monster_hunter", "treasure_hunter",
                             "speed_demon", "map_explorer"],
            "active": True
        },
        {
            "name": "diana",
            "score": 2050,
            "region": "central",
            "achievements": ["level_10", "first_kill"],
            "active": False
        },
    ]
    list_comp(game_data)
    dict_comp(game_data)
    set_comp(game_data)
    comb_analysis(game_data)


if __name__ == "__main__":
    ft_analytics_dashboard()
