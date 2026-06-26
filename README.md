# Emergence

Emergence is a work-in-progress planet and climate simulator built as a learning project for mathematics, simulation, and procedural generation.

Rather than relying on existing simulation libraries, the goal is to implement many concepts from first principles and explore how complex systems arise from simple rules. Over time the project aims to simulate a planet from its physical properties, allowing climate, hydrology, ecosystems, trade routes, and eventually civilizations to emerge naturally.

The project is also a companion to a larger worldbuilding effort, where the simulator serves as a tool for exploring plausible geography and environmental systems rather than manually designing them.

## Technology

- Python with
- NumPy
- Matplotlib

## Run

It does not currently run with

```bash
python src/emergence/main.py
```

Run with one of these:

```bash
uv run src/emergence/main.py

uv run python src/emergence/main.py
```

## Architecture

### Outline:

```
             Grid
      width, height, shape
              │
      ┌───────┴────────┐
      │                │
 Height Layer     Rain Layer
      │                │
      └───────┬────────┘
              │
          Renderer
```

### First steps

```
emergence/
│
src/
└── emergence/
│   ├── core/
│   │   ├── grid.py
│   │   ├── layer.py
│   │   └── world.py
│   │
│   ├── terrain/
│   │   ├── height.py
│   │   ├── erosion.py
│   │   └── rivers.py
│   │
│   ├── climate/
│   │   ├── wind.py
│   │   ├── rainfall.py
│   │   └── temperature.py
│   │
│   ├── civilization/
│   │   ├── settlements.py
│   │   └── roads.py
│   │
│   └── main.py
│
├── experiments/
│
├── tests/
│
├── README.md
│
├── pyproject.toml
│
├── uv.lock
│
└── .gitignore
```

### Finally (long term plans)

```
emergence/

planet/
    sphere.py
    projection.py
    coordinates.py

terrain/
    plates.py
    uplift.py
    erosion.py

climate/
    winds.py
    currents.py
    temperature.py
    rainfall.py

hydrology/
    rivers.py
    lakes.py
    watersheds.py

ecology/
    biomes.py
    vegetation.py

civilization/
    settlement.py
    roads.py
    trade.py
    politics.py

render/
    maps.py
    colors.py

experiments/
```

## Learning Milestones

```
Emergence

01_planet
02_height
03_temperature
04_wind
05_currents
06_rainfall
07_rivers
08_biomes
09_settlements
10_trade
```

## Initial Planet Parameters

Earth:

```
| Parameter       |                    Value |
| --------------- | -----------------------: |
| Mean radius     |                  6371 km |
| Rotation period |                     24 h |
| Axial tilt      |                    23.4° |
| Gravity         | Approximately Earth-like |
```

Planet B:

These values are intentionally close to Earth to reduce complexity during the early stages of development.

```
| Parameter       |                    Value |
| --------------- | -----------------------: |
| Mean radius     |                  7000 km |
| Rotation period |                     24 h |
| Axial tilt      |                      23° |
| Gravity         | Approximately Earth-like |
```

## Notes

The world is stored in row-major order:

```
grid[y][x]
```

Rows first. Columns second (matches NumPy).
