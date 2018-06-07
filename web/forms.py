# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import bleach_clean, RequiredFieldForm

from .models import Main


class MainForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        for name in ("title", "description", "url"):
            self.fields[name].widget.attrs.update({"class": "pure-input-2-3"}),
        for name in ("title",):
            self.fields[name].widget.attrs.update({"rows": "1"})

    def clean_description(self):
        data = self.cleaned_data["description"]
        return bleach_clean(data)

    class Meta:
        model = Main
        fields = ("title", "description", "url", "picture")
        widgets = {"picture": forms.FileInput}
