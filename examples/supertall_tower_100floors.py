"""
EXAMPLE: Supertall Tower (100 floors)
======================================

A true supertall building configuration for impressive visualizations.

Building Stats:
- Height: 380m (100 floors × 3.8m)
- Footprint: 60m × 60m
- Core: 30m × 30m (25% ratio)
- Leasable Area: ~2,640 m² per floor (73% efficiency)
- Typical for: Iconic skyline landmarks, Asian megacities
"""

# ===== MODIFIED PARAMETERS =====
# (Copy from skyscraper_superior_design.py and modify these lines)

# Building Dimensions
num_floors = 100             # Increased from 50
floor_height = 3.8           # Slightly reduced for structural efficiency
total_height = num_floors * floor_height  # 380m
slab_thick = 0.35            # Thicker for taller building
building_size = 60.0         # Increased from 50.0
build_half = building_size / 2

# Core Dimensions (maintain 25% ratio)
core_size = 30.0             # Increased from 25.0
core_half = core_size / 2
wall_thick = 0.35            # Thicker walls

# Structural System (heavier structure)
column_size = 4.0            # Larger mega-columns
perimeter_column_size = 1.2  # Larger perimeter columns
column_spacing = 10.0

# Special Floors
lobby_floors = [0, 1, 2, 3, 4]  # 5-story grand lobby
mechanical_floors = [19, 39, 59, 79, 99]  # Every 20 floors
typical_office_floors = [i for i in range(5, num_floors) if i not in mechanical_floors]

# Facade System
curtain_wall_thick = 0.18    # Thicker for wind loads
mullion_width = 0.10
vision_glass_h = 1.8
spandrel_h = floor_height - vision_glass_h - 0.2
window_module = 1.5

# Performance Optimization (IMPORTANT for 100 floors!)
# Generate interiors only every 10th floor to reduce object count
office_detail_frequency = 10

# ===== ADJUST OFFICE GENERATION =====
# In the script, change line 475 to:
# for floor_num in typical_office_floors[::office_detail_frequency]:

# ===== REST OF SCRIPT UNCHANGED =====
# Copy the entire material creation and geometry generation code
# from skyscraper_superior_design.py

print("=" * 60)
print("SUPERTALL 100-STORY TOWER GENERATION COMPLETE")
print("=" * 60)
print(f"Total Height: {total_height}m")
print(f"Floor Plate: {building_size}m x {building_size}m")
print(f"Core Size: {core_size}m x {core_size}m (25%)")
print(f"Floors: {num_floors} ({len(typical_office_floors)} typical office)")
print(f"Structural System: 4 mega-columns ({column_size}m) + perimeter grid")
print("Configuration: Supertall office tower")
print("=" * 60)
