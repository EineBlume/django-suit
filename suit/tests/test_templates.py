import os
from unittest import TestCase

from django.template import Engine


class FieldsetTemplateTestCase(TestCase):
    def test_fieldset_template_compiles(self):
        templates_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'templates',
        )
        engine = Engine(
            dirs=[templates_dir],
            libraries={
                'suit_forms': 'suit.templatetags.suit_forms',
            },
        )

        engine.get_template('admin/includes/fieldset.html')
