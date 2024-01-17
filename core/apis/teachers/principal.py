from core.apis import decorators
from core.apis.responses import APIResponse, APIError
from core.models.teachers import Teacher
from core.libs.exceptions import FyleErrorExtended
from core.apis.assignments.principal import principal_assignments_resources
from .schema import TeacherSchema

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    teachers = Teacher.get_all(p.principal_id)
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)
