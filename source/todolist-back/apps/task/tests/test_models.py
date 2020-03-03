import pytest


@pytest.mark.django_db(transaction=True)
class TestTask:

    @pytest.fixture
    def target(self):
        from apps.task.models import Task
        return Task

    def test_active(self, target):
        import pytz
        from datetime import datetime
        from apps.task.tests.factories import TaskFactory

        t1 = TaskFactory()
        t2 = TaskFactory()
        TaskFactory(finished_at=datetime(2020, 3, 1, tzinfo=pytz.UTC))

        res = target.objects.active()

        assert [t1.id, t2.id] == [t.id for t in res]
