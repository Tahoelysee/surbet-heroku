import time

def detect_surebets():
    # Extrait simulé : exemple de détection
    return [
        {"match": "Team A vs Team B", "sport": "Football", "roi": 24.5},
        {"match": "Player X vs Player Y", "sport": "Tennis", "roi": 22.1}
    ]

if __name__ == "__main__":
    while True:
        surebets = detect_surebets()
        for bet in surebets:
            print(f"[SUREBET] {bet['match']} - {bet['sport']} - ROI: {bet['roi']}%")
        time.sleep(60)
