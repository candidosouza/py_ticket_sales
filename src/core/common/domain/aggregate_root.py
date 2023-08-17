from abc import ABC
from dataclasses import dataclass, field
from typing import List

from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True)
class AggregateRoot(Entity, ABC):
    events: List = field(default_factory=list)

    def add_event(self, event) -> None:
        self.events.append(event)

    def clear_events(self) -> None:
        self.events.clear()
