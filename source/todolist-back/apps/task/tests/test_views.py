import pytest
from django.urls import reverse

from rest_framework.test import APIClient


@pytest.mark.django_db(transaction=True)
class TestTaskListView:

    def test_it(self):
        from datetime import datetime
        import pytz
        from apps.task.tests.factories import TaskFactory

        t1 = TaskFactory(content='taskA')
        t2 = TaskFactory(content='taskB')
        TaskFactory(content='taskC', finished_at=datetime(2020, 3, 1, tzinfo=pytz.UTC))

        client = APIClient()
        res = client.get(reverse('task:list'))

        assert res.status_code == 200
        assert len(res.data) == 2
        # 未完了のタスクだけが返ってくる
        assert res.data == [
            {
                'id': t1.id,
                'content': 'taskA',
            },
            {
                'id': t2.id,
                'content': 'taskB',
            }
        ]
