# Intercambio de toallas

1. Validar estancia y solicitud.
2. Consultar política e inventario; confirmar que se requiere intercambio.
3. Asignar robot compatible disponible y crear entrega idempotente.
4. Al retorno, el controlador/sensor verifica conteo.
5. Solo con conteo correcto se libera lote limpio.
6. Registrar resultado mínimo y cerrar.

Falla, discrepancia, robot no disponible o timeout: no liberar limpio automáticamente; cancelar/retener y ofrecer recepción. No todos los suministros requieren devolución.
