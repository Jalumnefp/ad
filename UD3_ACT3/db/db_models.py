from typing import List, Optional
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Clinic(Base):
    __tablename__ = "clinic"
    __fields__ = ['addr', 'name']

    id: Mapped[int] = mapped_column(primary_key=True)
    addr: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))

    pets: Mapped[List["Pet"]] = relationship(
        back_populates="clinic", 
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return F"Clinic(id={self.id!r}, addr={self.addr!r}, name={self.name!r})"
    

class Owner(Base):
    __tablename__ = "owner"
    __fields__ = ['email', 'name']

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))

    pets: Mapped[List["Pet"]] = relationship(
        back_populates="owner", 
        cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
            return F"Owner(id={self.id!r}, addr={self.email!r}, name={self.name!r})"


class Pet(Base):
    __tablename__ = "pet"
    __fields__ = ['breed', 'descr', 'name', 'clinic_id', 'owner_id']

    id: Mapped[int] = mapped_column(primary_key=True)
    breed: Mapped[str] = mapped_column(String(50))
    descr: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))
    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinic.id"))
    owner_id: Mapped[int] = mapped_column(ForeignKey("owner.id"))

    clinic: Mapped["Clinic"] = relationship(
        back_populates="pets"
    )
    owner: Mapped["Owner"] = relationship(
        back_populates="pets"
    )

    def __repr__(self) -> str:
        return F"Pet(id={self.id!r}, addr={self.breed!r}, descr={self.descr!r}, name={self.name!r}, id_clin={self.clinic_id!r}, id_ownr={self.owner_id!r})"

