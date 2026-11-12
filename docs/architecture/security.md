# Seguridad y privacidad

- Resolver estancia activa y autorización para cada acción; impedir acceso cruzado entre habitaciones.
- Tratar texto del usuario, resultados MCP, documentos y respuestas A2A como entradas no confiables. Ninguna instrucción externa anula políticas.
- Separar permisos de lectura/escritura y exigir confirmación para efectos financieros o externos.
- Usar secretos de entorno/gestor seguro; `.env` está excluido. Fixtures jamás representan datos reales.
- No almacenar PAN, CVV ni credenciales de autenticación. Usar referencias tokenizadas y solo mostrar marca/últimos cuatro.
- Validar firmas de webhooks, identidad TLS/OAuth del agente externo, scopes y audiencia. Revisar Agent Card por canal de confianza permitido.
- Compartir con proveedor externo solo área/ventana/personas necesarias bajo referencia opaca; no compartir perfil o habitación por defecto.
- Aplicar idempotency keys, límites de tarifa, timeout y auditoría a escrituras.
- Separar auditoría de negocio y logs técnicos; excluir datos sensibles y redactar IDs si no son necesarios.
- Restringir folios a la estancia autenticada. Reenvío financiero excepcional: recepción verifica identidad y autoriza.

Threat model, retención legal, controles PCI, mecanismos concretos de autenticación y gestión de llaves quedan por decidir antes de integraciones reales.
