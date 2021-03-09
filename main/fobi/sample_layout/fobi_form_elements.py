from fobi.base import form_element_plugin_widget_registry
from main.fobi.sample_textarea.widgets import BaseSampleTextareaPluginWidget


class SampleTextareaPluginWidget(BaseSampleTextareaPluginWidget):
    """Sample textarea plugin widget."""

    theme_uid = 'bootstrap3'  # Theme for which the widget is loaded
    media_js = [
        'sample_layout/js/fobi.plugins.form_elements.sample_boolean.js',
    ]
    media_css = [
        'sample_layout/css/fobi.plugins.form_elements.sample_boolean.css',
    ]


form_element_plugin_widget_registry.register(SampleTextareaPluginWidget)
