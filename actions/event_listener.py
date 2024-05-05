# event_listener.py
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="university_db",
    user="postgres",
    password="mariam",
    port="5432"
)

# Set up notification listener
def listen_to_notifications():
    with conn.cursor() as cursor:
        cursor.execute("LISTEN event_change;")
        conn.commit()

        print("Listening for notifications...")

        while True:
            if conn.poll():
                while conn.notifies:
                    notify = conn.notifies.pop(0)
                    print("Received notification:", notify.payload)
                    # Trigger retraining script here

if __name__ == "__main__":
    listen_to_notifications()
