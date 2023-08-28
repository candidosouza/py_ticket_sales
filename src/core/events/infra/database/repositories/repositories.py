from dataclasses import dataclass, field
from typing import List

from sqlalchemy.orm import Session

from src.core.common.domain.repositories import ET
from src.core.common.domain.value_objects import IdUUID
from src.core.events.domain.entities.partner import Partner
from src.core.events.domain.entities.customer import Customer
from src.core.events.domain.repositories.repositories_interface import (
    IPartinerRepository,
    ICustomerRepository
)
from src.core.events.infra.database.sqlalchemy.config import SQLAlchemyConfig
from src.core.events.infra.database.sqlalchemy.mappers import (
    PartnerMapper,
    CustomerMapper
)
from src.core.events.infra.database.sqlalchemy.models import (
    PartnerModel,
    CustomerModel
)


@dataclass(slots=True, kw_only=True)
class PartinerSqlAlchemyRepository(IPartinerRepository):

    session: Session = field(default_factory=SQLAlchemyConfig.get_session)

    def add(self, partiner: Partner) -> None:
        orm_partner = PartnerMapper.to_model(partiner)
        self.session.add(orm_partner)
        self.session.commit()
        return PartnerMapper.to_entity(orm_partner)

    def find_by_id(self, entity_id: str | IdUUID) -> ET:
        partner = (
            self.session.query(PartnerModel).filter_by(id=entity_id).first()
        )
        return PartnerMapper.to_entity(partner) if partner else None

    def find_all(self) -> List[ET]:
        partners = self.session.query(PartnerModel).all()
        return [PartnerMapper.to_entity(partner) for partner in partners]

    def delete(self, entity_id: str | IdUUID) -> None:
        partner = (
            self.session.query(PartnerModel).filter_by(id=entity_id).first()
        )
        self.session.delete(partner)
        self.session.commit()


@dataclass(slots=True, kw_only=True)
class CustomerSqlAlchemyRepository(ICustomerRepository):
   
        session: Session = field(default_factory=SQLAlchemyConfig.get_session)

        def add(self, customer: Customer) -> None:
            orm_customer = CustomerMapper.to_model(customer)
            self.session.add(orm_customer)
            self.session.commit()
            return CustomerMapper.to_entity(orm_customer)

        def find_by_id(self, entity_id: str | IdUUID) -> ET:
            customer = (
                self.session.query(CustomerModel).filter_by(id=entity_id).first()
            )
            return CustomerMapper.to_entity(customer) if customer else None

        def find_all(self) -> List[ET]:
            customers = self.session.query(CustomerModel).all()
            return [CustomerMapper.to_entity(customer) for customer in customers]

        def delete(self, entity_id: str | IdUUID) -> None:
            customer = (
                self.session.query(CustomerModel).filter_by(id=entity_id).first()
            )
            self.session.delete(customer)
            self.session.commit()
