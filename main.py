"""Reflexion Self-Correction Loop"""

def self_correct(attempt, test_fn):
    if test_fn(attempt):
        return attempt, "Success on first turn"
    corrected = attempt + 1 # simulated fix
    return corrected, "Reflexion corrected after failing initial test"

if __name__ == "__main__":
    print("[RUN] Reflexion Self-Correction Loop...")
    res, msg = self_correct(attempt=0, test_fn=lambda x: x > 0)
    print(f"[OK] Output: {res} ({msg})")
