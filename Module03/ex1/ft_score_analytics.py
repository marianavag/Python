import sys


def ft_score_analytics() -> None:
    """Analyse player scores provided via command line."""
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(f"No scores provided. Usage: python3 "
              f"{sys.argv[0]} <score1> <score2> ...")
        return
    scores = []
    user_args = sys.argv[1:]
    for arg in user_args:
        try:
            scores.append(int(arg))
        except ValueError:
            print("Error: scores must be numeric values.")
            return
    print(
        f"Scores processed: {scores}\n"
        f"Total players: {len(scores)}\n"
        f"Total score: {sum(scores)}\n"
        f"Average score: {sum(scores)/len(scores)}\n"
        f"High score: {max(scores)}\n"
        f"Low score: {min(scores)}\n"
        f"Score range: {max(scores) - min(scores)}\n"
    )


if __name__ == "__main__":
    ft_score_analytics()
