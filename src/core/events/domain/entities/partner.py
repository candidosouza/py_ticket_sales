from dataclasses import dataclass

from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.events.domain.entities.event import Event


@dataclass(frozen=True, slots=True, kw_only=True)
class Partner(AggregateRoot):
    name: str

    def init_event(self, input: dict):
        input['partner_id'] = self.id
        return Event(**input)

    def change_name(self, name: str):
        self._set('name', name)
