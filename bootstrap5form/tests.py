import os
from distutils.version import StrictVersion

import django
from django.test import TestCase
from django.template import Template, Context
from django import forms

from .templatetags import bootstrap5

TEST_DIR = os.path.abspath(os.path.join(__file__, '..'))


CHOICES = (
    (0, 'Zero'), 
    (1, 'One'), 
    (2, 'Two'),
)

try:
    # required by Django 1.7 and later
    django.setup()
except:
    pass

class ExampleForm(forms.Form):
    char_field = forms.CharField(required=False)
    choice_field = forms.ChoiceField(choices=CHOICES, required=False)
    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    multiple_choice = forms.MultipleChoiceField(choices=CHOICES, required=False)
    multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    file_fied = forms.FileField(required=False)
    password_field = forms.CharField(widget=forms.PasswordInput, required=False)
    textarea = forms.CharField(widget=forms.Textarea, required=False)
    boolean_field = forms.BooleanField(required=False)


class BootstrapTemplateTagTests(TestCase):
    maxDiff = None

    def test_basic_form(self):
        form = ExampleForm()

        html = Template("{% load bootstrap5 %}{{ form|bootstrap5 }}").render(Context({'form': form}))


        fixture = 'basic.html'

        tpl = os.path.join('fixtures', fixture)
        with open(os.path.join(TEST_DIR, tpl)) as f:
            content = f.read()

        self.assertHTMLEqual(html, content)

    def test_horizontal_form(self):
        form = ExampleForm()

        html = Template("{% load bootstrap5 %}{{ form|bootstrap5_horizontal }}").render(Context({'form': form}))

        fixture = 'horizontal.html'
        
        tpl = os.path.join('fixtures', fixture)
        with open(os.path.join(TEST_DIR, tpl)) as f:
            content = f.read()

        self.assertHTMLEqual(html, content)

    def test_bound_field(self):
        form = ExampleForm(data={'char_field': 'asdf'})

        self.assertTrue(form.is_bound)
        rendered_template = bootstrap.bootstrap(form['char_field'])
