# src/config.py
import os

# Read the path_to_emls from an environment variable, with a default value
path_to_emls = os.getenv('PATH_TO_EMLS', './tests/data/emls')