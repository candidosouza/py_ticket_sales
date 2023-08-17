from src.core.events.domain.entities.partner import Partner

from .models import Partner as PartnerORM


class PartnerMapper:
    @staticmethod
    def to_domain_model(partner_orm: PartnerORM) -> Partner:
        return Partner(
            name=partner_orm.name,
        )

    @staticmethod
    def to_orm_model(partner: Partner) -> PartnerORM:
        return PartnerORM(
            id=partner.id,
            name=partner.name,
        )
