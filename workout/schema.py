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
    timetable = graphene.List(TimetableType, from_time=graphene.String(), to_time=graphene.String())

    def resolve_training(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Training.objects.get(pk=id)
        return None

    def resolve_timetable(self, info, **kwargs):
        from_time = kwargs.get('from_time')
        to_time = kwargs.get('to_time')
        if from_time:
            from_time = datetime.datetime.strptime(from_time, "%d/%m/%Y %H:%M")
        else:
            from_time = datetime.datetime.now()
        if to_time:
            to_time = datetime.datetime.strptime(to_time, "%d/%m/%Y %H:%M")
        else:
            to_time = datetime.datetime.now()

        return Timetable.objects.filter(date__range=[from_time, to_time])


schema = graphene.Schema(query=Query)
