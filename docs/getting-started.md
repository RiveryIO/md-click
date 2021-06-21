
# Getting Started

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
> mdclick dumps --baseModule=app.cli --baseCommand=main --docsPath=./docs/commands
```

The output:

```shell
./docs/commands/namer.md
./docs/commands/namer-full.md
```

As you can assume, all of the markdown files under `docs/commands` in this repository, generated automatically by `mdclick` command.
Use them as a reference.

