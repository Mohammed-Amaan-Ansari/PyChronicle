from pathlib import Path
from datetime import datetime


SESSIONS_DIR = Path("sessions")
SESSIONS_DIR.mkdir(exist_ok=True)


def save_session_record(session_id: str, script_name: str):
    """
    Save a session record.
    """

    session_file = SESSIONS_DIR / f"{session_id}.txt"

    with open(session_file, "w", encoding="utf-8") as file:
        file.write(f"Session ID : {session_id}\n")
        file.write(f"Script     : {script_name}\n")
        file.write(f"Created    : {datetime.now().isoformat()}\n")


def list_sessions():
    """
    Return all saved session records.
    """

    sessions = []

    for file in SESSIONS_DIR.glob("*.txt"):
        sessions.append(file.stem)

    return sorted(sessions)