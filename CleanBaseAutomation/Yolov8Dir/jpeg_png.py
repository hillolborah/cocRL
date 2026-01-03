from pathlib import Path

# Define the folder containing your images
directory = Path(r'F:\cocRL\CleanBaseAutomation\Yolov8Dir\raw\raw_val')

# Define target extensions (lowercase for comparison)
target_extensions = {'.jpeg', '.jpg'}

# Iterate through all files in the directory
for file_path in directory.iterdir():
    # Check if the file's extension matches our targets (case-insensitive)
    if file_path.suffix.lower() in target_extensions:
        # Define the new filename with .png
        new_path = file_path.with_suffix('.png')
        
        # Rename the file on disk
        file_path.rename(new_path)
        print(f"Renamed: {file_path.name} -> {new_path.name}")
