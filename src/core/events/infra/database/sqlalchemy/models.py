import uuid

from sqlalchemy import String, TypeDecorator
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# class GUID(TypeDecorator):
#     """Platform-independent GUID type.

#     Uses PostgreSQL's UUID type, otherwise uses
#     String(36), storing as stringified hex representation.
#     """

#     impl = String

#     def process_bind_param(self, value, dialect):
#         if value is None:
#             return value
#         elif dialect.name == 'postgresql':
#             return str(value)
#         else:
#             if not isinstance(value, uuid.UUID):
#                 return '%.32x' % uuid.UUID(value).int
#             else:
#                 # hexstring
#                 return '%.32x' % value.int

#     def process_result_value(self, value, dialect):
#         if value is None:
#             return value
#         else:
#             return uuid.UUID(value)


class PartnerModel(Base):
    __tablename__ = 'partner'

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f'Partner(id={self.id!r}, name={self.name!r})'
