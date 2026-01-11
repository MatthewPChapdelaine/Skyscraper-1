"""
EXAMPLE: Compact Office Tower (30 floors)
==========================================

A smaller, more efficient office building configuration.

Building Stats:
- Height: 120m (30 floors × 4m)
- Footprint: 40m × 40m
- Core: 20m × 20m (25% ratio)
- Leasable Area: ~1,170 m² per floor (73% efficiency)
- Typical for: Urban sites with height restrictions
"""

# ===== MODIFIED PARAMETERS =====
# (Copy from skyscraper_superior_design.py and modify these lines)

# Building Dimensions
num_floors = 30              # Reduced from 50
floor_height = 4.0
total_height = num_floors * floor_height  # 120m
slab_thick = 0.3
building_size = 40.0         # Reduced from 50.0
build_half = building_size / 2

# Core Dimensions (maintain 25% ratio)
core_size = 20.0             # Reduced from 25.0
core_half = core_size / 2
wall_thick = 0.3

# Structural System
column_size = 2.5            # Slightly smaller
perimeter_column_size = 0.7
column_spacing = 10.0

# Special Floors
lobby_floors = [0, 1]        # 2-story lobby (smaller)
mechanical_floors = [9, 19, 29]  # Every 10 floors
typical_office_floors = [i for i in range(2, num_floors) if i not in mechanical_floors]

# Facade System (same as original)
curtain_wall_thick = 0.15
mullion_width = 0.08
vision_glass_h = 1.8
spandrel_h = 2.2
window_module = 1.5

# ===== REST OF SCRIPT UNCHANGED =====
# Copy the entire material creation and geometry generation code
# from skyscraper_superior_design.py

print("=" * 60)
print("COMPACT 30-STORY OFFICE TOWER GENERATION COMPLETE")
print("=" * 60)
print(f"Total Height: {total_height}m")
print(f"Floor Plate: {building_size}m x {building_size}m")
print(f"Core Size: {core_size}m x {core_size}m (25%)")
print(f"Floors: {num_floors} ({len(typical_office_floors)} typical office)")
print("Configuration: Compact office tower")
print("=" * 60)
