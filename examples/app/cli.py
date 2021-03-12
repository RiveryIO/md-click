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
