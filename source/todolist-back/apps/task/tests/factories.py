import factory


class TaskFactory(factory.django.DjangoModelFactory):

    content = 'タスクA'

    class Meta:
        model = 'task.Task'
