from typing import List, Dict

def within_budget(total: float, budget: float) -> bool:
    return total <= budget

def breakdown(components: List[Dict]) -> Dict[str, float]:
    return {c.get('id', c.get('name')): c.get('price', 0) for c in components}
