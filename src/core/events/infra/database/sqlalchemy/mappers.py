from src.core.common.domain.exceptions import (
    EntityValidationException,
    LoadEntityException,
)
from src.core.events.domain.entities.partner import Partner

from .models import PartnerModel


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
