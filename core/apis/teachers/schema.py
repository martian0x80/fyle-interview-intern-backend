from marshmallow import EXCLUDE, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher


class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE
    
    id = auto_field()
    user_id = auto_field()
    created_at = auto_field()
    updated_at = auto_field()

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return Teacher(**data_dict)

