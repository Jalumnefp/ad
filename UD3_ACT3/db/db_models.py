from typing import List, Optional
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship



class Base(DeclarativeBase):
    pass


class Clinic(Base):
    __tablename__ = "clinic"

    id: Mapped[int] = mapped_column(primary_key=True)
    addr: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))

    pets: Mapped[List["Pet"]] = relationship(
        back_populates="id_clin", 
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return F"Clinic(id={self.id!r}, addr={self.addr!r}, name={self.name!r})"
    

class Owner(Base):
    __tablename__ = "owner"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))

    pets: Mapped[List["Pet"]] = relationship(
        back_populates="id_ownr", 
        cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
            return F"Owner(id={self.id!r}, addr={self.email!r}, name={self.name!r})"


class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[int] = mapped_column(primary_key=True)
    breed: Mapped[str] = mapped_column(String(50))
    descr: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(50))
    id_clin: Mapped[int] = mapped_column(ForeignKey("clinic.id"))
    id_ownr: Mapped[int] = mapped_column(ForeignKey("owner.id"))

    clinic: Mapped["Clinic"] = relationship(
        back_populates="pets"
    )
    owner: Mapped["Owner"] = relationship(
        back_populates="pets"
    )

    def __repr__(self) -> str:
        return F"Pet(id={self.id!r}, addr={self.breed!r}, descr={self.descr!r}, name={self.name!r}, id_clin={self.id_clin!r}, id_ownr={self.id_ownr!r})"

