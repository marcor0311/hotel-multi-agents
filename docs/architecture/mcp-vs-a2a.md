# MCP frente a A2A

| Necesidad | Mecanismo | Motivo |
|---|---|---|
| Consultar horario, inventario, folio o estado de robot | Herramienta/recurso MCP | Capacidad determinista bajo control del hotel |
| Crear pedido interno | Herramienta MCP con autorización e idempotencia | Operación acotada dentro del dominio hotelero |
| Contratar proveedor autónomo con lógica propia | A2A | Colaboración entre agentes independientes |
| Cambiar de canal | Adaptador de canal | El canal no crea un agente nuevo |

MCP no consume tokens por sí mismo. A2A no justifica un agente para envolver una API simple. La Agent Card anuncia capacidades y requisitos; se verifica la identidad por canal autenticado y política de confianza, no por presencia del documento. SDK y revisión exacta del protocolo A2A son ADR pendiente.
