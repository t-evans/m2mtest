from django.test import TestCase

from m2mtest.models import Foo, Bar


class BarTests(TestCase):
    def setUp(self):
        pass

    def test_stuff(self):
        foo = Foo.objects.create(name='test1')
        bar = Bar.objects.create()
        some_invalid_id = 4654686

        some_foo_ids = [foo.id, some_invalid_id]
        bar.some_m2m_field.set(some_foo_ids)

        print('\n\nIT SHOULD NOT GET HERE (and yet it does...).\n\n')
