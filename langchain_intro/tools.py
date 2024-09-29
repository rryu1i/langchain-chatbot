import random
import time
from typing import Union

def get_current_wait_time(hospital: str) -> Union[int, str]:
    """Dummy function to generate fake wait times"""

    if hospital not in ["A", "B", "C", "D"]:
        return f"Hospital {hospital} does not exist"

    # Simulate API call delay
    time.sleep(1)

    return random.randint(0, 10000)