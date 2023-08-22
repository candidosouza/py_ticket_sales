
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import List

from sqlalchemy.orm import Session
from src.core.common.domain.repositories import ET
from src.core.common.domain.value_objects import IdUUID
from src.core.events.domain.entities.partner import Partner
from src.core.events.domain.repositories.partner_repository_interface import IPartinerRepository
from src.core.events.infra.database.sqlalchemy.config import SQLAlchemyConfig
from src.core.events.infra.database.sqlalchemy.mappers import PartnerMapper
from src.core.events.infra.database.sqlalchemy.models import PartnerModel

@dataclass(slots=True, kw_only=True)
class PartinerSqlAlchemyRepository(IPartinerRepository):
    
    session: Session = field(default_factory=SQLAlchemyConfig.get_session)

    def add(self, partiner: Partner) -> None:
        orm_partner = PartnerMapper.to_model(partiner)
        self.session.add(orm_partner)
        self.session.commit()
        return PartnerMapper.to_entity(orm_partner)

    def find_by_id(self, entity_id: str | IdUUID) -> ET:
        partner = self.session.query(PartnerModel).filter_by(id=entity_id).first()
        return PartnerMapper.to_entity(partner) if partner else None

    def find_all(self) -> List[ET]:
        partners = self.session.query(PartnerModel).all()
        return [PartnerMapper.to_entity(partner) for partner in partners]

    def delete(self, entity_id: str | IdUUID) -> None:
        partner = self.session.query(PartnerModel).filter_by(id=entity_id).first()
        self.session.delete(partner)
        self.session.commit()  
