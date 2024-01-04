from django.shortcuts import render
from django.views.generic import View

from app.models import About, Contact, Feedback, Header, Result, Service, WhyWe

# Create your views here.


class Index(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        header = Header.objects.first()
        why_we = WhyWe.objects.first()
        result = Result.objects.all()
        feedback = Feedback.objects.all()
        service = Service.objects.all()
        about = About.objects.all()
        contact = Contact.objects.first()

        about1 = about[0]
        about2 = about[1]
        about3 = about[2]

        context = {
            "header": header,
            "why_we": why_we,
            "results": result,
            "feedbacks": feedback,
            "services": service,
            "about1": about1,
            "about2": about2,
            "about3": about3,
            "contact": contact,
        }

        return render(request, self.template_name, context)
