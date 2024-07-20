def main():
    try:
        # Установите соединение с базой данных
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="testdb"
        )
        cursor = conn.cursor()
        
        # Пример создания таблицы
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        
        # Добавление пользователя
        cursor.execute("INSERT INTO users (name) VALUES ('John Doe')")
        conn.commit()

        # Получение пользователей
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()