# Reserva y rastreo de vuelos

El Concierge Agent atiende las llamadas y mantiene la conversación con el huésped. El Flights Agent recibe solicitudes internas con los datos mínimos y el permiso de la operación, usa el adaptador de vuelos y devuelve resultados estructurados al concierge. Se propone LangGraph para coordinar la delegación y la confirmación de reservas.

## Reservar un vuelo nuevo

1. El concierge recoge origen, destino, fechas y preferencias pertinentes. El Flights Agent busca y compara ofertas. Si hay conflictos de horario o presupuesto, devuelve alternativas.
2. El concierge presenta el itinerario y el precio total con moneda. El huésped confirma explícitamente esa oferta. Si el precio o el itinerario cambian, el concierge solicita una nueva confirmación.
3. El Flights Agent verifica la autorización para la estancia y la oferta confirmada, y solicita la reserva con una clave de idempotencia. Devuelve el estado verificable del proveedor y el modo de ejecución. La emisión de un boleto se comunica únicamente cuando el proveedor la confirme en modo real.

## Rastrear un vuelo agendado

1. Para un vuelo reservado por el hotel, el concierge recupera los datos del itinerario autorizado para la estancia. Para un vuelo compartido por el huésped, solicita el número de vuelo y la fecha de salida. Si hay ambigüedad, confirma el tramo con el huésped.
2. El Flights Agent consulta el estado operativo del vuelo y devuelve la fuente, la hora de consulta y los retrasos, cambios de horario o cancelaciones que el proveedor confirme. El concierge informa si el estado está indisponible o desactualizado.

La búsqueda y el rastreo usan permisos de lectura. La creación de una reserva requiere un permiso de escritura y confirmación explícita. Los datos externos se validan contra el esquema de respuesta y se tratan como datos, incluso cuando contienen texto que parece una instrucción.

La Fase 0 conserva el modo simulado y carece de conexión a un proveedor. La selección y el acceso a las API para la implementación quedan pendientes. [Integración de vuelos](../integrations/flights.md).
