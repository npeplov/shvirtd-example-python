def main():
    # Настройки подключения
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'db',  # Это имя сервиса из docker-compose
        'database': 'test_db',
    }

    try:
        connection = mysql.connector.connect(**config)
        print("Подключение успешно!")
        # Здесь можете добавить логику работы с БД
    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    main()