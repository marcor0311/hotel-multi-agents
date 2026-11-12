# Orquestación

LangGraph se propone para coordinar estado conversacional, ramas de confirmación y puntos de interrupción humana. La estructura `agents/` contiene el contrato de estado y el lugar previsto del grafo, pero no ejecuta un LLM en Fase 0. No se incorpora LangChain por separado hasta que exista una necesidad que LangGraph no cubra.

Los nodos de resolución de estancia, permiso, disponibilidad y cálculo son deterministas. El checkpointing requiere decisión sobre backend, cifrado y retención antes de producción. Nunca incluir secretos, PAN o CVV en estado, prompts o tracing.
