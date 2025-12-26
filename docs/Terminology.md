# Absolute Viewport Coordinate Model

This document defines the **canonical coordinate system, terminology, and invariants** for the Clash of Clans vegetation mapping and removal system running on **Google Play Games (Desktop)**.

The goal is to build a **stable world-space representation of all vegetation** when the full base does not fit in the screen at maximum zoom-out and vertical panning is required.

---

## 1. Design Decision (Locked)

We use an **absolute viewport model**.

> **The viewport is fixed and absolute.**
> **The world (base) moves underneath the viewport when panning.**
> **Screen space coordinates are identical to viewport coordinates.**

This is a viewport-centric reference frame. All logic, code, and reasoning must conform to this model.

---

## 2. Terminology

### 2.1 Viewport (Absolute)

**Definition**
The viewport is the fixed rectangular window through which the game world is observed.

**Properties**

* Fixed position
* Fixed size (at fixed zoom level)
* Defines the origin `(0, 0)`
* Does **not** move

**Interpretation**
All `(x, y)` values produced by vision or used for clicking are relative to the viewport.

---

### 2.2 Screen Space (SS)

**Definition**
Screen Space is the pixel coordinate system of the emulator window.

**In this model**

> **Screen Space ≡ Viewport Space**

They are treated as the same coordinate system.

**Properties**

* Origin: top-left of viewport
* Units: pixels
* Fixed
* Used for interaction

**Usage**

* Vision detections
* Mouse clicks
* Screenshot indexing

```python
screen_x, screen_y
```

---

### 2.3 World Space (WS)

**Definition**
World Space is a logical coordinate system representing the full Clash of Clans base.

**Properties**

* Global
* Persistent
* Relative positions do not change
* Independent of viewport

World space coordinates represent **where objects truly are on the base**, regardless of what is currently visible.

```python
world_x, world_y
```

---

### 2.4 World Offset (WO)

**Definition**
World Offset represents how much the world has shifted relative to the fixed viewport.

```python
world_offset_y
```

**Semantics**

* Increases when panning down
* Decreases when panning up
* Accumulates over time

This replaces the traditional concept of a moving camera.

---

## 3. Coordinate Transformations

### 3.1 Screen → World

```python
world_y = screen_y + world_offset_y
```

### 3.2 World → Screen

```python
screen_y = world_y - world_offset_y
```

These equations must be the **only** way coordinates are transformed.

---

## 4. Panning Semantics

### Visual Pan Down

* World moves up relative to viewport
* `world_offset_y` increases

```python
world_offset_y += pan_delta_y
```

### Visual Pan Up

* World moves down relative to viewport
* `world_offset_y` decreases

---

## 5. Invariants (Must Always Hold)

These are non-negotiable.

1. **World positions are invariant**
   Objects do not move relative to each other in world space.

2. **Screen positions change on pan**
   Objects shift in screen space when panning.

3. **Viewport never moves**
   `(0, 0)` is always the same.

4. **World Offset accumulates pan history**

5. **Stored coordinates are always world-space**

---

## 6. Landmark Consistency Check

Let Town Hall be a fixed world object.

Initial state:

```python
screen_y = 300
world_offset_y = 0
world_y = 300
```

After panning down by 200 pixels:

```python
world_offset_y = 200
screen_y = 100
world_y = 300
```

✔ World position unchanged
✔ Screen position changed
✔ Viewport fixed

---

## 7. Vegetation Detection Pipeline

### Step 1: Detect in Screen Space

```python
screen_detection = (screen_x, screen_y)
```

### Step 2: Project to World Space

```python
world_y = screen_y + world_offset_y
```

### Step 3: Store in Vegetation Map

```python
vegetation_map.add((screen_x, world_y))
```

---

## 8. Vegetation Map

**Definition**
A persistent registry of all vegetation in world space.

```python
VegetationMap = {
    "bush": set[(world_x, world_y)],
    "tree": set[(world_x, world_y)],
}
```

**Properties**

* World-space only
* Deduplicated
* Order-independent

---

## 9. Visibility Test

Determines whether a world-space object is currently visible.

```python
def is_visible(world_y):
    return (
        world_offset_y <= world_y <=
        world_offset_y + viewport_height
    )
```

---

## 10. Naming Conventions (Mandatory)

| Concept         | Variable Name          |
| --------------- | ---------------------- |
| Screen Space    | `screen_x`, `screen_y` |
| World Space     | `world_x`, `world_y`   |
| World Offset    | `world_offset_y`       |
| Viewport Height | `viewport_height`      |

Do not introduce alternative names.

---

## 11. Mental Model (One Sentence)

> **The viewport is fixed.
> The world slides underneath it.
> Screen coordinates live inside the viewport.**

If this statement is true everywhere in the codebase, the system is correct.

---

## 12. Scope

This document governs:

* Vision
* Mapping
* Planning
* Automation
* RL observation design

Any new module must comply with this coordinate model.

---

**Status:** Locked and canonical
