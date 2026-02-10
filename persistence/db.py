import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="siste214_gato_si",
        password = "ITSON@2026#si",
        database="siste214_gato_si"
    )