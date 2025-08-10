import re

def question_validator(question: str) -> (bool, str):
    q = question.lower()

    injection_patterns = [
        r"disregard.*(instruction|command)",
        r"ignore.*(prompt|instruction|previous)",
        r"you are now.*",
        r"act as.*",
        r"forget.*above.*",
        r"break.*rules"
    ]
    for pattern in injection_patterns:
        if re.search(pattern, q):
            return False, "⚠️ Prompt injection attempt detected."

    return True, ""
