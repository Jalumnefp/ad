from peewee import *

maria_db = MySQLDatabase('starwars', host='127.0.0.1', user='star', password='wars', port=3306)


class BaseModel(Model):
    class Meta:
        database = maria_db


class Affiliations(BaseModel):
    id = AutoField(primary_key=True)
    affiliation = TextField()

class Planets(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()
    rotation_period = IntegerField()
    orbital_period = IntegerField()
    diameter = IntegerField()
    climate = TextField()
    gravity = TextField()
    terrain = TextField()
    surface_water = TextField()
    population = IntegerField()
    created_date = DateField()
    updated_date = DateField()
    url = TextField()


class Films(BaseModel):
    id = AutoField(primary_key=True)
    episode = TextField()
    title = TextField()

class Characters(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()
    height = IntegerField()
    mass = FloatField()
    hair_color = TextField()
    skin_color = TextField()
    eye_color = TextField()
    birth_year = TextField()
    gender = TextField()
    planet_id = ForeignKeyField(Planets)
    created_date = DateField()
    updated_date = DateField()
    url = TextField()
    id_affiliation = ManyToManyField(Affiliations, backref='id_characters')
    id_film = ManyToManyField(Films, backref='id_characters')

class Deaths(BaseModel):
    id = AutoField(primary_key=True)
    id_character = ForeignKeyField(Characters)
    id_killer = ForeignKeyField(Characters)
    id_film = ForeignKeyField(Films)