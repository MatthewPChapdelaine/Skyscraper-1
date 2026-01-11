"""
EXAMPLE: Residential Tower (40 floors)
=======================================

Optimized for residential use with appropriate floor heights and window proportions.

Building Stats:
- Height: 128m (40 floors × 3.2m)
- Footprint: 35m × 35m
- Core: 18m × 18m (26% ratio)
- Leasable Area: ~900 m² per floor (73% efficiency)
- Typical for: Luxury residential condos, apartment towers
"""

# ===== MODIFIED PARAMETERS =====
# (Copy from skyscraper_superior_design.py and modify these lines)

# Building Dimensions
num_floors = 40
floor_height = 3.2           # Typical residential ceiling height
total_height = num_floors * floor_height  # 128m
slab_thick = 0.25            # Thinner for residential loads
building_size = 35.0         # Smaller footprint
build_half = building_size / 2

# Core Dimensions
core_size = 18.0             # Scaled proportionally
core_half = core_size / 2
wall_thick = 0.25

# Structural System
column_size = 2.0            # Lighter structure
perimeter_column_size = 0.6
column_spacing = 8.75        # Proportional spacing

# Vertical Circulation
stair_width = 1.8
stair_run = 2.8
stair_tread = 0.28
stair_riser = 0.178          # Adjusted for 3.2m height
num_steps = int(floor_height / stair_riser)  # ~18 steps

# Elevators (residential typically needs fewer)
elev_width = 2.0             # Slightly smaller
elev_depth = 2.2

# Special Floors
lobby_floors = [0]           # Single-story residential lobby
mechanical_floors = [13, 26, 39]  # Every ~13 floors
typical_office_floors = [i for i in range(1, num_floors) if i not in mechanical_floors]

# Facade System (residential proportions)
curtain_wall_thick = 0.15
mullion_width = 0.08
vision_glass_h = 1.6         # Lower sill height for residential
spandrel_h = floor_height - vision_glass_h - 0.4
window_module = 2.5          # Wider modules for residential units

# ===== ADDITIONAL CUSTOMIZATIONS =====

# Residential units typically have:
# - Private balconies (not modeled in this example)
# - Smaller window modules (wider for unit spacing)
# - Lower window sills
# - Less transparent lobby

# Adjust lobby glazing in script:
# if is_lobby:
#     vision_h = floor_height - 1.0  # Less dramatic than office
#     spandrel_h = 0.5

# ===== REST OF SCRIPT UNCHANGED =====
# Copy the entire material creation and geometry generation code
# from skyscraper_superior_design.py

# ===== NOTE ON INTERIOR LAYOUTS =====
# For residential, you might want to:
# 1. Create unit divisions (studio, 1BR, 2BR layouts)
# 2. Add balconies at perimeter
# 3. Different corridor layout (single-loaded or double-loaded)
# This example maintains the basic office interior for simplicity

print("=" * 60)
print("RESIDENTIAL 40-STORY TOWER GENERATION COMPLETE")
print("=" * 60)
print(f"Total Height: {total_height}m")
print(f"Floor Plate: {building_size}m x {building_size}m")
print(f"Core Size: {core_size}m x {core_size}m (26%)")
print(f"Floors: {num_floors} ({len(typical_office_floors)} residential floors)")
print("Configuration: Residential tower")
print("=" * 60)
