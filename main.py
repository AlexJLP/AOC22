from datetime import datetime
import importlib

if __name__ == '__main__':
    day = datetime.now().strftime('%#d')
    print(f"AOC Day {day}".center(20,'#'))
    importlib.import_module(f"day{day}")


