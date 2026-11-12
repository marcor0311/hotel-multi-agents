# Architectural Decision Records

## ADR-001: Monolito modular y límites lógicos MCP

**Estado:** Aceptado para Fase 0. Un solo backend y módulos/servidores MCP organizados por dominio; separación de despliegue solo si una necesidad operativa o de confianza la justifica.

## ADR-002: A2A solo para proveedor autónomo independiente

**Estado:** Aceptado; versión/SDK pendiente. No usar A2A para envolver APIs simples. Seleccionar especificación publicada, autenticación y verificación antes de implementar.

## ADR-003: Fixtures y efectos simulados por defecto

**Estado:** Aceptado. Proveedores externos y pagos quedan desconectados, fixtures llevan identificadores ficticios y las reservas/pagos se etiquetan como simulados.

## ADR-004: Contexto de huésped mínimo y autorización por acción

**Estado:** Aceptado conceptualmente. Método de autenticación por canal y persistencia/retención quedan pendientes de diseño detallado.

## Decisiones abiertas

- SDK/protocolo A2A y autenticación de proveedor.
- Backend de persistencia/checkpoint, migraciones y retención.
- Autenticación de huéspedes por teléfono/WhatsApp.
- Proveedores de vuelos, transporte, telefonía y correo.
- Políticas oficiales, horario after-hours y SLA de recepción.
- Modelo/tracing/evaluación y límites presupuestarios.
