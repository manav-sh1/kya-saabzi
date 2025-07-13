import random
from datetime import datetime, timedelta
from typing import List, Tuple, Dict 


def recommend_sabzi(sabzi_list: List[Dict[str, str]]) -> Tuple[str, int]:
    """
        Returns a dictionary of vegetable(s) and the amount of days 
        passed.

    Args:
        sabzi_list (List[Dict]): A list of vegetables and the date they
        were last made.

    Returns:
        Tuple[str, int]: (vegetable name, days since last cooked)
    """
    today = datetime.today().date()
    candidates = []
    threshold = 7

    for sabzi in sabzi_list:
        last_cooked = sabzi.date_cooked or datetime(2000, 1, 1).date()
        days_ago = (today - last_cooked).days

        if days_ago >= threshold:
            candidates.append((sabzi.name, days_ago))

    if candidates:
        return candidates
    else:
        return ("Kuch bhi bana lo", 0)
