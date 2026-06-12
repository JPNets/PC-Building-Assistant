from itertools import product
from typing import List, Dict
from utils.file_io import load_json


def generate_candidate_builds(limit_per_category: int = 3) -> List[Dict]:
    # load small sample sets from data
    cpus = load_json('cpus.json')[:limit_per_category]
    gpus = load_json('gpus.json')[:limit_per_category]
    mobos = load_json('motherboards.json')[:limit_per_category]
    rams = load_json('ram.json')[:limit_per_category]
    storages = load_json('storage.json')[:limit_per_category]
    psus = load_json('psus.json')[:limit_per_category]
    coolers = load_json('coolers.json')[:limit_per_category]
    cases = load_json('cases.json')[:limit_per_category]

    candidates = []
    # naive combinatorics — small datasets keep this manageable
    for cpu, gpu, mobo, ram, storage, psu, cooler, case in product(cpus, gpus, mobos, rams, storages, psus, coolers, cases):
        components = {
            'cpu': cpu,
            'gpu': gpu,
            'motherboard': mobo,
            'ram': ram,
            'storage': storage,
            'psu': psu,
            'cooler': cooler,
            'case': case
        }
        total_price = sum([c.get('price', 0) for c in components.values()])
        total_power = sum([c.get('power_draw', 0) for c in components.values() if c.get('power_draw')])
        candidates.append({
            'components': components,
            'total_price': total_price,
            'total_power': total_power
        })
    return candidates
