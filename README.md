# 🧬 Bio-Trends: Journey to Fight Aging with AI

My learning journey from zero to using artificial intelligence for anti-aging research

## 📖 این Repo چیه؟

یک مسیر یادگیری ساختاریافته و پروژه‌محور برای:
- یادگیری Machine Learning و Deep Learning
- کار با داده‌های زیستی و پزشکی
- تحقیق در حوزه longevity و anti-aging

## 🎯 الان کجام؟

→ **ببین:** [`00-ROADMAP/current-phase.md`](00-ROADMAP/current-phase.md)

## 📋 قدم بعدی چیه؟

→ **ببین:** [`00-ROADMAP/next-steps.md`](00-ROADMAP/next-steps.md)

## 📚 راهنماها

- [چطوری شروع کنم؟](01-GUIDES/how-to-start.md)
- [مشکل دارم!](01-GUIDES/debugging-guide.md) (به زودی)

## 📊 پیشرفت من

→ **ببین:** [`02-LOGS/week-01.md`](02-LOGS/week-01.md)

## 🗂️ ساختار Repo
```
bio-trends/
├── 00-ROADMAP/        # نقشه کلی و وضعیت فعلی
├── 01-GUIDES/         # راهنماهای قدم‌به‌قدم
├── 02-LOGS/           # گزارش روزانه/هفتگی
├── 03-CONTEXT-FOR-AI.md  # برای وقتی که چت لیمیت می‌خوره
└── projects/          # پروژه‌های واقعی (به زودی)
```

## 🚀 پروژه‌های برنامه‌ریزی شده

1. **Health Data Analyzer** - تحلیل داده‌های سلامت شخصی
2. **Disease Classifier** - کلاسیفای بیماری‌های مرتبط با سن
3. **Biological Age Predictor** - پیش‌بینی سن بیولوژیک
4. **Cell Image Analysis** - تحلیل تصاویر میکروسکوپی
5. **Longevity Predictor** - مدل پیش‌بینی طول عمر
6. **Anti-Aging Recommender** - سیستم توصیه مداخلات

## 💡 فلسفه این Repo

- **Self-Documenting:** همه چیز مستند است، حتی وقتی من نیستم
- **Progressive:** از ساده به پیچیده، قدم‌به‌قدم
- **Practical:** همه چیز پروژه‌محور و کاربردی
- **Open:** همه می‌تونند ببینند و یاد بگیرند

---

**Last Update:** 2025-01-16  
**Status:** 🔨 در حال ساخت
```

---

## ✅ قدم 3: یک .gitignore درست کن

فایل `.gitignore` رو Edit کن یا بساز:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# Jupyter
.ipynb_checkpoints
*.ipynb

# Data
*.csv
*.xlsx
*.h5
*.pkl
data/raw/
data/processed/

# Models
models/*.pt
models/*.h5
*.pth

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Personal
TODO_personal.md
secrets/ 
