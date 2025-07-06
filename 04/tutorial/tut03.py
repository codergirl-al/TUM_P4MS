from typing import List

def search_for(field: List[int], target: int) -> int:
    if target in field:
        return field.index(target) + 1
    else:
        return -1