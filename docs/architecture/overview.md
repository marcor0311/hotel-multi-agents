# Arquitectura del concierge

El **Concierge Agent** mantiene la conversación con el huésped y coordina a los especialistas. El [diagrama de agentes del README](../../README.md#agentes) muestra las cuatro áreas de servicio y las conexiones con MCP, recepción y el proveedor externo. En **Fase 0**, la API expone el health check y el repositorio contiene contratos de datos y fixtures. La atención por voz, la orquestación y las integraciones externas están pendientes.

## Del huésped al concierge

Los [adaptadores de canal](channel-abstraction.md) convierten los mensajes de voz, WhatsApp o web a un formato común. La API valida la entrada y los metadatos de autenticación. El concierge resuelve la estancia activa, usa el contexto autorizado y responde por el mismo canal. Los especialistas devuelven sus resultados al concierge, que presenta las opciones y recoge las confirmaciones del huésped.

## Delegación interna

Los grupos del diagrama organizan los agentes por responsabilidad dentro del mismo backend.

| Grupo | Solicitudes que recibe |
|---|---|
| Viajes y destinos | Vuelos, transporte ejecutivo y recomendaciones locales |
| Experiencias | Entrenadores personales, reservas de restaurantes y servicios de spa |
| Servicios del hotel | Información del hotel, suministros, pedidos y entregas con robot |
| Cuentas y asistencia | Pagos de prueba, consultas de folio y traspasos a recepción |

Cada delegación lleva una operación, los datos mínimos para ejecutarla y los permisos aplicables a la estancia. El especialista devuelve un resultado estructurado, como una cotización, un estado o una solicitud de aprobación. El backend autoriza cada acción y valida las respuestas de las herramientas y los proveedores como datos externos. [Diseño agéntico](agentic-design.md) y [Seguridad y privacidad](security.md).

## Herramientas MCP, A2A y recepción

| Conexión del diagrama | Responsabilidad |
|---|---|
| **Herramientas MCP** | El concierge y los especialistas las invocan para operaciones autorizadas, como consultar inventario, buscar vuelos o registrar pedidos. Los adaptadores conectan con fixtures o proveedores e identifican el modo de ejecución. |
| **A2A con Security Provider Agent** | El concierge verifica la identidad y el endpoint del proveedor independiente, y envía únicamente los datos necesarios para la solicitud. |
| **Recepción** | Human Handoff deriva las solicitudes que requieren atención humana. El concierge comunica el estado del traspaso según lo que confirme la integración de telefonía. |

[MCP frente a A2A](mcp-vs-a2a.md) y [Escalamiento a recepción](../workflows/human-handoff.md).

## Flujo de solicitud

1. El huésped llama para preguntar si su vuelo va retrasado.
2. El concierge valida la estancia y obtiene el número de vuelo y la fecha del itinerario autorizado o del propio huésped.
3. El Flights Agent recibe una consulta de lectura, verifica el estado mediante el adaptador de vuelos y devuelve el resultado con fuente y hora de consulta.
4. El concierge comunica el estado disponible.

Si el huésped pide reservar un vuelo, el concierge presenta el itinerario y el precio total y recoge la confirmación explícita antes de delegar la reserva. Cuando la política exige aprobación humana, la solicitud queda pendiente hasta que el equipo autorizado la revise. [Reserva y rastreo de vuelos](../workflows/flight-booking.md) y [Reglas de escalamiento](../business/escalation-rules.md).

## Implementación prevista

La API aloja un monolito modular. LangGraph es la opción propuesta para coordinar el estado conversacional, la delegación y las pausas por confirmación o aprobación. El dominio aplica políticas, permisos y reglas de negocio. Los puertos definen las operaciones disponibles y los adaptadores las conectan a fuentes locales o proveedores. El SDK y el protocolo de las integraciones se decidirán según cada caso. [Orquestación](orchestration.md) y [Decisiones](../decisions/README.md).

## Estado y persistencia

El contexto conversacional recuperable contempla el ID de conversación, el canal, el ID de estancia y los resultados mínimos para continuar. Los secretos, PAN, CVV y expedientes quedan fuera del estado del modelo. PostgreSQL es el destino previsto para las entidades de negocio y los eventos de auditoría. El almacenamiento de checkpoints y los plazos de retención están pendientes. La auditoría de negocio se mantiene separada de los logs técnicos.
