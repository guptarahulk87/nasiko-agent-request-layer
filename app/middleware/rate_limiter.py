
import time

request_tracker = {}

LIMIT = 5
WINDOW = 60

def allow_request(agent_name):
    current_time = time.time()

    if agent_name not in request_tracker:
        request_tracker[agent_name] = []

    request_tracker[agent_name] = [
        t for t in request_tracker[agent_name]
        if current_time - t < WINDOW
    ]

    if len(request_tracker[agent_name]) >= LIMIT:
        return False

    request_tracker[agent_name].append(current_time)

    return True
