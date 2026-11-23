# Diseño agéntico

El Concierge Agent mantiene la conversación y puede delegar a un especialista con un contrato interno tipado. El modelo puede interpretar la intención, comparar opciones o proponer una acción. El backend aplica las políticas de autorización y verifica confirmaciones, reglas de negocio e idempotencia antes de ejecutar una operación.

Cada especialista recibe los campos y permisos mínimos para la operación. Las respuestas de herramientas y proveedores se validan y se tratan como datos. Las decisiones de autorización se aplican en el backend con independencia de lo que contenga una respuesta externa. El concierge solicita confirmación explícita al huésped cuando corresponda, y Human Handoff deriva a recepción las solicitudes que requieren intervención humana.

## Flujo de grafo previsto

`normalizar → resolver estancia → interpretar y enrutar → autorizar operación → delegar o escalar → responder`

Si una operación requiere confirmación, el grafo pausa la ejecución y verifica la autorización al retomarla. Los errores tipados permiten informar al huésped o escalar según el caso. Las escrituras requieren idempotencia para admitir reintentos automáticos. [Orquestación](orchestration.md)
