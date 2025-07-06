from typing import List, Tuple

def solution(n: int, matches: List[Tuple[int, int, int, int]]) -> List[int]:
    stats = {i: [0, 0, 0] for i in range(1, n+1)}
    
    for i, j, p, q in matches:
        stats[i][2] += p
        stats[j][2] += q
        stats[i][1] += p - q
        stats[j][1] += q - p
        
        if p > q:
            stats[i][0] += 3
        elif p < q:
            stats[j][0] += 3
        else:
            stats[i][0] += 1
            stats[j][0] += 1
    
    sorted_teams = sorted(range(1, n+1), key=lambda team: (
        -stats[team][0], -stats[team][1], -stats[team][2], team
    ))
    
    return sorted_teams