from core.apis import decorators
from flask import Blueprint
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    teachers = Teacher.get_all(p.principal_id)
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)
