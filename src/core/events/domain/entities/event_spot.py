from dataclasses import dataclass
from typing import Optional

from src.core.common.domain.entities import Entity


@dataclass(frozen=True, slots=True, kw_only=True)
class EventSpot(Entity):
    location: Optional[str] = None
    is_reserved: Optional[bool] = False
    is_published: Optional[bool] = False
