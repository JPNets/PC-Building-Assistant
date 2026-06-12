from typing import List, Dict
from .build_generator import generate_candidate_builds
from .compatibility import check_compatibility
from .scoring import score_build


def optimize_builds(user_input: Dict, top_n: int = 5) -> List[Dict]:
    candidates = generate_candidate_builds(limit_per_category=3)
    filtered = []

    for c in candidates:
        comp = c['components']
        compat = check_compatibility(comp)
        # drop combos with any ❌ Incompatible
        if any('❌' in v for v in compat.values()):
            continue
        # budget filter
        if c['total_price'] > user_input.get('budget', 9999):
            continue
        # score
        scores = score_build(comp, user_input.get('use_case', 'gaming'))
        c['scores'] = scores
        c['compatibility'] = compat
        filtered.append(c)

    # sort for different objectives
    builds = []
    if not filtered:
        return []

    # Balanced: maximize gaming+productivity
    balanced = sorted(filtered, key=lambda x: -(x['scores']['gaming'] + x['scores']['productivity']))[:top_n]
    value = sorted(filtered, key=lambda x: -x['scores']['value'])[:top_n]
    max_perf = sorted(filtered, key=lambda x: -(x['scores']['gaming'] + x['scores']['ai_ml']))[:top_n]

    builds.append({'type': 'Balanced Build', 'items': balanced})
    builds.append({'type': 'Best Value Build', 'items': value})
    builds.append({'type': 'Maximum Performance Build', 'items': max_perf})

    return builds
