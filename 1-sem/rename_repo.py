#!/usr/bin/env python3
from __future__ import annotations

import logging
import os
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "rename_errors.log"

USE_COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ


def c(text: str, code: str) -> str:
    if not USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


BOLD = "1"
DIM = "2"
RED = "31"
GREEN = "32"
YELLOW = "33"
CYAN = "36"
MAGENTA = "35"


@dataclass(frozen=True)
class RenameTask:
    rel_src: Path
    new_name: str
    title: str
    is_dir: bool


# Порядок важен: родительские папки идут раньше вложенных элементов.
TASKS: list[RenameTask] = [
    # --- math / 1-LEC_MakarovaOV / 0_topics_review / 1_problems / 101 ---
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101А_алгоритм_евклида_и_взаимная_простота.md"),
        "SEM-101A_euclidean_algorithm_and_coprimality.md",
        "SEM-101A алгоритм евклида и взаимная простота",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101А_факторизация_и_проверка_простоты.md"),
        "SEM-101A_factorization_and_primality_testing.md",
        "SEM-101A факторизация и проверка простоты",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101А_целая_часть_и_остаток.md"),
        "SEM-101A_floor_and_remainder.md",
        "SEM-101A целая часть и остаток",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101B_несократимость_дроби.md"),
        "SEM-101B_fraction_irreducibility.md",
        "SEM-101B несократимость дроби",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101B_основная_теорема_арифметики.md"),
        "SEM-101B_fundamental_theorem_of_arithmetic.md",
        "SEM-101B основная теорема арифметики",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101B_расширенный_алгоритм_евклида.md"),
        "SEM-101B_extended_euclidean_algorithm.md",
        "SEM-101B расширенный алгоритм евклида",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101C_бесконечность_простых_вида_4k_плюс_3.md"),
        "SEM-101C_infinitude_of_primes_4k_plus_3.md",
        "SEM-101C бесконечность простых вида 4k плюс 3",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101C_евклид_в_показателях_степеней.md"),
        "SEM-101C_euclid_in_exponents.md",
        "SEM-101C евклид в показателях степеней",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101C_сложность_факторизации_и_евклида.md"),
        "SEM-101C_factorization_and_euclid_complexity.md",
        "SEM-101C сложность факторизации и евклида",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101D_диофантово_уравнение_с_ограничениями.md"),
        "SEM-101D_constrained_diophantine_equation.md",
        "SEM-101D диофантово уравнение с ограничениями",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101D_метод_факторизации_ферма_и_rsa.md"),
        "SEM-101D_fermat_factorization_and_rsa.md",
        "SEM-101D метод факторизации ферма и rsa",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/1_problems/101/ПР-101D_формула_лежандра_и_делимость_факториала.md"),
        "SEM-101D_legendres_formula_and_factorial_divisibility.md",
        "SEM-101D формула лежандра и делимость факториала",
        False,
    ),

    # --- math / 1-LEC_MakarovaOV / 0_topics_review / 2_solutions / 101 ---
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101А_факторизация_и_проверка_простоты.md"),
        "SOL-101A_factorization_and_primality_testing.md",
        "SOL-101A факторизация и проверка простоты",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101А_целая_часть_и_остаток.md"),
        "SOL-101A_floor_and_remainder.md",
        "SOL-101A целая часть и остаток",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101B_несократимость_дроби.md"),
        "SOL-101B_fraction_irreducibility.md",
        "SOL-101B несократимость дроби",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101B_основная_теорема_арифметики.md"),
        "SOL-101B_fundamental_theorem_of_arithmetic.md",
        "SOL-101B основная теорема арифметики",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101B_расширенный_алгоритм_евклида.md"),
        "SOL-101B_extended_euclidean_algorithm.md",
        "SOL-101B расширенный алгоритм евклида",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101C_бесконечность_простых_вида_4k_плюс_3.md"),
        "SOL-101C_infinitude_of_primes_4k_plus_3.md",
        "SOL-101C бесконечность простых вида 4k плюс 3",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101C_евклид_в_показателях_степеней.md"),
        "SOL-101C_euclid_in_exponents.md",
        "SOL-101C евклид в показателях степеней",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101C_сложность_факторизации_и_евклида.md"),
        "SOL-101C_factorization_and_euclid_complexity.md",
        "SOL-101C сложность факторизации и евклида",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101D_диофантово_уравнение_с_ограничениями.md"),
        "SOL-101D_constrained_diophantine_equation.md",
        "SOL-101D диофантово уравнение с ограничениями",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101D_метод_факторизации_ферма_и_rsa.md"),
        "SOL-101D_fermat_factorization_and_rsa.md",
        "SOL-101D метод факторизации ферма и rsa",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/2_solutions/101/ОТ-101D_формула_лежандра_и_делимость_факториала.md"),
        "SOL-101D_legendres_formula_and_factorial_divisibility.md",
        "SOL-101D формула лежандра и делимость факториала",
        False,
    ),

    # --- math / 1-LEC_MakarovaOV / 0_topics_review ---
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/0_план_исб-126.md"),
        "0_plan_iass-126.md",
        "0 план исб-126",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/КП-101_натуральные_и_целые_числа.md"),
        "LEC-101_natural_and_integer_numbers.md",
        "LEC-101 натуральные и целые числа",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/0_topics_review/КП-301_векторы.md"),
        "LEC-301_vectors.md",
        "LEC-301 векторы",
        False,
    ),

    # --- math / 1-LEC_MakarovaOV ---
    RenameTask(
        Path("math/1-LEC_MakarovaOV/КП 01 - делимость_целых_чисел_и_алгоритм_евклида.md"),
        "LEC-01_integer_divisibility_and_euclidean_algorithm.md",
        "LEC-01 делимость целых чисел и алгоритм евклида",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/КП 02 - рациональные_и_вещественные_числа.md"),
        "LEC-02_rational_and_real_numbers.md",
        "LEC-02 рациональные и вещественные числа",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/КП 03 - комплексные_числа.md"),
        "LEC-03_complex_numbers.md",
        "LEC-03 комплексные числа",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/КП 04 - группы.md"),
        "LEC-04_groups.md",
        "LEC-04 группы",
        False,
    ),
    RenameTask(
        Path("math/1-LEC_MakarovaOV/КП 05 - кольца_и_подкольца.md"),
        "LEC-05_rings_and_subrings.md",
        "LEC-05 кольца и подкольца",
        False,
    ),

    # --- physics (только папки и их index.md) ---
    RenameTask(
        Path("physics/1_лекции (Малышева ДА)"),
        "1-LEC_MalyshevaDA",
        "1-LEC Малышева Д.А.",
        True,
    ),
    RenameTask(
        Path("physics/3_лабы (Малышева ДА)"),
        "3-LAB_MalyshevaDA",
        "3-LAB Малышева Д.А.",
        True,
    ),
    RenameTask(
        Path("physics/4_рейтинги_2026 (Малышева ДА)"),
        "4-TEST_MalyshevaDA_2026",
        "4-TEST Малышева Д.А. 2026",
        True,
    ),
    RenameTask(
        Path("physics/4_рейтинги_2026 (Малышева ДА)/1_Механика"),
        "1_mechanics",
        "1 Механика",
        True,
    ),

    # --- russian_statehood ---
    RenameTask(
        Path("russian_statehood/4_рейтинги_2026 (Кузьмин ИМ)"),
        "4-TEST_KuzminIM_2026",
        "4-TEST Кузьмин И.М. 2026",
        True,
    ),
    RenameTask(
        Path("russian_statehood/4_рейтинги_2026 (Кузьмин ИМ)/1 рейтинг"),
        "TEST-1",
        "TEST-1",
        True,
    ),
    RenameTask(
        Path("russian_statehood/4_рейтинги_2026 (Кузьмин ИМ)/1 рейтинг/понятия.md"),
        "concepts.md",
        "понятия",
        False,
    ),
]


