# DS_AI_Growth

90-дневный практический план развития в сторону Data Science / Applied AI / RAG / AI Risk.

## Цель

Собрать доказательную базу навыков:
- SQL
- Python / pandas
- ML basics
- NLP / embeddings
- RAG evaluation
- AI Risk / Governance

## Формат

Короткие практические занятия по 20–30 минут.
Каждый день должен давать артефакт: файл, код, запрос, таблицу, README, метрику или коммит.

## Фазы

1. Days 1–30: SQL, Python/pandas, Git
2. Days 31–60: ML basics, NLP, embeddings
3. Days 61–90: RAG 2.0, evaluation, AI Risk

## Текущий мини-проект: AI-assisted data pipeline

В рамках Phase 01 собран небольшой пайплайн обработки данных, который показывает рабочий подход к AI-assisted data workflow.

Пайплайн выполняет:

* очистку грязных данных по заказам;
* фильтрацию валидных оплаченных заказов;
* объединение заказов с данными пользователей;
* автоматическую проверку результата;
* формирование JSON-отчёта о качестве данных;
* запуск всего процесса одной командой.

Главный запуск:

```bash
python phase_01_base/day_13_pipeline_runner/run_pipeline.py
```

Основные файлы:

```text
phase_01_base/day_10_ai_assisted_pandas_review/agent_solution.py
phase_01_base/day_11_data_validation/validate_cleaned_orders.py
phase_01_base/day_12_data_quality_report/quality_report.py
phase_01_base/day_13_pipeline_runner/run_pipeline.py
```

Выходные артефакты:

```text
phase_01_base/day_10_ai_assisted_pandas_review/cleaned_paid_orders.csv
phase_01_base/day_12_data_quality_report/quality_report.json
```

Ключевая идея: AI-generated код нельзя считать корректным только потому, что он запускается. Его нужно читать, проверять, валидировать и документировать.

Этот мини-проект закрепляет связку:

```text
AI-generated code → review → validation → quality report → documented pipeline
```
