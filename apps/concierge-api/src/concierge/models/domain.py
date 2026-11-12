"""Initial typed contracts for hotel operations and future adapters."""

from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class Status(StrEnum):
    ACTIVE = "active"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"
    UNAVAILABLE = "unavailable"


class Guest(Contract):
    id: UUID
    display_name: str
    authorized_preferences: dict[str, Any] = Field(default_factory=dict)


class Room(Contract):
    id: str
    number: str


class Stay(Contract):
    id: UUID
    guest_id: UUID
    room_id: str
    starts_at: datetime
    ends_at: datetime
    status: Status


class HotelService(Contract):
    id: str
    name: str
    description: str
    hours: dict[str, str]
    after_hours_available: bool = False


class ServiceAvailability(Contract):
    service_id: str
    available: bool
    reason: str | None = None
    checked_at: datetime


class GuestRequest(Contract):
    id: UUID
    stay_id: UUID
    channel: str
    request_type: str
    requested_at: datetime
    status: Status = Status.PENDING


class ServiceOrder(Contract):
    id: UUID
    stay_id: UUID
    items: list[dict[str, Any]]
    requested_for: datetime | None = None
    status: Status = Status.PENDING


class Delivery(Contract):
    id: UUID
    order_id: UUID
    robot_id: str | None = None
    status: Status = Status.PENDING
    events: list[dict[str, Any]] = Field(default_factory=list)


class Robot(Contract):
    id: str
    kind: str
    capabilities: list[str]
    status: Status
    max_load_kg: Decimal
    compartments: int = Field(ge=0)
    location_simulated: str
    battery_percent: int = Field(ge=0, le=100)


class InventoryItem(Contract):
    id: str
    name: str
    quantity_available: int = Field(ge=0)
    exchange_required: bool = False


class FlightOffer(Contract):
    id: str
    source: str
    simulated: bool = True
    origin: str = "LAX"
    destination: str
    departure_at: datetime
    arrival_at: datetime
    price: Decimal = Field(ge=0)
    currency: str = "USD"


class FlightReservation(Contract):
    id: UUID
    offer_id: str
    status: Status = Status.PENDING
    simulated: bool = True


class PaymentMethod(Contract):
    id: str
    brand: str
    last_four: str = Field(pattern=r"^\d{4}$")
    token_reference: str


class PaymentTransaction(Contract):
    id: UUID
    stay_id: UUID
    amount: Decimal = Field(gt=0)
    currency: str = "USD"
    status: Status = Status.PENDING
    simulated: bool = True
    payment_method_id: str


class Vehicle(Contract):
    id: str
    make: str
    model: str
    category: str
    capacity: int = Field(gt=0)
    rate: Decimal = Field(ge=0)
    status: Status


class Driver(Contract):
    id: str
    name: str
    languages: list[str]
    shift_starts_at: datetime
    shift_ends_at: datetime
    authorized_vehicle_ids: list[str]


class TransportReservation(Contract):
    id: UUID
    stay_id: UUID
    vehicle_id: str
    driver_id: str
    pickup_at: datetime
    dropoff_at: datetime
    price: Decimal = Field(ge=0)
    status: Status = Status.PENDING


class SecurityServiceRequest(Contract):
    id: UUID
    booking_reference: str
    service_window_start: datetime
    service_window_end: datetime
    pickup_area: str
    passenger_count: int = Field(ge=1)


class SecurityServiceQuote(Contract):
    id: UUID
    booking_reference: str
    amount: Decimal = Field(ge=0)
    currency: str = "USD"
    available: bool
    expires_at: datetime


class FolioEntry(Contract):
    id: UUID
    category: str
    description: str
    amount: Decimal
    status: str
    posted_at: datetime


class GuestFolio(Contract):
    id: UUID
    stay_id: UUID
    currency: str = "USD"
    entries: list[FolioEntry]
    balance: Decimal
    last_delivery_status: str | None = None


class NotificationPreference(Contract):
    guest_id: UUID
    channel: str
    consented: bool = False
    daily_folio_enabled: bool = False
    send_local_time: str = "20:00"


class NotificationDelivery(Contract):
    id: UUID
    channel: str
    purpose: str
    status: Status
    attempted_at: datetime | None = None


class HumanEscalation(Contract):
    id: UUID
    stay_id: UUID
    reason: str
    status: Status = Status.PENDING
    created_at: datetime


class ToolError(Contract):
    code: str
    message: str
    retryable: bool = False
