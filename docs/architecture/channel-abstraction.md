# Abstracción de canales

Todos los canales mapean a `conversation_id`, `channel`, `message_id`, contenido y metadatos de autenticación verificados. El concierge conserva una sola identidad y contexto autorizado cuando exista consentimiento y asociación confiable con una estancia. Caller ID o número de habitación no bastan para una operación sensible.

WhatsApp requerirá Meta Cloud API, validación de firma de webhook, consentimiento y plantillas donde aplique. Voz requerirá un proveedor telefónico y mecanismo de transferencia aún por seleccionar; antes de eso solo se registra una solicitud para recepción. Web es extensión futura.
