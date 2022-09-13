import os
import sqlite3
from sql_queries import create_table_queries, drop_table_queries


def initialise_db():
    db_filename = "airline2.db"
        
    # remove the db file if it exists
    try:
        os.remove(db_filename)
    except FileNotFoundError:
        pass
    
    # create database and open connection
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        

def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()