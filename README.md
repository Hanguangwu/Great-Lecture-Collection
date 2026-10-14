# 著名演讲合辑

基于 [mdBook](https://rust-lang.github.io/mdBook/) 的历史著名演讲收录网站，演讲按年份组织。

## 目录结构

```
src/
├── SUMMARY.md          # 目录（自动生成，请勿手工编辑）
├── 前言.md
├── 2005/
│   └── 乔布斯在斯坦福大学的演讲.md
└── YYYY/
    └── *.md
```

## 添加新演讲

在 `src/` 下新建以年份命名的文件夹（如 `src/2026/`），将演讲的 `.md` 文件放入即可。目录 `SUMMARY.md` 由 `scripts/generate_summary.py` 自动生成：前言固定在最前，年份按逆序排列。

本地可手动刷新目录：

```bash
python scripts/generate_summary.py
```

## 本地构建

```bash
mdbook serve   # 本地预览 http://localhost:3000
mdbook build   # 构建到 book/ 目录
```

构建依赖插件：`mdbook-toc`、`mdbook-katex`（见 `book.toml`）。

## 部署

使用 GitHub Actions：推送到 `main` 分支时自动构建并发布到 GitHub Pages（见 `.github/workflows/gh-pages.yml`）。需在仓库设置中将 Pages 源配置为 `gh-pages` 分支。
