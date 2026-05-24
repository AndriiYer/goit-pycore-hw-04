import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows і Unix
init(autoreset=True)


def show_directory(path: Path, indent: str = ""):
    """Рекурсивно виводить структуру директорії з кольорами."""
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/")
            show_directory(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")
    
def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії. Приклад:")
        print("python hw03.py /path/to/directory")
        sys.exit(-1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + "Помилка: шлях не існує")
        sys.exit(-1)

    if not dir_path.is_dir():
        print(Fore.RED + "Помилка: шлях не є директорією")
        sys.exit(-1)

    print(Fore.CYAN + f"Структура директорії: {dir_path}\n")
    show_directory(dir_path)


if __name__ == "__main__":
    main()
