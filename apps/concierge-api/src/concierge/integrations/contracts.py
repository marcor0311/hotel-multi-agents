"""Narrow ports for future integrations; no provider is connected in Phase 0."""

from typing import Protocol
from uuid import UUID

from concierge.models.domain import Delivery, FlightOffer, GuestFolio, Robot, ServiceOrder


class HotelTools(Protocol):
    def get_active_stay(self, conversation_id: str) -> UUID | None: ...


class RobotDeliveryTools(Protocol):
    def list_robots(self) -> list[Robot]: ...

    def get_robot_status(self, robot_id: str) -> Robot: ...

    def assign_delivery(self, order: ServiceOrder) -> Delivery: ...

    def get_delivery_status(self, delivery_id: UUID) -> Delivery: ...

    def verify_item_return(self, delivery_id: UUID, item_count: int) -> bool: ...

    def complete_delivery(self, delivery_id: UUID) -> Delivery: ...

    def cancel_delivery(self, delivery_id: UUID, reason: str) -> Delivery: ...


class FlightTools(Protocol):
    def search(self, origin: str, destination: str) -> list[FlightOffer]: ...


class FolioTools(Protocol):
    def get_folio(self, stay_id: UUID) -> GuestFolio: ...
