# Laboratorio 3

## Tecnologías

- Python
- Playwright
- Pytest
- Pytest HTML

## Casos automatizados

1. Home
2. Login válido
3. Login inválido
4. Cart
5. Favorites
6. Sign Up

## Instalación

pip install -e .

playwright install

## Ejecutar pruebas

pytest

## Generar reporte

pytest --html=reports/report.html --self-contained-html
python -m pytest --html=report.html
## Evidencias

Las capturas se almacenan en:

screenshots/

## Reporte

reports/report.html