from tastypie.resources import ModelResource
from myproject.polls.models import Poll, Choice
from tastypie import fields

class PollResource(ModelResource):
    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'

class ChoiceResource(ModelResource):
    poll = fields.ForeignKey(PollResource, 'poll')
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
