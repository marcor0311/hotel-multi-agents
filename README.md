# Luxury Hotel AI Concierge

Un concierge agéntico para un hotel ficticio de cinco estrellas en Los Ángeles, diseñado para atender a huéspedes con una estancia activa y reducir tareas operativas repetitivas, especialmente fuera del horario habitual.

## Problema

Los huéspedes necesitan coordinar servicios del hotel y solicitudes complejas sin repetir su contexto ni contactar a varios proveedores por separado. El concierge mantiene la conversación, comparte solo la información necesaria y coordina agentes especializados; los servicios de pago requieren aprobación explícita del huésped.

## Agentes

- **Concierge Agent:** Es el punto de contacto del huésped y coordina el contexto autorizado, las herramientas, los agentes especializados, las aprobaciones y el escalamiento a recepción.
- **Personal Trainer Booking Agent (prioridad 1):** Busca entrenadores registrados según especialidad, tarifa y preferencias, los llama dentro del horario permitido hasta encontrar disponibilidad y presenta la opción al huésped para aprobación antes de registrar una reserva y un pago simulados; solo puede contactarlos por teléfono, nunca por WhatsApp ni correo.
- **Travel Planning Agent (prioridad 2):** Coordina vuelos, conexiones y transporte según horarios, presupuesto y preferencias, propone alternativas ante conflictos y usa herramientas MCP para consultas y reservas simuladas.
- **Security Provider Agent (externo):** Representa al proveedor ficticio e independiente de seguridad, con el que el concierge colabora mediante A2A después de verificar el endpoint y la autenticación.

Los agentes especializados son componentes internos coordinados por el Concierge Agent y reciben únicamente el contexto necesario para cada solicitud; no se implementa aquí lógica funcional.
