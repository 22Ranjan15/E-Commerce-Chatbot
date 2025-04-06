import os
from pathlib import Path

list_of_files = [
    ".env",
    ".gitignore",
    "setup.py",
    "requirements.txt",
    "README.md",
    "LICENSE",
    "Data/.gitkeep",
    "Demo/.gitkeep",
    "Notebooks/experiments.ipynb",
    "Components/__init__.py",
    "Components/data_convertion.py",
    "Components/data_ingestion.py",
    "Components/retrieve_response.py",
    "static/style.css",
    "static/script.js",
    "templates/index.html",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok = True)

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w"):
            pass