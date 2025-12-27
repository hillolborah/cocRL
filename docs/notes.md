```
.\cocvenv\Scripts\activate
```
```
F:\cocRL> python .\automation\CleanBase.py
```

- [https://clashofclans.fandom.com/wiki/Clash_of_Clans_Wiki](https://clashofclans.fandom.com/wiki/Clash_of_Clans_Wiki)

- The base map in Clash of Clans is a square that is rotated 45 degrees, giving it a diamond-shaped appearance on your screen. Map Dimensions and Structure Grid Size: The playable area for the Home Village is a 44x44 grid of tiles. Total Area: Including the non-playable grassy border (which is 3 tiles wide), the total map size is 50x50 tiles (2,500 total square tiles). Visual Orientation: Because the game uses an isometric perspective, the square grid is viewed from an angle, making the corners point up, down, left, and right rather than having flat edges.

- CleanBaseLogic:

    Step 0: Precondition

    Eagle Artillery is detectable by CV

    Zoom level is irrelevant initially

    Step 1: Place cursor on Eagle Artillery

    Move mouse so that the cursor is exactly on the Eagle Artillery

    This establishes the zoom anchor point

    ⚠️ This step is critical.
    Zoom behavior in CoC is cursor-anchored.

    Step 2: Zoom in fully

    Scroll / zoom in to maximum

    Because the cursor is on Eagle:

    Eagle Artillery is now perfectly centered in the viewport

    This removes any prior camera drift

    At this point:

    Viewport center ≈ Eagle Artillery

    World space is normalized

    Step 3: Cursor reposition (phase-dependent)
    Phase A — Top-Half Scan

    Move cursor to bottom edge of viewport

    Phase B — Bottom-Half Scan

    Move cursor to top edge of viewport

    This does not move the camera yet — it just sets the zoom-out bias.

    Step 4: Zoom out fully

    Zoom out to maximum

    Camera expands away from the cursor

    Resulting visible region:

    Eagle Artillery still visible

    Plus top half or bottom half of the base

    Step 5: Run vegetation logic

    Capture screenshot

    Run vegetation detection

    Project detections → tile/world space

    Store results

algorithm:
```
# Anchor camera
move_cursor(eagle_screen_pos)
zoom_in_fully()

# Phase A: Top half
move_cursor(viewport_bottom_center)
zoom_out_fully()
scan_top_half()

# Re-anchor
move_cursor(eagle_screen_pos)
zoom_in_fully()

# Phase B: Bottom half
move_cursor(viewport_top_center)
zoom_out_fully()
scan_bottom_half()
```