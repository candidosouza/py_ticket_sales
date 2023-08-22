from abc import ABC
import abc
from dataclasses import dataclass, field
from typing import Generic, List, TypeVar
from src.core.common.domain.aggregate_root import AggregateRoot
from src.core.common.domain.value_objects import IdUUID
from src.core.common.domain.exceptions import NotFoundException


ET = TypeVar('ET', bound=AggregateRoot)


class RepositoryInterface(Generic[ET], ABC):

    @abc.abstractmethod
    def add(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, entity_id: str | IdUUID) -> ET:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[ET]:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, entity_id: str | IdUUID) -> None:
        raise NotImplementedError()



# repository in memory
@dataclass(slots=True)
class InMemoryRepository(RepositoryInterface[ET], ABC):

    items: List[ET] = field(default_factory=lambda: [])

    def add(self, entity: ET) -> None:
        self.items.append(entity)

    def find_by_id(self, entity_id: str | IdUUID) -> ET:
        id_str = str(entity_id)
        return self._get(id_str)

    def find_all(self) -> List[ET]:
        return self.items

    def delete(self, entity_id: str | IdUUID) -> None:
        id_str = str(entity_id)
        entity_found = self._get(id_str)
        self.items.remove(entity_found)

    def _get(self, entity_id: str) -> ET:
        entity = next(filter(lambda i: i.id == entity_id, self.items), None)
        if not entity:
            raise NotFoundException(f"Entity not found using ID '{entity_id}'")
        return entity
