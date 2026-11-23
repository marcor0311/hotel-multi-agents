# Contexto del sistema

El huésped autenticado conversa con el Concierge Agent a través del adaptador de canal. El concierge consulta el contexto autorizado de la estancia y coordina a los especialistas internos. Recepción está disponible 24/7 y conserva las verificaciones presenciales y las decisiones fuera de política. El proveedor externo de seguridad opera como una organización independiente. [Guía de arquitectura](overview.md)

```mermaid
flowchart TB
  Guest[Huésped en estancia activa]
  subgraph Hotel[Hotel ficticio de Los Ángeles]
    Channel[Adaptadores: voz / WhatsApp / web]
    Concierge[Concierge Agent]
    Context[Contexto autorizado de estancia]
    Specialists[Agentes especializados]
    Handoff[Human Handoff Agent]
    Tools[Herramientas hoteleras MCP]
    Staff[Recepción 24/7]
  end
  Provider[Proveedor de seguridad independiente]
  Guest <--> Channel <--> Concierge
  Concierge --> Context
  Concierge <--> Specialists
  Concierge --> Tools
  Specialists --> Tools
  Concierge --> Handoff --> Staff
  Concierge <-->|A2A, datos mínimos| Provider
```
