import datetime
import os
from pathlib import Path

DIR = 'backup'

HOST = 'localhost'
PORT = '3306'
USER_NAME = 'root'
PASSWORD = ''
databases = ('database')
# databases = ('database', 'database_2')

LATEST_DIR = f'{DIR}/_latest'


# databases=('diverse_bpc_local')

def get_dump(db):
    day_stamp = datetime.datetime.now().strftime("%Y_%m_%d")
    file_stamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # create a folder with date if it doesn't exist
    Path(f'{DIR}/{day_stamp}').mkdir(parents=True, exist_ok=True)

    command = f'mysqldump -h {HOST} -P {PORT} -u {USER_NAME} --p={PASSWORD} {db} > {DIR}/{day_stamp}/{db}_{file_stamp}.sql'
    command_latest = f'mysqldump -h {HOST} -P {PORT} -u {USER_NAME} --p={PASSWORD} {db} > {LATEST_DIR}/{db}_latest.sql'

    os.popen(command)
    os.popen(command_latest)

    print(f'Database dumped to {day_stamp}/{db}_{file_stamp}\n')


if __name__ == "__main__":
    # make sure folders for backups exist, and create them in case they dont
    Path('backup').mkdir(parents=True, exist_ok=True)
    Path('backup/_latest').mkdir(parents=True, exist_ok=True)

    if isinstance(databases, tuple):
        for database in databases:
            get_dump(database)
    else:
        get_dump(databases)
