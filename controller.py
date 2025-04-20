import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

# Database connection pool
pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

# Get all projects
def get_projects():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, lat, lon, sound, hour
            FROM nangrong
        """)
        result = [models.Project(*row) for row in cs.fetchall()]
        return result

# Get details of a specific project
def get_project_details(project_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, lat, lon, sound, hour
            FROM nangrong
            WHERE id = %s
        """, [project_id])
        result = cs.fetchone()
    if result:
        return models.Project(*result)
    else:
        abort(404)

# Get all dust entries
def get_dust_data():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, hour, pm25, pm10, aqi, lat, lon
            FROM nangrong
        """)
        result = [models.Dust(*row) for row in cs.fetchall()]
        return result

# Get details of a specific dust record
def get_dust_entry(dust_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, hour, pm25, pm10, aqi, lat, lon
            FROM nangrong
            WHERE id = %s
        """, [dust_id])
        result = cs.fetchone()
    if result:
        return models.Dust(*result)
    else:
        abort(404)

def get_dust_average():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT AVG(pm25), AVG(pm10), AVG(aqi)
            FROM nangrong
        """)
        result = cs.fetchone()
    if result and all(val is not None for val in result):
        avg_pm25, avg_pm10, avg_aqi = result
        return models.DustAverage(round(avg_pm25, 2), round(avg_pm10, 2), round(avg_aqi, 2))
    else:
        abort(404)
