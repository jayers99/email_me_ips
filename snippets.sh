# Install Python 3.9.19 using pyenv
pyenv install 3.9.19

# Set the local Python version to 3.9.19
pyenv local 3.9.19

# Create a new pipenv environment with Python 3.9.19
pipenv --python 3.9.19

# Activate the pipenv shell
pipenv shell

# Create subdirectories
mkdir src tests docs

# Create __init__.py and main.py in src
touch src/__init__.py src/main.py

# Create __init__.py and test_main.py in tests
touch tests/__init__.py tests/test_main.py

# Create README.md in docs
touch docs/README.md

# Create setup.py and Pipfile in the main directory
touch setup.py Pipfile