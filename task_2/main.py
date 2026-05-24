def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

        return cats

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except Exception as e:
        print("Помилка при читанні файлу:", e)
        return []
    
cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)