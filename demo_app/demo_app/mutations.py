import graphene
import logging

from graphene import relay
from graphql_relay import from_global_id
from schooldata.models import GradeLevel, School, Skill
from .nodes import GradeLevelNode, SchoolNode, SkillNode


logger = logging.getLogger(__name__)


# region Skill

class CreateSkill(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        difficulty = graphene.Float(required=True)
        grade_level_id = graphene.ID(required=True)

    skill = graphene.Field(SkillNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        # XXX Note that any exceptions that arise here will be very, very well hidden.
        # The GraphQL service will happily return a 200 with no error payload and a null schedule ID.
        skill = Skill(
            name = input.get('name'),
            difficulty = input.get('difficulty'),
            grade_level=GradeLevel.objects.get(id=from_global_id(input.get('grade_level_id')).id)
        )
        skill.save()
        return CreateSkill(skill=skill)

class UpdateSkill(relay.ClientIDMutation):
    class Input:
        skill_id = graphene.ID(required=True)
        name = graphene.String()
        difficulty = graphene.Float()
        grade_level_id = graphene.ID()

    skill = graphene.Field(SkillNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        skill = Skill.objects.get(id=from_global_id(input.get('skill_id')).id)

        modified = False

        if 'name' in input:
            skill.name = input.get('name')
            modified = True

        if 'grade_level_id' in input:
            skill.grade_level = GradeLevel.objects.get(id=from_global_id(input.get('grade_level_id')).id)
            modified = True

        if 'difficulty' in input:
            skill.difficulty = input.get('difficulty')
            modified = True

        if modified:
            skill.save()

        return UpdateSkill(skill=skill)

class DeleteSkill(relay.ClientIDMutation):
    class Input:
        skill_id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        skill = Skill.objects.get(id=from_global_id(input.get('skill_id')).id)
        skill.delete()
        return DeleteSkill(skill=skill)

# endregion

# region GradeLevel

class CreateGradeLevel(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        grade_level = graphene.Int(required=True)

    grade_level = graphene.Field(GradeLevelNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        grade_level = GradeLevel(
            name = input.get('name'),
            grade_level = input.get('grade_level')
        )
        grade_level.save()
        return CreateGradeLevel(grade_level=grade_level)

class UpdateGradeLevel(relay.ClientIDMutation):
    class Input:
        grade_level_id = graphene.ID(required=True)
        name = graphene.String()
        grade_level = graphene.Int()

    grade_level = graphene.Field(GradeLevelNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        grade_level = GradeLevel.objects.get(id=from_global_id(input.get('grade_level_id')).id)

        modified = False

        if 'grade_level' in input:
            grade_level.grade_level = input.get('grade_level')
            modified = True

        if 'name' in input:
            grade_level.name = input.get('name')
            modified = True

        if modified:
            grade_level.save()

        return UpdateGradeLevel(grade_level=grade_level)

class DeleteGradeLevel(relay.ClientIDMutation):
    class Input:
        grade_level_id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        grade_level = GradeLevel.objects.get(id=from_global_id(input.get('grade_level_id')).id)
        grade_level.delete()
        return DeleteGradeLevel(grade_level=grade_level)

# endregion

# region School

class CreateSchool(relay.ClientIDMutation):
    class Input:
        name = graphene.String()
        is_using_scheduling = graphene.Boolean()

    school = graphene.Field(SchoolNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        school = School(
            name = input.get('name'),
            is_using_scheduling = input.get('is_using_scheduling')
        )

        school.save()
        return CreateSchool(school=school)

class UpdateSchool(relay.ClientIDMutation):
    class Input:
        school_id = graphene.ID(required=True)
        name = graphene.String()
        is_using_scheduling = graphene.Boolean()

    school = graphene.Field(SchoolNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        school = School.objects.get(id=from_global_id(input.get('school_id')).id)

        modified = False

        if 'name' in input:
            school.name = input.get('name')
            modified = True

        if 'is_using_scheduling' in input:
            school.is_using_scheduling = input.get('is_using_scheduling')
            modified = True

        if modified:
            school.save()

        return UpdateSchool(school=school)

class DeleteSchool(relay.ClientIDMutation):
    class Input:
        school_id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        school = School.objects.get(id=from_global_id(input.get('school_id')).id)
        school.delete()
        return DeleteSchool(school=school)

# endregion


class Mutation(graphene.ObjectType):

    create_skill = CreateSkill.Field()
    update_skill = UpdateSkill.Field()
    delete_skill = DeleteSkill.Field()

    create_grade_level = CreateGradeLevel.Field()
    update_grade_level = UpdateGradeLevel.Field()
    delete_grade_level = DeleteGradeLevel.Field()

    create_school = CreateSchool.Field()
    update_school = UpdateSchool.Field()
    delete_school = DeleteSchool.Field()
