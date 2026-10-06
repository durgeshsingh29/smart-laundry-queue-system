import sqlite3
from datetime import datetime

DB_NAME = "laundry.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            room_no TEXT NOT NULL
        )
    """)

    # Machines table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_name TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'Available',
            current_student TEXT
        )
    """)

    # Queue table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS laundry_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            machine_name TEXT NOT NULL,
            join_time TEXT NOT NULL,
            status TEXT DEFAULT 'Waiting',
            estimated_wait INTEGER DEFAULT 0
        )
    """)

    # Insert default machines
    machines = [
        ("Machine 1",),
        ("Machine 2",),
        ("Machine 3",),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO machines (machine_name)
        VALUES (?)
    """, machines)

    conn.commit()
    conn.close()


def add_student(student_id, name, room_no):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO students (student_id, name, room_no)
            VALUES (?, ?, ?)
        """, (student_id, name, room_no))

        conn.commit()
        return True, "Student registered successfully."

    except sqlite3.IntegrityError:
        return False, "Student ID already exists."

    finally:
        conn.close()


def get_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()
    conn.close()

    return student


def get_machines():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM machines
    """)

    machines = cursor.fetchall()
    conn.close()

    return machines


def get_queue(machine_name=None):
    conn = get_connection()
    cursor = conn.cursor()

    if machine_name:
        cursor.execute("""
            SELECT * FROM laundry_queue
            WHERE machine_name = ?
            AND status = 'Waiting'
            ORDER BY join_time ASC
        """, (machine_name,))
    else:
        cursor.execute("""
            SELECT * FROM laundry_queue
            WHERE status = 'Waiting'
            ORDER BY join_time ASC
        """)

    queue = cursor.fetchall()
    conn.close()

    return queue


def add_to_queue(student_id, machine_name, estimated_wait):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if student is already waiting
    cursor.execute("""
        SELECT * FROM laundry_queue
        WHERE student_id = ?
        AND status = 'Waiting'
    """, (student_id,))

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return False, "You are already in a laundry queue."

    join_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO laundry_queue
        (student_id, machine_name, join_time, status, estimated_wait)
        VALUES (?, ?, ?, 'Waiting', ?)
    """, (
        student_id,
        machine_name,
        join_time,
        estimated_wait
    ))

    conn.commit()
    conn.close()

    return True, "Successfully joined the queue."


def complete_current_laundry(machine_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, student_id
        FROM laundry_queue
        WHERE machine_name = ?
        AND status = 'Waiting'
        ORDER BY join_time ASC
        LIMIT 1
    """, (machine_name,))

    first = cursor.fetchone()

    if not first:
        conn.close()
        return False, "No student is waiting for this machine."

    queue_id = first[0]

    cursor.execute("""
        UPDATE laundry_queue
        SET status = 'Completed'
        WHERE id = ?
    """, (queue_id,))

    conn.commit()
    conn.close()

    return True, "Laundry marked as completed."


def remove_from_queue(queue_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE laundry_queue
        SET status = 'Cancelled'
        WHERE id = ?
    """, (queue_id,))

    conn.commit()
    conn.close()


def get_all_queue_data():
    conn = get_connection()

    query = """
        SELECT
            q.id,
            q.student_id,
            s.name,
            s.room_no,
            q.machine_name,
            q.join_time,
            q.status,
            q.estimated_wait
        FROM laundry_queue q
        LEFT JOIN students s
        ON q.student_id = s.student_id
        ORDER BY q.join_time DESC
    """

    import pandas as pd

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df