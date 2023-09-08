from anyio import Event
from src.core.common.domain.exceptions import (
    EntityValidationException,
    LoadEntityException,
)
from src.core.events.domain.entities.customer import Customer
from src.core.events.domain.entities.partner import Partner

from .models import CustomerModel, EventModel, PartnerModel


class PartnerMapper:
    @staticmethod
    def to_entity(partner_orm: PartnerModel) -> Partner:
        try:
            partner = Partner(
                id_uuid=partner_orm.id,
                name=partner_orm.name,
            )
            return {**partner.to_dict(), 'id': str(partner.id_uuid)}
        except EntityValidationException as exception:
            raise LoadEntityException() from exception

    @staticmethod
    def to_model(partner: Partner) -> PartnerModel:
        return PartnerModel(
            id=partner.id,
            name=partner.name,
        )


class CustomerMapper:
    @staticmethod
    def to_entity(customer_orm: CustomerModel) -> Customer:
        try:
            customer = Customer(
                id_uuid=customer_orm.id,
                cpf=customer_orm.cpf,
                name=customer_orm.name,
            )
            return {**customer.to_dict(), 'id': str(customer.id_uuid)}
        except EntityValidationException as exception:
            raise LoadEntityException() from exception

    @staticmethod
    def to_model(customer: Customer) -> CustomerModel:
        return CustomerModel(
            id=customer.id,
            cpf=customer.cpf,
            name=customer.name,
        )


class EventMapper:
    @staticmethod
    def to_entity(event_orm: EventModel) -> Event:
        try:
            return Event(
                id_uuid=event_orm.id,
                name=event_orm.name,
                description=event_orm.description,
                date=event_orm.date,
                is_published=event_orm.is_published,
                total_spot=event_orm.total_spot,
                total_spot_reserved=event_orm.total_spot_reserved,
                partner_id=event_orm.partner_id,
            )
            # return {**event.to_dict(), 'id': str(event.id_uuid)}
        except EntityValidationException as exception:
            raise LoadEntityException() from exception
        
    @staticmethod
    def to_model(event: Event) -> EventModel:
        return EventModel(
            id=event.id,
            name=event.name,
            description=event.description,
            date=event.date,
            is_published=event.is_published,
            total_spot=event.total_spot,
            total_spot_reserved=event.total_spot_reserved,
            partner_id=event.partner_id,
        )