# Example Configurations

This directory contains pre-configured variations of the skyscraper design for different use cases.

## Available Examples

### 1. Compact Tower (30 floors)
**File:** `compact_tower_30floors.py`

**Specifications:**
- Height: 120m (30 floors × 4m)
- Footprint: 40m × 40m
- Core: 20m × 20m
- Use case: Urban sites with height restrictions

**To use:**
```bash
blender --python examples/compact_tower_30floors.py
```

---

### 2. Standard Tower (50 floors) - DEFAULT
**File:** `../skyscraper_superior_design.py`

**Specifications:**
- Height: 200m (50 floors × 4m)
- Footprint: 50m × 50m
- Core: 25m × 25m
- Use case: Standard Class A office building

**To use:**
```bash
blender --python skyscraper_superior_design.py
```

---

### 3. Supertall Tower (100 floors)
**File:** `supertall_tower_100floors.py`

**Specifications:**
- Height: 380m (100 floors × 3.8m)
- Footprint: 60m × 60m
- Core: 30m × 30m
- Use case: Iconic skyline landmarks

**To use:**
```bash
blender --python examples/supertall_tower_100floors.py
```

**Note:** This configuration generates ~15,000+ objects. Recommended: 16GB RAM, background mode.

---

### 4. Residential Tower (40 floors)
**File:** `residential_tower_40floors.py`

**Specifications:**
- Height: 128m (40 floors × 3.2m)
- Footprint: 35m × 35m
- Core: 18m × 18m
- Use case: Luxury residential condos

**To use:**
```bash
blender --python examples/residential_tower_40floors.py
```

---

## Creating Your Own Configuration

1. Copy `../skyscraper_superior_design.py` to this folder
2. Rename to describe your configuration (e.g., `hotel_tower_60floors.py`)
3. Modify parameters at the top of the file:
   ```python
   num_floors = 60
   floor_height = 3.5
   building_size = 45.0
   core_size = 23.0
   # ... etc
   ```
4. Test with small floor count first:
   ```python
   num_floors = 10  # Quick test
   ```
5. Run and verify before full generation

## Configuration Comparison

| Configuration | Floors | Height | Footprint | Generation Time* | Objects |
|--------------|--------|--------|-----------|-----------------|---------|
| Compact | 30 | 120m | 40m × 40m | 1-3 min | ~4,700 |
| **Standard** | **50** | **200m** | **50m × 50m** | **2-8 min** | **~7,850** |
| Supertall | 100 | 380m | 60m × 60m | 5-15 min | ~15,600 |
| Residential | 40 | 128m | 35m × 35m | 2-5 min | ~6,300 |

*Times vary based on hardware and detail level

## Tips

- **Test first**: Always run with `num_floors = 10` to test parameters
- **Background mode**: Use `blender --background` for faster generation
- **Reduce detail**: Adjust `typical_office_floors[::10]` for fewer interiors
- **Memory**: Supertall config requires 8-16GB RAM

## Parameter Guidelines

### Core Size (must be 20-30% of floor plate):
```python
# Calculation:
core_size = building_size * 0.5  # 25% ratio
# or use this formula:
# core_size = building_size * sqrt(0.25) = building_size * 0.5
```

### Column Spacing (proportional to footprint):
```python
column_spacing = building_size / 5  # Approximately
```

### Mechanical Floors (every 15-20 floors):
```python
# For 30 floors:
mechanical_floors = [9, 19, 29]  # Every 10
# For 50 floors:
mechanical_floors = [14, 29, 44, 49]  # Every 15
# For 100 floors:
mechanical_floors = [19, 39, 59, 79, 99]  # Every 20
```

---

📖 **See [../docs/CUSTOMIZATION.md](../docs/CUSTOMIZATION.md) for detailed customization guide**
