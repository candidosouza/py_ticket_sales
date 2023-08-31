import uuid

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class PartnerModel(Base):
    __tablename__ = 'partner'

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f'Partner(id={self.id!r}, name={self.name!r})'

    def __str__(self) -> str:
        return f'PartnerModel: {self.name}'


class CustomerModel(Base):
    __tablename__ = 'customer'

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    cpf: Mapped[str] = mapped_column(String(11), unique=True)
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f'Customer(id={self.id!r}, name={self.name!r})'

    def __str__(self):
        return f'CustomerModel: {self.name}'


class EventModel(Base):
    __tablename__ = 'event'

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    date: Mapped[str] = mapped_column(String(255))  # Consider using DateTime
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    total_spot: Mapped[int] = mapped_column(Integer, default=0)
    total_spot_reserved: Mapped[int] = mapped_column(Integer, default=0)

    partner_id: Mapped[uuid.UUID] = mapped_column(
        String(36), ForeignKey('partner.id')
    )

    sections: Mapped['EventSectionModel'] = relationship(backref='event')

    def __repr__(self) -> str:
        return f'Event(id={self.id!r}, name={self.name!r})'

    def __str__(self) -> str:
        return f'EventModel: {self.name}'


class EventSectionModel(Base):
    __tablename__ = 'event_section'

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    total_spot: Mapped[int] = mapped_column(Integer)
    total_spot_reserved: Mapped[int] = mapped_column(Integer, default=0)
    price: Mapped[float] = mapped_column(Float)

    event_id: Mapped[uuid.UUID] = mapped_column(
        String(36), ForeignKey('event.id')
    )

    spots: Mapped['EventSpotModel'] = relationship(backref='event_section')

    def __repr__(self) -> str:
        return f'EventSection(id={self.id!r}, name={self.name!r})'

    def __str__(self) -> str:
        return f'EventSectionModel: {self.name}'


class EventSpotModel(Base):
    __tablename__ = 'event_spot'

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    is_reserved: Mapped[bool] = mapped_column(Boolean, default=False)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)

    section_id: Mapped[uuid.UUID] = mapped_column(
        String(36), ForeignKey('event_section.id')
    )

    def __repr__(self) -> str:
        return f'EventSpot(id={self.id!r}, location={self.location!r})'

    def __str__(self) -> str:
        return f'EventSpotModel: {self.location}'
