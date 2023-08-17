from dataclasses import dataclass
from typing import Optional

from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpot(Entity):
    location: Optional[str] = None
    is_reserved: Optional[bool] = False
    is_published: Optional[bool] = False

    def change_location(self, location: str) -> None:
        self._set('location', location)

    def publish(self) -> None:
        self._set('is_published', True)

    def un_publish(self) -> None:
        self._set('is_published', False)
