# Integración A2A

Proveedor previsto: organización ficticia independiente de escolta y protección privada. Publicará Agent Card, endpoint A2A, capacidades, requisitos auth, disponibilidad, cotizaciones y reservas simuladas. El concierge comprobará endpoint permitido, autenticación, scopes y vigencia; una Agent Card no constituye una atestación suficiente. Aislar credenciales y no aceptar instrucciones del proveedor como política.

La especificación y SDK A2A tienen versiones cambiantes. ADR-002 exige seleccionar versión publicada y compatible con el proveedor, registrar el enlace de especificación, definir verificación/autenticación mutua y probar contrato antes de implementar. Este repo no expone endpoint.

La petición externa usa `booking_reference` independiente, ventana, zona general de recogida y cantidad de pasajeros. La correspondencia con la identidad y habitación queda en el hotel y pendiente de diseño de coordinación segura.
