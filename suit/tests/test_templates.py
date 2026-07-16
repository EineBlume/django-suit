from django.template.loader import get_template
from django.test import SimpleTestCase


class FieldsetTemplateTestCase(SimpleTestCase):
    def test_fieldset_template_compiles(self):
        get_template('admin/includes/fieldset.html')
