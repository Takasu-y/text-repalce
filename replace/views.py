from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import TextForm
# Create your views here.


class IndexView(FormView):
    form_class = TextForm
    template_name = "index.html"

    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]

        # ここで変換
        replaced_text = text.replace(search, replace)

        # テンプレートに渡す
        context = self.get_context_data(replaced_text=replaced_text, form=form)
        return self.render_to_response(context)