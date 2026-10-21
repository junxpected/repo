import os
import subprocess
import sys

name = input("Введіть назву файлу з програмою (наприклад, finite.py): ")

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, name)

if not os.path.exists(path):
    print("Файл не знайдено:", path)
else:
    try:
        result = subprocess.run([sys.executable, path], timeout=10, stdin=subprocess.DEVNULL)
        if result.returncode == 0:
            print("Програма завершилась за 10 секунд")
        else:
            print("Програма завершилась з помилкою")
    except subprocess.TimeoutExpired:
        print("Програма не завершилась за 10 секунд")