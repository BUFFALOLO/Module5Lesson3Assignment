import mysql.connector

def add_member(id, name, age):
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="gym_db"
        )
        cursor = connection.cursor()
        
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        
        connection.commit()
        print(f"Member {name} added successfully.")

    except mysql.connector.Error as err:
        if err.errno == 1062:  
            print("Error: Member with this ID already exists.")
        else:
            print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="gym_db"
        )
        cursor = connection.cursor()

        query = """
        INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))

        connection.commit()
        print(f"Workout session added successfully for member {member_id}.")

    except mysql.connector.Error as err:
        if err.errno == 1452:  
            print("Error: Invalid member ID.")
        else:
            print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def update_member_age(member_id, new_age):
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="gym_db"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        member = cursor.fetchone()

        if member:
            query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(query, (new_age, member_id))

            connection.commit()
            print(f"Member {member_id} age updated successfully to {new_age}.")
        else:
            print("Error: Member not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def delete_workout_session(session_id):
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="gym_db"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        session = cursor.fetchone()

        if session:
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))

            connection.commit()
            print(f"Workout session {session_id} deleted successfully.")
        else:
            print("Error: Session not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()