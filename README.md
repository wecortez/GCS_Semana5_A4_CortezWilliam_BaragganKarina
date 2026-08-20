# API de Inventario - Mini Juguetería

Proyecto académico simulado para aplicar control de versiones, registro de
estados de configuración y trazabilidad mediante Git y GitHub.

## Funcionalidades

- Listar juguetes mediante `GET /products`.
- Agregar juguetes mediante `POST /products`.

## Integrantes y responsabilidades

- William Cortez: estructura inicial y función `list_products()`.
- Karina Barragán: función `add_product()` y prueba del inventario.

## Cómo ejecutar

No se requiere despliegue real. El código representa una API de inventario
simplificada para la práctica de Gestión de Configuración del Software.

## Convenciones

- Ramas: `feature/`, `fix/`, `docs/` y `release/`.
- Commits: `chore`, `docs`, `feat` o `fix`.
- Trazabilidad: los cambios de corrección usarán una referencia `ISSUE-xx`.
- Versiones: SemVer con formato `vMAJOR.MINOR.PATCH`.