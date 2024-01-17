from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse, APIError
from core.models.assignments import Assignment, GradeEnum, AssignmentStateEnum
from core.libs.exceptions import FyleErrorExtended

from .schema import AssignmentSchema, AssignmentGradeSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)


@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    teachers_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)


@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""

    assignment = Assignment.get_by_id(incoming_payload['id'])
    
    # additions start here

    if assignment is None:
        return APIError.respond(FyleErrorExtended(status_code=404, error='FyleError', message='Assignment not found'))

    if assignment.teacher_id != p.teacher_id:
        return APIError.respond(FyleErrorExtended(status_code=400, error='FyleError', message='Assignment not submitted to this teacher'))

    gradeEnumList = [GradeEnum.A, GradeEnum.B, GradeEnum.C, GradeEnum.D]
    if assignment.grade not in gradeEnumList:
        return APIError.respond(FyleErrorExtended(status_code=400, error='ValidationError', message='Invalid grade'))

    if assignment.state != AssignmentStateEnum.SUBMITTED:
        return APIError.respond(FyleErrorExtended(status_code=400, error='FyleError', message='Assignment not gradable'))

    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    # additions end here

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
