import graphene

from graphene import relay
from graphene_django import DjangoObjectType

from schooldata.models import GradeLevel, Skill, School


class PKDjangoObjectType(DjangoObjectType):
    '''
    Nodes of this type will automatically have the Django primary key value
    exposed in their GraphQL schema type. Note that this does not enable querying
    or filtering by PK value; that's significantly more challenging to implement.
    '''
    pk = graphene.Int(source='pk')

    class Meta:
        abstract = True


class SchoolNode(PKDjangoObjectType):
    class Meta:
        model = School
        filter_fields = ['name']
        interfaces = [relay.Node]


class GradeLevelNode(PKDjangoObjectType):
    class Meta:
        model = GradeLevel
        filter_fields = ('name', 'grade_level')
        interfaces = [relay.Node]


class SkillNode(PKDjangoObjectType):
    class Meta:
        model = Skill
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'grade_level__name': ['istartswith'],
        }
        interfaces = [relay.Node]
