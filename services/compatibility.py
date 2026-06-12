from typing import Dict, Tuple


def check_compatibility(components: Dict) -> Dict[str, str]:
    """Return compatibility status per rule: Compatible/Warning/Incompatible"""
    status = {}
    cpu = components.get('cpu')
    mobo = components.get('motherboard')
    ram = components.get('ram')
    gpu = components.get('gpu')
    psu = components.get('psu')
    cooler = components.get('cooler')
    case = components.get('case')

    # CPU <-> Motherboard
    if cpu and mobo:
        if cpu.get('socket') == mobo.get('socket'):
            status['cpu_motherboard'] = "✅ Compatible"
        else:
            status['cpu_motherboard'] = "❌ Incompatible: socket mismatch"

    # RAM generation
    if ram and mobo:
        if ram.get('ddr_generation') == mobo.get('ram_generation'):
            status['ram_motherboard'] = "✅ Compatible"
        else:
            status['ram_motherboard'] = "❌ Incompatible: RAM generation mismatch"

    # GPU clearance
    if gpu and case:
        if gpu.get('length_mm', 0) <= case.get('gpu_clearance_mm', 0):
            status['gpu_case'] = "✅ Compatible"
        else:
            status['gpu_case'] = "❌ Incompatible: GPU too long for case"

    # PSU wattage check
    if psu and components:
        total_draw = sum([c.get('power_draw', 0) for c in components.values() if isinstance(c, dict)])
        # simple headroom 25%
        required = total_draw * 1.25
        if psu.get('wattage', 0) >= required:
            status['psu'] = "✅ Compatible"
        else:
            status['psu'] = "❌ Incompatible: PSU wattage insufficient"

    # Cooler support
    if cooler and cpu:
        supported = cooler.get('supported_sockets', [])
        if cpu.get('socket') in supported:
            status['cooler_cpu'] = "✅ Compatible"
        else:
            status['cooler_cpu'] = "⚠ Warning: Cooler may not support CPU socket"

    # Form factor
    if mobo and case:
        if mobo.get('form_factor') in case.get('supported_form_factors', []):
            status['form_factor'] = "✅ Compatible"
        else:
            status['form_factor'] = "❌ Incompatible: Motherboard doesn't fit case"

    return status
