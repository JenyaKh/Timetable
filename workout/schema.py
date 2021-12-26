import datetime

import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from workout.models import Training, Timetable


class TrainingType(DjangoObjectType):
    class Meta:
        model = Training


class TimetableType(DjangoObjectType):
    class Meta:
        model = Timetable


class Query(ObjectType):
    training = graphene.Field(TrainingType, id=graphene.Int())
    timetable = graphene.List(TimetableType, date1=graphene.String(), date2=graphene.String())

    def resolve_training(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Training.objects.get(pk=id)
        return None

    def resolve_timetable(self, info, **kwargs):
        date1 = kwargs.get('date1')
        date2 = kwargs.get('date2')
        if date1:
            date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
        if date2:
            date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
        if date1 is None:
            date1 = datetime.datetime.now()
        if date2 is None:
            date2 = datetime.datetime.now()

        return Timetable.objects.filter(date__range=[date1, date2])


schema = graphene.Schema(query=Query)
