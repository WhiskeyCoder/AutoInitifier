# 🐍 AutoInitifier
_**Make every Python folder package-ready. Instantly. Cleanly. Reusably.**_

---

## 🔥 What is AutoInitifier?

**AutoInitifier** is a recursive Python script that **automatically creates or updates** `__init__.py` files across your entire project, ensuring every subfolder is importable and **keeps your Python packages clean and modular.**

Whether you're working on a complex codebase with 50+ folders or just want to tidy up your project structure, AutoInitifier makes sure every folder plays nice with Python imports.

---

## 🚀 Features

- 📁 Recursively walks all folders  
- ✍️ Creates missing `__init__.py` files  
- 🧠 Updates existing `__init__.py` files with only missing imports  
- 🛡️ Prevents duplicates — intelligently checks before writing  
- 🔧 Outputs clean `from .<module> import *` lines for intra-folder access  
- 💾 Keeps your modular structure tight & import-ready

---

## 🛠️ How It Works

For each directory:
- It finds all `.py` files (except `__init__.py`)
- It generates `from .module_name import *` lines
- If `__init__.py` is missing, it creates it
- If it's already there, it appends only the missing lines

---

## 🧑‍💻 Installation

Clone this repo:

```bash
git clone https://github.com/yourusername/autoinitifier.git
cd autoinitifier
```

Install requirements (none, it’s just Python stdlib ✨).

---

## ▶️ Usage

1. Open `autoinitifier.py`
2. Replace the path with your project's root:

```python
base_dir = r"your\project\path"
```

3. Run the script:

```bash
python autoinitifier.py
```

Boom. Done.

---

## 💡 Example Output

Given a folder like:

```
project/
└── utils/
    ├── helpers.py
    ├── time_tools.py
    └── __init__.py  ← updated to include both modules
```

`__init__.py` will now contain:

```python
from .helpers import *
from .time_tools import *
```

---

## 🤝 Contributing

Found a bug or want more features like:
- `__all__` auto-generation
- Black-style sorting
- CLI flags for mode control?

Feel free to fork and send a PR — or open an issue!

---

## 📜 License

MIT. Use it, love it, abuse it responsibly.

---
