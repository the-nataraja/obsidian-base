import os
import re
import sys
from pathlib import PurePosixPath

import yaml

ALLOWED_PREFIXES = ["КП", "ЛБ", "ПР", "ЭКЗ"]
ALLOWED_TAGS = ["#экзамен", "#важно", "#дописать", "#вопрос"]
ALLOWED_EXTENSIONS = {".md", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".pdf"}

MAX_FILE_SIZE_MB = 10
WARNING_FILES = [".gitignore", "contributing.md"]


def check_file(filepath):
    errors = []
    warnings = []

    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    if filename in WARNING_FILES:
        warnings.append(
            f"::warning title=Изменен системный файл::Обратите внимание на изменение {filepath}"
        )

    file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        errors.append(
            f"[{filename}] Превышен размер файла: {file_size_mb:.2f} МБ (лимит {MAX_FILE_SIZE_MB} МБ)."
        )

    if ext not in ALLOWED_EXTENSIONS:
        errors.append(f"[{filename}] Недопустимое расширение '{ext}'.")
        return errors, warnings

    if ext != ".md":
        return errors, warnings

    # Git diff всегда возвращает пути с прямым слэшем (независимо от ОС)
    path_parts = PurePosixPath(filepath).parts

    if len(path_parts) > 1 and "семестр" in path_parts[0].lower():
        if len(path_parts) >= 4:
            folder_lvl3 = path_parts[2]
            if not re.match(r"^\d+_", folder_lvl3):
                errors.append(
                    f"[{filepath}] Папка '{folder_lvl3}' должна начинаться с цифры и подчеркивания (например '1_')."
                )

    if not filename.startswith("_"):
        prefix_pattern = "|".join(ALLOWED_PREFIXES)
        match = re.match(rf"^({prefix_pattern}) (\d{{2}}) - (.*)\.md$", filename)

        if not match:
            errors.append(
                f"[{filename}] Неверный формат имени. Ожидается: '[ПРЕФИКС] [XX] - [Тема].md'."
            )
        else:
            _, _, topic = match.groups()
            if not re.match(r"^[a-zа-яё0-9_-]+$", topic):
                errors.append(
                    f"[{filename}] Ошибка в теме '{topic}'. Разрешены только строчные буквы, цифры, '_' и '-'."
                )

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        errors.append(f"[{filename}] Файл не в кодировке UTF-8.")
        return errors, warnings
    except Exception as e:
        errors.append(f"[{filename}] Ошибка чтения: {e}")
        return errors, warnings

    yaml_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)", content, re.DOTALL)
    if not yaml_match:
        errors.append(f"[{filename}] Отсутствует или повреждена YAML шапка.")
    else:
        yaml_text, body_text = yaml_match.groups()

        try:
            metadata = yaml.safe_load(yaml_text) or {}

            if "date" not in metadata:
                errors.append(f"[{filename}] Отсутствует поле 'date'.")
            elif not re.match(r"^\d{4}-\d{2}-\d{2}$", str(metadata.get("date", ""))):
                errors.append(
                    f"[{filename}] Поле 'date' должно быть в формате YYYY-MM-DD."
                )

            tags = metadata.get("tags", [])
            if not tags or not isinstance(tags, list):
                errors.append(f"[{filename}] Отсутствует массив 'tags'.")
            else:
                has_author = any(str(tag).startswith("author/") for tag in tags)
                if not has_author:
                    errors.append(
                        f"[{filename}] Отсутствует обязательный тег 'author/username'."
                    )
        except yaml.YAMLError:
            errors.append(f"[{filename}] Синтаксическая ошибка в YAML.")

        # Вырезаем блоки кода для предотвращения ложных срабатываний парсера тегов
        clean_body = re.sub(r"```.*?```", "", body_text, flags=re.DOTALL)
        clean_body = re.sub(r"`.*?`", "", clean_body)

        body_tags = re.findall(r"(?<!\S)#[a-zA-Zа-яА-Я0-9_-]+", clean_body)
        for tag in body_tags:
            if tag.lower() not in ALLOWED_TAGS:
                errors.append(f"[{filename}] Запрещенный тег '{tag}' в теле документа.")

    return errors, warnings


if __name__ == "__main__":
    all_errors = []
    files_to_check = []

    try:
        with open("changed_files.txt", "r", encoding="utf-8") as f:
            files_to_check = [line.strip().strip('"') for line in f if line.strip()]
    except FileNotFoundError:
        print("Файл changed_files.txt не найден. Проверка пропущена.")
        sys.exit(0)

    if not files_to_check:
        print("Нет файлов для проверки.")
        sys.exit(0)

    print(f"Запуск проверки для {len(files_to_check)} файла(ов)...")
    for filepath in files_to_check:
        if not os.path.exists(filepath) or not os.path.isfile(filepath):
            continue

        errors, warnings = check_file(filepath)
        all_errors.extend(errors)

        for warning in warnings:
            print(warning)

    if all_errors:
        print(f"\n[!] ОШИБКА ВАЛИДАЦИИ (найдено проблем: {len(all_errors)}):\n")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("\n[OK] Проверка успешно пройдена.")
        sys.exit(0)
