# Vuelos

LAX es el aeropuerto de referencia. El Flights Agent accederá a proveedores mediante un adaptador con operaciones tipadas para buscar ofertas, crear reservas y consultar el estado de un vuelo. Cada resultado identificará su fuente, su modo (real, sandbox o simulado) y la hora de consulta. Las ofertas incluirán precio total y moneda. El rastreo usará el número de vuelo y la fecha de salida, con el tramo cuando haga falta distinguir resultados.

El primer objetivo de integración es probar con una API real, en sandbox si el proveedor lo ofrece. La selección está pendiente. Duffel figura como candidato para búsqueda y reserva, sujeto a acceso y condiciones comerciales. Se evaluará por separado si el proveedor de reservas cubre el estado operativo de vuelos agendados fuera del hotel o si hace falta otro proveedor.

El adaptador reservará únicamente tras verificar el permiso de escritura y la confirmación de la oferta. La Fase 0 conserva fixtures y efectos simulados. Una reserva de prueba se identifica como tal y el estado de emisión se comunica solo con confirmación verificable en modo real. [Flujo de reserva y rastreo](../workflows/flight-booking.md).
