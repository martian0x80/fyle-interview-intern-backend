from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.teachers import Teacher
from core.libs.helpers import GeneralObject


class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        load_instance = True
        include_relationships = True
        unknown = EXCLUDE
    
    id = auto_field()
    user_id = auto_field()
    created_at = auto_field()
    updated_at = auto_field()

    @post_load
    def make_object(self, data, **kwargs):
        return Teacher(**data)

