import sqlite3
from config import DB_PATH

def clear_table(table_name: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Очистка таблицы
        cursor.execute(f"DELETE FROM {table_name};")
        conn.commit()

        print(f"Таблица {table_name} успешно очищена.")
    except sqlite3.Error as e:
        print(f"Ошибка при очистке таблицы: {e}")
    finally:
        conn.close()


# Пример использования
clear_table("referral_rewards")
