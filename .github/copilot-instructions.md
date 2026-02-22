# Copilot Instructions

## Python Package Management
- Always use `uv` for Python package management in this project
- Use `uv add <package>` to add new dependencies
- Use `uv add --dev <package>` for development dependencies
- Use `uv sync` to install dependencies from lockfile
- Use `uv run <command>` to run commands in the project environment
- Use `uv venv` for creating virtual environments if needed
- Never suggest using pip, conda, or other package managers directly