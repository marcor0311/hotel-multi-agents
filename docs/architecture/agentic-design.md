# Diseño agéntico

El agente principal tiene identidad única y responsabilidad de conversación. El modelo interpreta solo lo necesario; autorización, disponibilidad, horarios, cálculo de tarifas, inventario, sensores, pagos de prueba, idempotencia y transiciones se resuelven en código determinista. No hay un agente por canal o por API.

La solicitud pasa por validación y permisos antes de ejecutar herramientas. Respuestas de herramientas y proveedores son datos no confiables y nunca pueden cambiar políticas. Se exige confirmación explícita para transacciones aplicables. Estado y memoria se limitan al contexto necesario y autorizado.

## Flujo de grafo previsto

`normalize → resolve_active_stay → authorize → interpret/route → tool | confirm | escalate → format_response`

Los errores tipados conducen a respuesta segura o escalamiento; no se reintenta automáticamente una escritura sin idempotencia. La persistencia de checkpointer, retención y evaluación quedan para Fase 1/6.
