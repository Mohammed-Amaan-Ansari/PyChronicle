import uuid
from datetime import datetime


class SessionManager:
    """
    Generates unique tracing session information.
    """

    def __init__(self):
        self.session_id = str(uuid.uuid4())[:8]
        self.started_at = datetime.now()

    def get_session_info(self):
        return {
            "session_id": self.session_id,
            "started_at": self.started_at.isoformat(),
        }