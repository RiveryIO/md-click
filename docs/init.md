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

# Usage

Create md files per each command, in format of `parent-command`, under the `--docsPath` directory.

for example, we have the next click python module:

```python
# app/cli.py
import click

@click.group('namer')
@click.option('--debug', help='Should I run on Debug?', is_flag=True)
def main(**kwargs):
  """ A namer CLI """
  debug = kwargs.get('debug')
  if debug:
    click.secho('is Debug? True', color='green')

@main.command('full')
@click.option('--name', help='The user name', required=True, type=str)
@click.option('--lastName', help='The last Name', required=False, type=str)
def full_name(**kwargs):
    """ A CLI that gets name and last name and returns the full name"""
    firstname = kwargs.get('name')
    lastname = kwargs.get('lastname')
    
    click.secho(f'The full name is: {firstname} {lastname}', color='yellow')
```

and we want to create a nice md files per each command, we'll run the next cli command:

```shell
> mdclick dumps --baseModule=app.cli --baseCommand=main --docPath=./docs/commands
```

The output:

```shell
./docs/commands/namer.md
./docs/commands/namer-full.md
```

As you can assume, all of the markdown files under `docs/commands` in this repository, generated automatically by `mdclick` command.
Use them as a reference.

