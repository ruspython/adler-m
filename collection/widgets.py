from django.forms import widgets
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe


class PreviewImageWidget(widgets.ClearableFileInput):
    template_with_initial = u'%(clear_template)s<br>%(input_text)s: %(input)s'

    def render(self, name, value, attrs=None):
        output = super(PreviewImageWidget, self).render(name, value, attrs=None)
        if value and hasattr(value, 'url'):
            try:
                mini = get_thumbnail(value, 'x80', upscale=False)
            except Exception:
                pass
            else:
                output = u'<div class="image_preview_widget">' \
                         u'<img src="%s">' \
                         u'<div class="labels">%s</div>' \
                         u'</div>'\
                         % (mini.url, output)
        return mark_safe(output)