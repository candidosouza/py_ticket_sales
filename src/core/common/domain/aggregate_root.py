from abc import ABC

from src.core.common.domain.entities import Entity


class AggregateRoot(Entity, ABC):
    
    def add_event(self, event):
        self.events.append(event)

    def clear_events(self):
        self.events.clear()
