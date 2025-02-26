import psycopg2 #postgreSQL module

def connect_db():
    """Connects postgreSQL and returns a connection."""
    return psycopg2.connect (
        dbname = "network_db",
        user = "postgres",
        password = "admin123",
        host = "localhost",
        port = "5432"
    )

def save_to_postgresql(devices):
    """Stores scan results in PostgreSQL"""
    conn = connect_db() #Establishing connection and assign connection object to var conn
    cursor = conn.cursor() #create cursor to allow executing SQL commands and fetching from database

    for device in devices:
        cursor.execute("INSERT INTO network_scan (ip_address, mac_address) VALUES (%s, %s)",
                        (device["IP"], device["MAC"])) #inserting data into database

    conn.commit() #commit changes
    cursor.close() #closing cursor object
    conn.close() #closing connection
    print("Results saved to PostgreSQL")

if __name__ == "__main__":
    test_data = [{"IP": "192.168.1.1", "MAC": "00:1A:2B:3C:4D:5E"}]
    save_to_postgresql(test_data)  # Testing database save function


