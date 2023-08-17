import uuid

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.events.infra.database.sqlalchemy.models import Base, Partner


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


class TestPartnerMondelIntegr:
    @pytest.mark.usefixtures('session')
    def test_should_create_partner(self, session):
        partner = Partner(id=str(uuid.uuid4()), name='Partner 1')
        session.add(partner)
        session.commit()

        retrieved_partner = (
            session.query(Partner).filter_by(name='Partner 1').first()
        )
        assert retrieved_partner.name == 'Partner 1'
