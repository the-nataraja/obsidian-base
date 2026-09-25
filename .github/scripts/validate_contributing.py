import os
import sys
import re
import yaml

# --- НАСТРОЙКИ ---
ALLOWED_PREFIXES = ['КП', 'ЛБ', 'ПР', 'ЭКЗ']
ALLOWED_TAGS = ['#экзамен', '#важно', '#дописать', '#вопрос']
# Презентации теперь полностью под запретом
BANNED_EXTENSIONS = ['.mp3', '.mp4', '.zip', '.rar', '.7z', '.exe', '.bin', '.pptx', '.ppt']
# Файлы, при изменении которых нужно выдать желтое предупреждение (без блокировки PR)
WARNING_FILES = ['.gitignore', 'contributing.md']

def check_file(filepath):
    errors = []
    warnings = []
    
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    # 1. Проверка на системные файлы (ПРЕДУПРЕЖДЕНИЯ)
    if filename in WARNING_FILES:
        warnings.append(f"::warning title=Внимание! Изменен системный файл::Администратор, обратите внимание: изменен файл {filepath}")

    # 2. Проверка запрещенных форматов (ОШИБКИ)
    if ext in BANNED_EXTENSIONS:
        errors.append(f"Файл {filename}: Формат {ext} строго запрещен для загрузки.")
        return errors, warnings # Дальше не проверяем

    # Если это не Markdown, игнорируем его для дальнейших проверок
    if ext != '.md':
        return errors, warnings

    path_parts = filepath.split(os.sep)

    # 3. Проверка структуры папок
    if len(path_parts) > 1 and "семестр" in path_parts[0].lower():
        if len(path_parts) >= 4:
            folder_lvl3 = path_parts[2]
            if not re.match(r'^\d+_', folder_lvl3):
                errors.append(f"Путь '{filepath}': Папка '{folder_lvl3}' должна начинаться с цифры и подчеркивания ('1_', '2_').")

    # 4. Проверка имени файла (игнорируем индексы с '_')
    if not filename.startswith('_'):
        prefix_pattern = '|'.join(ALLOWED_PREFIXES)
        
        # Разбиваем имя на 3 части: Префикс, Номер, Тема
        match = re.match(rf'^({prefix_pattern}) (\d{{2}}) - (.*)\.md$', filename)
        
        if not match:
            errors.append(f"Имя файла '{filename}': Нарушен базовый формат. Должно быть '[ПРЕФИКС] [ДВЕ ЦИФРЫ] - [Тема].md'.")
        else:
            # Извлекаем саму тему (всё, что после дефиса и до .md)
            _, _, topic = match.groups()
            
            # Строго проверяем тему: только маленькие буквы, цифры, минус и подчеркивание. Никаких пробелов!
            if not re.match(r'^[a-zа-яё0-9_-]+$', topic):
                errors.append(
                    f"Имя файла '{filename}': Ошибка в теме '{topic}'. "
                    f"Тема должна быть ТОЛЬКО строчными (маленькими) буквами, "
                    f"а вместо пробелов используйте подчеркивания '_' или дефисы '-'."
                )

    # 5. Чтение и парсинг содержимого
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        errors.append(f"Файл '{filename}': Сохранен не в кодировке UTF-8. Пересохраните файл.")
        return errors, warnings
    except Exception as e:
        errors.append(f"Файл '{filename}': Невозможно прочитать ({e}).")
        return errors, warnings

    # Разделяем YAML и тело (поддерживает \n и \r\n)
    yaml_match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL)
    if not yaml_match:
        errors.append(f"Файл '{filename}': Отсутствует или сломана YAML шапка (блоки ---).")
    else:
        yaml_text, body_text = yaml_match.groups()
        
        # Проверка YAML
        try:
            metadata = yaml.safe_load(yaml_text)
            if not metadata: 
                metadata = {}
            
            # Дата
            if 'date' not in metadata:
                errors.append(f"Файл '{filename}': В шапке нет поля 'date'.")
            elif not re.match(r'^\d{4}-\d{2}-\d{2}$', str(metadata.get('date', ''))):
                errors.append(f"Файл '{filename}': Дата должна быть в формате ГГГГ-ММ-ДД.")
            
            # Теги автора
            tags = metadata.get('tags', [])
            if not tags or not isinstance(tags, list):
                errors.append(f"Файл '{filename}': В шапке нет списка 'tags'.")
            else:
                has_author = any(str(tag).startswith('author/') for tag in tags)
                if not has_author:
                    errors.append(f"Файл '{filename}': Отсутствует обязательный тег 'author/username'.")
        except yaml.YAMLError:
            errors.append(f"Файл '{filename}': Синтаксическая ошибка в YAML шапке (неверные отступы или спецсимволы).")

        # Проверка тегов в теле (запрет тематических)
        body_tags = re.findall(r'(?<!\S)#[a-zA-Zа-яА-Я0-9_-]+', body_text)
        for tag in body_tags:
            if tag.lower() not in ALLOWED_TAGS:
                errors.append(f"Файл '{filename}': Тематические теги запрещены. Найден: '{tag}'.")

    return errors, warnings

if __name__ == "__main__":
    all_errors = []
    files_to_check = []

    # Читаем список файлов из временного документа
    try:
        with open('changed_files.txt', 'r', encoding='utf-8') as f:
            # Читаем строки и удаляем лишние пробелы/переносы по краям
            files_to_check = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Файл со списком изменений не найден. Проверка пропущена.")
        sys.exit(0)

    # Если файлов нет, завершаем успешно
    if not files_to_check:
        print("✅ Нет файлов для проверки (или изменены только не-markdown файлы).")
        sys.exit(0)

    for filepath in files_to_check:
        # Игнорируем удаленные файлы
        if not os.path.exists(filepath):
            continue
            
        if os.path.isfile(filepath):
            errors, warnings = check_file(filepath)
            all_errors.extend(errors)
            
            # Печатаем предупреждения
            for warning in warnings:
                print(warning)

    if all_errors:
        print("\n❌ НАЙДЕНЫ ОШИБКИ ОФОРМЛЕНИЯ:\n")
        for error in all_errors:
            print(f" - {error}")
        print("\nПожалуйста, исправьте эти ошибки и обновите Pull Request.")
        sys.exit(1)
    else:
        print("✅ Все файлы соответствуют стандарту contributing.md!")
        sys.exit(0)
