import graphene
import logging

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField


from .nodes import GradeLevelNode, SchoolNode, SkillNode

logger = logging.getLogger(__name__)


class Query(graphene.ObjectType):
    all_schools = DjangoFilterConnectionField(SchoolNode)
    school_by_pk = relay.node.Field(SchoolNode, pk=graphene.Int(required=True))

    grade_level = relay.Node.Field(GradeLevelNode)
    all_grade_levels = DjangoFilterConnectionField(GradeLevelNode)

    skill = relay.Node.Field(SkillNode)
    all_skills = DjangoFilterConnectionField(SkillNode)
