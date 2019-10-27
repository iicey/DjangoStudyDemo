# -*- coding: utf-8 -*-

# Author: 桑葚ICE
# Email: 152516cc@gmail.com
# Blog: iicey.github.io
# JueJin: juejin.im/user/5c64dce8e51d45013c40742c
from django import forms

from .models import Student


class StudentForm(forms.Form):
    def clean_qq(self):
        cleaned_data = self.cleaned_data["qq"]
        if not cleaned_data.isdigit():
            raise forms.ValidationError("必须是数字")
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            "name", "sex", "profession",
            "email", "qq", "phone"
        )
