
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import List

from sqlalchemy.orm import Session
from src.core.common.domain.repositories import ET, RepositoryInterface
from src.core.common.domain.value_objects import IdUUID
from src.core.events.domain.entities.partner import Partner
from src.core.events.domain.repositories.partner_repository_interface import IPartinerRepository
from src.core.events.infra.database.sqlalchemy.config import SQLAlchemyConfig
from src.core.events.infra.database.sqlalchemy.mappers import PartnerMapper


@dataclass(slots=True, kw_only=True)
class PartinerSqlAlchemyRepository(IPartinerRepository):
    
    session: Session = field(default_factory=SQLAlchemyConfig.get_session)

    def add(self, partiner: Partner) -> None:
        orm_partner = PartnerMapper.to_model(partiner)
        self.session.add(orm_partner)
        self.session.commit()
        return PartnerMapper.to_entity(orm_partner)

    # def bulk_insert(self, entities: List[ET]) -> None:
    #     raise NotImplementedError()

    def find_by_id(self, entity_id: str | IdUUID) -> ET:
        raise NotImplementedError()

    def find_all(self) -> List[ET]:
        raise NotImplementedError()

    # def update(self, entity: ET) -> None:
    #     raise NotImplementedError()

    def delete(self, entity_id: str | IdUUID) -> None:
        raise NotImplementedError()
