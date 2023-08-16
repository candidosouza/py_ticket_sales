from dataclasses import dataclass, field
from typing import List, Optional

from src.core.common.domain.entities import Entity
from src.core.events.domain.entities.event_spot import EventSpot


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSection(Entity):
    name: str
    description: Optional[str] = None
    is_published: Optional[bool] = False
    total_spot: int
    total_spot_reserved: Optional[int] = 0
    price: float
    spot: Optional[List[EventSpot]] = field(default_factory=list)

    def __post_init__(self):
        self._init_spot()

    def _init_spot(self):
        for _ in range(self.total_spot):
            self.spot.append(EventSpot())
