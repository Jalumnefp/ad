import peewee

class BaseModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase('db/database.db')

class Clinic(BaseModel):
    id = peewee.AutoField(primary_key=True)
    addr = peewee.TextField()
    name = peewee.TextField()

    class Meta:
        name = 'Clinic'
        fields_list: list = ['id', 'addr', 'name']

class Owner(BaseModel):
    id = peewee.AutoField(primary_key=True)
    email = peewee.TextField()
    name = peewee.TextField()

    class Meta:
        name = 'Owner'
        fields_list: list = ['id', 'email', 'name']

class Pet(BaseModel):
    id = peewee.AutoField(primary_key=True)
    id_clin = peewee.ForeignKeyField(Clinic)
    id_ownr = peewee.ForeignKeyField(Owner)
    breed = peewee.TextField()
    desc = peewee.TextField()
    name = peewee.TextField()

    class Meta:
        name = 'Pet'
        fields_list: list = ['id', 'id_clin', 'id_ownr', 'breed', 'desc', 'name']

