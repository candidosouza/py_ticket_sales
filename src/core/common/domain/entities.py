from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import Any

from src.core.common.domain.value_objects import IdUUID


@dataclass(frozen=True, slots=True)
class Entity(ABC):
    id_uuid: IdUUID = field(default_factory=lambda: IdUUID()) 

    @property
    def id(self):
        return str(self.id_uuid)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('id_uuid')
        return {'id': str(self.id_uuid), **entity_dict}
