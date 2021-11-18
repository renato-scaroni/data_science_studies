import requests
from io import StringIO
import pandas as pd
import sqlite3 as sql
from tqdm import tqdm
from datetime import datetime

BASE_URL = "https://github.com/beefsack/bgg-ranking-historicals/raw/master/"
def build_url(year, month, day=1):
    return f'{BASE_URL}{year}-{month:02d}-{day:02d}.csv'

def create_conn (db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sql.connect(db_file)
    except Exception as e:
        print(e)

    return conn

def build_range(
        starting_month=1, 
        starting_year=2019, 
        end_month=datetime.now().month, 
        end_year=datetime.now().year
    ):
    if int(starting_year) != end_year:
        date_range = [(starting_year, m) for m in range(starting_month, 13)]
        return date_range + build_range(starting_month=1, starting_year=starting_year+1, end_year=end_year, end_month=end_month)
    else:
        date_range = [(starting_year, m) for m in range(starting_month, end_month+1)]
        return date_range

def drop_table(conn, table):
    """
    Drop table
    :param conn: Connection to the SQLite database
    :param table: name of the table to drop
    :return:
    """
    sql = f'DROP TABLE if exists {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def format_column_name(name):
    return "_".join(name.split(' ')).lower()

def rebuild_history(
        conn, 
        top100_table="top_100_history",
        starting_month=1,
        starting_year = 2017,
        end_month=datetime.now().month, 
        end_year=datetime.now().year
    ):
    for y, m in tqdm(build_range(starting_month, starting_year, end_month, end_year)):
        resp = requests.get(build_url(y, m))
        data = resp.text
        if resp.status_code != 200:
            print(f'no entries for {y} month {m}')
            continue
        data = StringIO(data)
        df = pd.read_csv(data, sep=',')
        df.columns = map(format_column_name, df.columns.to_list())
        df["rank_year"] = y
        df["rank_month"] = m
        df['rank_year'] = df.rank_year.astype(str)
        df['rank_month'] = df.rank_month.astype(str)

        df['date_str'] = df.rank_year + '-' + df.rank_month
        df['date'] = pd.to_datetime(df['date_str'])
        df.to_sql(top100_table, conn, if_exists='append', index=False)

if __name__ == "__main__":
    conn = create_conn("bgg_history.db")
    drop_table(conn, "top_100_history")
    rebuild_history(conn)
