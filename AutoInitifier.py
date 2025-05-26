import os

# Root folder to walk
base_dir = r"your\project\path"  # ← Replace with your root directory

def generate_import_lines(py_files):
    return [f"from .{os.path.splitext(f)[0]} import *" for f in py_files if f.endswith(".py") and f != "__init__.py"]

def update_init_file(init_path, import_lines):
    if os.path.exists(init_path):
        with open(init_path, "r", encoding="utf-8") as f:
            existing_lines = f.read().splitlines()
    else:
        existing_lines = []

    new_lines = []
    for line in import_lines:
        if line not in existing_lines:
            new_lines.append(line)

    if new_lines:
        with open(init_path, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(new_lines) + "\n")
        print(f"Updated: {init_path}")
    else:
        print(f"Unchanged: {init_path}")

# Walk the tree
for root, dirs, files in os.walk(base_dir):
    py_files = [f for f in files if f.endswith(".py")]
    import_lines = generate_import_lines(py_files)
    if import_lines:
        init_path = os.path.join(root, "__init__.py")
        update_init_file(init_path, import_lines)
