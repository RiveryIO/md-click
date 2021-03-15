# MD Click
MD-Click is a command line tool for creating `.md` files for any python's click CLI projects.

# The Problem
After creating new CLI project using click, we couldn't found out any tool that generates automatic
`.md` files documentation per each command. This is the reason we've create this quick and easy tool.

# The Solution
MD-Click creates `.md` files per each command exists under the `click` project CLI.
The tool runs recursively and generates a markdown file per each command, and sub commands.

# Installation

Just install it using pip:
```bash
> pip install md-click
```