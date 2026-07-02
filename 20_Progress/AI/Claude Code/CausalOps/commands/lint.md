Run ruff and pyright on the memory layer and coordinator. Execute:
python -m ruff check src/memory/ src/coordinator/ tests/memory/ --output-format=concise
python -m pyright src/memory/ src/coordinator/ 2>&1 | tail -30
Report all errors. Do not auto-fix. If no errors: say "ruff: clean. pyright: clean."
