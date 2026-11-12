"""Minimal, privacy-conscious future graph state contract."""

from typing import TypedDict


class ConciergeState(TypedDict, total=False):
    conversation_id: str
    channel: str
    stay_id: str
    normalized_request: str
    tool_results: list[dict[str, str]]
    needs_confirmation: bool
    escalation_reason: str
    response: str
