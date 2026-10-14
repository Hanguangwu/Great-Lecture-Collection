#!/usr/bin/env python3
"""根据 src/ 下的年份文件夹自动生成 src/SUMMARY.md。

规则：
- 前言始终位于最前
- 年份文件夹（4 位数字命名）按年份逆序排列
- 年份内 .md 文件按文件名排序，标题取文件名（不含扩展名）
- 每次全量重写 SUMMARY.md，请勿手工编辑该文件
"""

import re
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
SUMMARY_FILE = SRC_DIR / "SUMMARY.md"
YEAR_DIR_PATTERN = re.compile(r"^\d{4}$")


def generate_summary() -> str:
    lines = ["# Summary", "", "- [前言](./前言.md)"]

    year_dirs = sorted(
        (d for d in SRC_DIR.iterdir() if d.is_dir() and YEAR_DIR_PATTERN.match(d.name)),
        key=lambda d: d.name,
        reverse=True,
    )

    for year_dir in year_dirs:
        md_files = sorted(
            year_dir.glob("*.md"),
            key=lambda f: f.name,
        )
        if not md_files:
            continue
        lines.append("")
        lines.append(f"## {year_dir.name}")
        lines.append("")
        for md_file in md_files:
            title = md_file.stem
            rel_path = f"./{year_dir.name}/{md_file.name}"
            lines.append(f"- [{title}]({rel_path})")

    return "\n".join(lines) + "\n"


def main() -> None:
    content = generate_summary()
    SUMMARY_FILE.write_text(content, encoding="utf-8")
    year_count = content.count("\n## ")
    link_count = sum(1 for line in content.splitlines() if line.startswith("- ["))
    print(f"已生成 {SUMMARY_FILE}")
    print(f"年份分部: {year_count} 个，条目总数: {link_count} 条（含前言）")


if __name__ == "__main__":
    sys.exit(main())
