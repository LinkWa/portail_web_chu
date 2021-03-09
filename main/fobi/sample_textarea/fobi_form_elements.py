from django import forms
from django.conf import settings
from fobi.base import FormFieldPlugin, form_element_plugin_registry
from fobi.contrib.plugins.form_elements.fields.file.defaults import FILES_UPLOAD_DIR
from fobi.helpers import handle_uploaded_file

from main.fobi.sample_textarea.forms import SampleTextareaForm


class SampleTextareaPlugin(FormFieldPlugin):
    """Sample textarea plugin."""

    uid = "sample_textarea"
    name = "Sample Textarea"
    form = SampleTextareaForm
    group = "Samples"  # Group to which the plugin belongs to

    def get_form_field_instances(self,
                                 request=None,
                                 form_entry=None,
                                 form_element_entries=None,
                                 **kwargs):
        kwargs = {
            'required': self.data.required,
            'label': self.data.label,
            'initial': self.data.initial,
            'widget': forms.widgets.Textarea(attrs={})
        }

        return [(self.data.name, forms.CharField, kwargs), ]


form_element_plugin_registry.register(SampleTextareaPlugin)


def submit_plugin_form_data(self,
                            form_entry,
                            request,
                            form,
                            form_element_entries=None,
                            **kwargs):
    """Submit plugin form data."""
    # Get the file path
    file_path = form.cleaned_data.get(self.data.name, None)
    if file_path:
        # Handle the upload
        saved_file = handle_uploaded_file(FILES_UPLOAD_DIR, file_path)
        # Overwrite ``cleaned_data`` of the ``form`` with path to moved
        # file.
        form.cleaned_data[self.data.name] = "{0}{1}".format(
            settings.MEDIA_URL, saved_file
        )

    # It's critically important to return the ``form`` with updated
    # ``cleaned_data``
    return form
