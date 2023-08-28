import uuid

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.events.infra.database.sqlalchemy.models import Base, PartnerModel


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


class TestPartnerModelIntegr:
    @pytest.mark.usefixtures('session')
    def test_should_create_partner(self, session):
        partner = PartnerModel(id=str(uuid.uuid4()), name='Partner 1')
        session.add(partner)
        session.commit()

        retrieved_partner = (
            session.query(PartnerModel).filter_by(name='Partner 1').first()
        )
        assert retrieved_partner.name == 'Partner 1'
