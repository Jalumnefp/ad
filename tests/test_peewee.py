from peewee import *
import sqlite3


sqlite_con = SqliteDatabase('database.sqlite3')


class BaseModel(Model):
    class Meta:
        database = sqlite_con


class Persona(BaseModel):
    id_p = AutoField()
    nom = TextField()
    cognoms = TextField()
    data_naix = DateField()


class Telefon(BaseModel):
    id_t = AutoField()
    persona_id = ForeignKeyField(Persona)
    numero = CharField()


sqlite_con.connect()
Persona(nom="Ronaldo",cognoms="Soccer",data_naix=2023-12-12).save()
Telefon(persona_id=1,numero="666666666").save()
Persona.delete().where(Persona.id_p > 4).execute()
Telefon.delete().where(Telefon.id_t > 3).execute()
Persona.update(id_p = 5).where(Persona.id_p == 4).execute()
sqlite_con.create_tables([Persona, Telefon])
sqlite_con.close()

sqlite_con = sqlite3.connect('database.sqlite3')
cursor = sqlite_con.cursor()
cursor.execute('SELECT * FROM Persona')
res = cursor.fetchall()
for row in res:
    print(row)
cursor.execute('SELECT * FROM Telefon')
res = cursor.fetchall()
for row in res:
    print(row)