HOMOGLYPHS = str.maketrans(
    {
        "А": "A",
        "В": "B",
        "С": "C",
        "Е": "E",
        "Н": "H",
        "К": "K",
        "М": "M",
        "О": "O",
        "Р": "P",
        "Т": "T",
        "Х": "X",
        "а": "a",
        "е": "e",
        "о": "o",
        "р": "p",
        "с": "c",
        "х": "x",
    }
)


def normalize_name(name: str) -> str:
    return unicodedata.normalize("NFC", name).translate(HOMOGLYPHS)


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("repo_renamer")
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8", delay=True)
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(handler)
    return logger


def resolve_parent(rel_parent: Path, renamed_dirs: dict[Path, Path]) -> Path:
    """Подменяет переименованных родителей на их актуальные пути."""
    current = Path(".")
    orig_accum = Path(".")
    for part in rel_parent.parts:
        orig_accum = orig_accum / part
        if orig_accum in renamed_dirs:
            current = renamed_dirs[orig_accum]
        else:
            current = current / part
    return current


def find_existing_entry(parent_abs: Path, expected_name: str, is_dir: bool) -> Path | None:
    """Ищет файл или папку, учитывая возможные кириллические/латинские омоглифы."""
    direct = parent_abs / expected_name
    if direct.exists() and direct.is_dir() == is_dir:
        return direct

    if not parent_abs.exists():
        return None

    target_norm = normalize_name(expected_name)
    matches = [
        entry
        for entry in parent_abs.iterdir()
        if entry.is_dir() == is_dir and normalize_name(entry.name) == target_norm
    ]
    if len(matches) == 1:
        return matches[0]
    return None


