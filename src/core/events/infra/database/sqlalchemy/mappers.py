from src.core.common.domain.exceptions import (
    EntityValidationException,
    LoadEntityException,
)
from src.core.events.domain.entities.partner import Partner
from src.core.events.domain.entities.customer import Customer

from .models import (
    PartnerModel, 
    CustomerModel
)


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

