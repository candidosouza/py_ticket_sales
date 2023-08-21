from src.core.common.domain.exceptions import EntityValidationException, LoadEntityException
from src.core.events.domain.entities.partner import Partner

from .models import Partner as PartnerORM


class PartnerMapper:
    @staticmethod
    def to_entity(partner_orm: PartnerORM) -> Partner:
        try:
            return Partner(
                id_uuid=partner_orm.id,
                name=partner_orm.name,
            )
        except EntityValidationException as exception:
            raise LoadEntityException() from exception

    @staticmethod
    def to_model(partner: Partner) -> PartnerORM:
        return PartnerORM(
            id=partner.id,
            name=partner.name,
        )