def upsert_yaml_title(md_path: Path, title: str) -> str:
    """
    Добавляет `title: ...` в самый верх YAML-шапки, если `title` ещё не задан.
    Если файла нет (актуально для index.md) — создаёт его.
    """
    if not md_path.exists():
        md_path.write_text(f"---\ntitle: {title}\n---\n", encoding="utf-8")
        return "создан index.md с title"

    raw = md_path.read_text(encoding="utf-8")
    had_bom = raw.startswith("\ufeff")
    content = raw.lstrip("\ufeff")
    newline = "\r\n" if "\r\n" in content else "\n"
    lines = content.splitlines()

    if lines and lines[0].strip() == "---":
        end_idx = None
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                end_idx = idx
                break

        if end_idx is not None:
            frontmatter = lines[1:end_idx]
            if any(re.match(r"^title\s*:", line) for line in frontmatter):
                return "title уже есть — не перезаписан"

            new_lines = [lines[0], f"title: {title}", *lines[1:]]
            result = newline.join(new_lines)
            if content.endswith(("\n", "\r")) or not content:
                result += newline
            if had_bom:
                result = "\ufeff" + result
            md_path.write_text(result, encoding="utf-8")
            return "добавлен title в начало YAML"

    # YAML-шапки нет (или она не закрыта корректно) — добавляем новую шапку сверху
    header = f"---{newline}title: {title}{newline}---{newline}"
    result = header + content
    if had_bom:
        result = "\ufeff" + result
    md_path.write_text(result, encoding="utf-8")
    return "создана YAML-шапка с title"


def prompt_decision() -> bool:
    while True:
        try:
            ans = input(c("  Принять? [Enter — да / n — нет]: ", BOLD)).strip().lower()
        except EOFError:
            return False
        if ans == "":
            return True
        if ans == "n":
            return False
        print(c("  Нажмите Enter для подтверждения или 'n' для пропуска.", YELLOW))


def main() -> int:
    logger = setup_logger()
    rejected: list[str] = []
    errors: list[str] = []
    renamed_count = 0
    renamed_dirs: dict[Path, Path] = {}

    total = len(TASKS)
    print(c(f"\nКорень: {BASE_DIR}", CYAN))
    print(c(f"Всего запланировано элементов: {total}\n", CYAN))

    try:
        for idx, task in enumerate(TASKS, start=1):
            rel_parent = resolve_parent(task.rel_src.parent, renamed_dirs)
            parent_abs = BASE_DIR / rel_parent

            src_abs = find_existing_entry(parent_abs, task.rel_src.name, task.is_dir)
            if src_abs is None:
                msg = f"Не найден путь: {rel_parent / task.rel_src.name}"
                print(c(f"[{idx:02d}/{total}] ОШИБКА: {msg}\n", RED))
                logger.error(msg)
                errors.append(msg)
                continue

            actual_rel_src = src_abs.relative_to(BASE_DIR)
            actual_rel_dst = rel_parent / task.new_name
            dst_abs = parent_abs / task.new_name

            kind = c("[ПАПКА]", MAGENTA) if task.is_dir else c("[ФАЙЛ ]", CYAN)
            yaml_target = f"{actual_rel_dst / 'index.md'}" if task.is_dir else str(actual_rel_dst)

            print(c(f"── [{idx:02d}/{total}] ", DIM) + kind)
            print(f"  {c('Было :', RED)} {actual_rel_src}")
            print(f"  {c('Станет:', GREEN)} {actual_rel_dst}")
            print(f"  {c('YAML  :', YELLOW)} {yaml_target}  ->  title: {task.title}")

            if not prompt_decision():
                print(c("  -> Пропущено\n", YELLOW))
                rejected.append(f"{actual_rel_src}  ->  {actual_rel_dst}")
                continue

            if dst_abs.exists() and dst_abs != src_abs:
                msg = f"Целевой путь уже существует: {actual_rel_dst} (исходник: {actual_rel_src})"
                print(c(f"  -> ОШИБКА: {msg}\n", RED))
                logger.error(msg)
                errors.append(msg)
                continue

            try:
                if src_abs != dst_abs:
                    src_abs.rename(dst_abs)

                if task.is_dir:
                    renamed_dirs[task.rel_src] = actual_rel_dst
                    yaml_status = upsert_yaml_title(dst_abs / "index.md", task.title)
                else:
                    yaml_status = upsert_yaml_title(dst_abs, task.title)

                renamed_count += 1
                print(c(f"  -> Готово ({yaml_status})\n", GREEN))
            except Exception as exc:
                msg = f"Ошибка при обработке '{actual_rel_src}' -> '{actual_rel_dst}': {exc}"
                print(c(f"  -> ОШИБКА: {msg}\n", RED))
                logger.exception(msg)
                errors.append(msg)

    except KeyboardInterrupt:
        print(c("\n\nПрервано пользователем (Ctrl+C).", YELLOW))

    print(c("═" * 60, DIM))
    print(c(f"Итог: переименовано {renamed_count}, пропущено {len(rejected)}, ошибок {len(errors)}", BOLD))

    if rejected:
        print(c("\nНе принятые переименования:", YELLOW))
        for item in rejected:
            print(f"  - {item}")

    if errors:
        print(c(f"\nОшибки (подробности в {LOG_FILE.name}):", RED))
        for err in errors:
            print(f"  - {err}")

    print()
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
