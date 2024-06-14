import click

from app.main import App


@click.command()
@click.option('--mappings', default='csv/mappings.csv', help='Mappings file')
@click.option('--price_catalog', default='csv/pricat.csv', help='Price catalog file')
@click.option('--output_file', default='catalog.json', help='Output json catalog file')
def run(mappings, price_catalog, output_file):
    app = App(mappings)
    app.process_catalog(price_catalog, output_file)
    click.echo('Done')


if __name__ == '__main__':
    run()
