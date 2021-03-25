from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection, BadHeaderError
from django.conf import settings

from .forms import ContactForm
from .models import EmailRecord


class ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = EmailRecord  # data from database
    template_name = 'mainpage/index.html'
    context_object_name = 'list_projects'  # name of the var in html template
    queryset = EmailRecord.objects.all().order_by("-send_date")  # list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/'  # After submiting the form keep staying on the same url
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            cd['name'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['vlad.moroshan@gmail.com'],
            fail_silently=False
        )
        return super(ProjectListAndFormView, self).form_valid(form)

    @ensure_csrf_cookie
    def send_email(request):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        name = request.POST.get('name', '')
        if subject and message and from_email:
            try:
                #send_mail(subject, message, from_email, ['shaifulislamopu@gmail.com'])
                p = EmailRecord(name=name, email=from_email, message=message, subject=subject)
                p.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return JsonResponse(data={}, status=200)
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
