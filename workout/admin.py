from django.contrib import admin

from workout.models import Training, Timetable

admin.site.register([Training, Timetable])
