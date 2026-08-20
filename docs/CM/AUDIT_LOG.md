# Bitácora de auditoría

| ID | Hallazgo | Corrección | Evidencia | Estado |
|---:|----------|------------|-----------|--------|
| H-01 | Tag `v1.0` incompleto | Eliminado y sustituido por `v1.0.0` | Tag `v1.0.0` | Corregido |
| H-02 | Commit `63ab439` sin Issue | Se crearon commits correctivos vinculados al Issue #3 | Issue #3 y PR #5 | Corregido |
| H-03 | REQ-003 sin criterios | Se agregaron criterios de aceptación | SRS y PR #5 | Corregido |
| H-04 | REQ-003 sin implementación | Se implementó `filter_products_by_date()` | Código y prueba | Corregido |
| H-05 | Cambio directo en `main` | Se adoptó el flujo rama, revisión y PR | PR #5 | Corregido |
| H-06 | Hotfix sin Issue | El cambio fue documentado en el changelog y la auditoría | Issue #3 | Corregido |
| H-07 | Changelog sin versión ni fecha | Se reorganizó mediante versiones y fechas | CHANGELOG.md | Corregido |
| H-08 | Tag `release-1.1` inconsistente | Eliminado y sustituido por `v1.1.0` | Tag y release `v1.1.0` | Corregido |
| H-09 | `.env` bajo seguimiento | Retirado mediante `git rm --cached` | PR #4 | Corregido |
| H-10 | Sin `.env.example` | Se creó un ejemplo seguro | PR #4 | Corregido |
| H-11 | Sin regla en `.gitignore` | Se agregó `config/.env` | PR #4 | Corregido |
| H-12 | Mensaje `update stuff` | Se preservó como evidencia histórica y se aplicaron commits profesionales | Issue #3 y PR #4 | Corregido |

## Nota de integridad histórica

El commit `update stuff` no fue eliminado mediante reescritura del historial
porque ya había sido publicado. La corrección se realizó mediante un nuevo
commit trazable, conservando la evidencia original para la auditoría.