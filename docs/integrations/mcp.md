# Integración MCP

MCP se usará como contrato de herramientas/recursos, con esquemas versionados y validación de autorización en el servidor. Capacidades previstas: hotel, estancia, inventario, pedidos, robot, vuelos, pagos, transporte, folio y preferencias. Acciones de escritura deben validar estado e idempotencia. Ningún servidor está implementado/conectado en Fase 0.

El SDK oficial Python publica cambios mayores del SDK; confirmar API estable y protocolo soportado al iniciar Fase 2, fijar lockfile y probar compatibilidad cliente/servidor. No usar un servidor MCP como excusa para despliegue independiente.
