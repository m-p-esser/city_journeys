import click
from src.db import DatabaseClient

@click.command()
@click.option('--file_name', default='cities.csv', help='File you want to import into DB')
@click.option('--database', default='db_prod', help='Target Database')
@click.option('--chunk_size', default=1000, help='Number of rows committed on each batch')
def import_data(file_name, database, chunk_size):
    db_client = DatabaseClient()
    table_name = file_name.split('.')[0]
    db_client.insert_from_csv(
        file_name,
        table_name,
        database,
        chunk_size
    )

if __name__ == '__main__':
    import_data()