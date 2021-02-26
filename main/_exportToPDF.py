from django.contrib.auth.mixins import LoginRequiredMixin
from django_renderpdf.views import PDFView

from main import models
from portail_web_chu import settings


class Viewpdf(LoginRequiredMixin, PDFView):
    """Generate labels for some Shipments.

    A PDFView behaves pretty much like a TemplateView, so you can treat it as such.
    """
    template_name = 'main/recherche.html'
    base_url = 'file://' + settings.STATIC_ROOT
    download_filename = 'hello.pdf'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super(Viewpdf, self).get_context_data(pagesize = 'A4' , title = 'Bonjour!' , *args, **kwargs)

        context['models'] = models.objects.filter(
            # batch_id=kwargs['pk'],
        )

        return context