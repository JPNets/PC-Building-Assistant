from typing import Dict


def score_build(components: Dict, use_case: str) -> Dict[str, float]:
    """Return multiple scores for a build"""
    scores = {
        'gaming': 0.0,
        'productivity': 0.0,
        'ai_ml': 0.0,
        'value': 0.0,
        'efficiency': 0.0,
        'upgradeability': 0.0,
    }

    cpu = components.get('cpu', {})
    gpu = components.get('gpu', {})
    ram = components.get('ram', {})
    psu = components.get('psu', {})

    # Simple heuristics: weighted sums
    cpu_score = cpu.get('performance_score', 0)
    gpu_score = gpu.get('performance_score', 0)
    ram_size = ram.get('capacity_gb', ram.get('capacity', 16))
    psu_watt = psu.get('wattage', 0)
    total_price = sum([c.get('price', 0) for c in components.values() if isinstance(c, dict)])

    scores['gaming'] = gpu_score * 0.7 + cpu_score * 0.3
    scores['productivity'] = cpu_score * 0.6 + ram_size * 10
    scores['ai_ml'] = gpu_score * 0.6 + ram_size * 5 + cpu_score * 0.2
    # value = performance per dollar
    perf = (cpu_score + gpu_score)
    scores['value'] = perf / max(total_price, 1)
    # efficiency: performance per watt
    total_power = sum([c.get('power_draw', 0) for c in components.values() if isinstance(c, dict)])
    scores['efficiency'] = perf / max(total_power, 1)
    # upgradeability simple proxy
    scores['upgradeability'] = (psu_watt / 1000) + (ram_size / 64)

    # normalize / scale a bit
    for k, v in scores.items():
        scores[k] = round(v, 2)

    return scores
