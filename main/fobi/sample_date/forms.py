from django import forms
from fobi.base import BasePluginForm
from fobi.contrib.plugins.form_elements.content.content_image.defaults import IMAGES_UPLOAD_DIR
from fobi.helpers import handle_uploaded_file


class SampleDataForm(forms.Form, BasePluginForm):
    """Sample data form."""

    plugin_data_fields = [
        ("Nom", ""),
        ("NomBDD", ""),
        ("required", False)
    ]

    name = forms.CharField(label="Nom", required=True)
    label = forms.CharField(label="NomBDD", required=True)
    required = forms.BooleanField(label="Required", required=False)


def save_plugin_data(self, request=None):
    """Saving the plugin data and moving the file."""
    file_path = self.cleaned_data.get('file', None)
    if file_path:
        saved_image = handle_uploaded_file(IMAGES_UPLOAD_DIR, file_path)
        self.cleaned_data['file'] = saved_image


