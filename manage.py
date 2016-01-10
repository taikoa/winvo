import click

import winvo

INVOICES_DIR = ''
SKEL_FILE = './example.conf'

# TODO Me cargo el custom config??
# TODO Create invoices path
# TODO Create invoices number file


@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', default=None, help='Name of the invoice file')
@click.option('--client', default=None, help='Client for the invoice')
def new_invoice(name, client=None):
    pass


@cli.command()
@click.option('--path', default=None, help='Pdf path')
def topdf(config):
    configuration = winvo.read_config(config)
    output = '.'.join(config.split('.')[0:-1] + ['pdf'])
    winvo.getPDF(output, configuration)


@cli.command()
@click.option('--path', default=None, help='Locales path')
def genlocales(path):
    pass


@cli.command()
@click.option('--path', default=None, help='Locales path')
def translate(path):
    pass


if __name__ == '__main__':
    cli(obj={})
