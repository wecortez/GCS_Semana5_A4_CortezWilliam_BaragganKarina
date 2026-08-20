# SRS v1 - Mini Juguetería

## Requisitos funcionales

### REQ-001: Listar productos

El sistema permitirá consultar todos los juguetes registrados.

### REQ-002: Agregar productos

El sistema permitirá agregar un juguete con una cantidad mayor o igual a cero.

Criterios de aceptación:

- El nombre es obligatorio.
- La cantidad no puede ser negativa.
- El producto agregado debe aparecer en el listado.

### REQ-003: Filtrar productos por fecha de ingreso

El sistema permitirá consultar los juguetes registrados en una fecha específica.

Criterios de aceptación:

- La búsqueda utilizará una fecha en formato `AAAA-MM-DD`.
- Solo se mostrarán productos cuya fecha coincida exactamente.
- Los productos sin fecha de ingreso no aparecerán en el resultado.

## Requisitos no funcionales

- RNF-001: Los cambios deben ser trazables mediante Issue, commit y Pull Request.
- RNF-002: El versionado seguirá SemVer mediante tags y changelog.
- RNF-003: Los archivos con credenciales locales no serán versionados.

## Líneas base

- `v1.0.0`: listar y agregar productos, SRS y prueba mínima.
- `v1.0.1`: corrección de seguridad para archivos de entorno.
- `v1.1.0`: filtro por fecha y controles completos de auditoría.