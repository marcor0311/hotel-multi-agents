# Luxury Hotel AI Concierge

Un concierge agéntico para un hotel ficticio de cinco estrellas en Los Ángeles, diseñado para atender a huéspedes con una estancia activa y reducir tareas operativas repetitivas, especialmente fuera del horario habitual.

## Problema

Como huésped de un hotel de alto prestigio, quiero acceder a los servicios que ofrece el hotel de forma cómoda, rápida y sencilla, sin tener que averiguar a quién contactar ni repetir mi solicitud. El hotel busca facilitar ese acceso y coordinar con agilidad tareas operativas repetitivas que son importantes para la experiencia del huésped, especialmente fuera del horario habitual. El objetivo es complementar al equipo del hotel, no reemplazarlo: el personal sigue aportando criterio, atención humana y aprobación en los servicios que la requieren.

## Agentes

- **Concierge Agent:** Es el punto de contacto del huésped y coordina el contexto autorizado, los agentes especializados, las capacidades del hotel, las aprobaciones y el escalamiento a recepción.
- **Personal Trainer Booking Agent (prioridad 1):** Busca entrenadores registrados según especialidad, tarifa y preferencias, los llama dentro del horario permitido hasta encontrar disponibilidad y presenta la opción al huésped para aprobación antes de registrar una reserva y un pago simulados; solo puede contactarlos por teléfono, nunca por WhatsApp ni correo.
- **Flights Agent:** Busca y compara vuelos e itinerarios según horarios, presupuesto y preferencias, propone alternativas ante conflictos y gestiona reservas simuladas.
- **Uber / Executive Transportation Agent:** Consulta disponibilidad y coordina transporte ejecutivo simulado.
- **Stripe Payments Agent:** Coordina pagos de prueba mediante Stripe Test Mode y solo los confirma tras la autorización explícita del huésped.
- **Security Provider Agent (externo):** Representa al proveedor ficticio e independiente de seguridad, con el que el concierge colabora mediante A2A después de verificar el endpoint y la autenticación.
- **Hotel Information Agent:** Responde preguntas sobre instalaciones, políticas, servicios y horarios y disponibilidad de limpieza general a partir de información estructurada del hotel.
- **Guest Supplies Agent:** Gestiona solicitudes permitidas de suministros y comprueba el inventario disponible.
- **Room Service Agent:** Consulta el menú, registra pedidos simulados y comunica su estado según el horario del servicio.
- **Dining & Reservations Agent:** Consulta la red de restaurantes del hotel, coordina preferencias y disponibilidad y prepara solicitudes de reserva, que requieren aprobación humana antes de confirmarse.
- **Wellness & Spa Agent:** Consulta tratamientos, profesionales y horarios disponibles, y coordina solicitudes de bienestar que requieren aprobación humana antes de confirmarse.
- **Local Guide Agent:** Consulta la red curada por el hotel de restaurantes, actividades y lugares turísticos recomendados, incluyendo descuentos disponibles, y prepara opciones para el huésped.
- **Robot Delivery Agent:** Coordina entregas e intercambios simulados sujetos a disponibilidad del robot y validaciones de seguridad.
- **Guest Folio Agent:** Consulta el saldo y los movimientos del folio y distingue cargos confirmados de pendientes.
- **Human Handoff Agent:** Transfiere solicitudes que requieren asistencia de recepción y comunica con claridad si el traspaso se completó.

Estos agentes y capacidades comparten únicamente el contexto necesario y son coordinados por el Concierge Agent; los pagos requieren aprobación explícita del huésped. Los módulos MCP proporcionan herramientas deterministas y no representan agentes autónomos. Este README documenta responsabilidades previstas, no lógica funcional.
