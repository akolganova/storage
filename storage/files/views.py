from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from storage.files.forms import FileUploadForm
from storage.files.models import Upload
from django.core.servers.basehttp import FileWrapper
import uuid
from django.contrib import messages
from django.db import transaction

FILE_LIMIT = 100


@login_required
def index(request, template_name):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                _upload(request, request.FILES['file'])
            return HttpResponseRedirect(reverse('storage.files.views.index'))
    else:
        form = FileUploadForm()
    uploads = Upload.objects.filter(user=request.user)
    return TemplateResponse(request, template_name, {'form': form, 'uploads': uploads})


def _check_file_limit(request):
    if Upload.objects.filter(user=request.user).count() >= FILE_LIMIT:
        messages.add_message(request, messages.ERROR, 'You have reached the limit of %s files' % FILE_LIMIT)
        return True
    return False


def _upload(request, file):
    if _check_file_limit(request):
        return
    matching_upload = Upload.objects.get_with_file(file)
    if matching_upload:
        text = 'Duplicate (%s, "%s")' % (matching_upload.user, matching_upload.name)
        messages.add_message(request, messages.INFO, text)
    Upload.objects.create(
        user=request.user,
        file=matching_upload and matching_upload.file or file,
        name=file.name,
        content_type=file.content_type,
        uuid=uuid.uuid1(),
    )


def download(request, uuid):
    upload = get_object_or_404(Upload, uuid=uuid)
    response = HttpResponse(FileWrapper(upload.file), content_type=upload.content_type)
    response['Content-Disposition'] = 'attachment; filename=%s' % upload.name
    return response


@login_required
def delete(request, uuid):
    with transaction.atomic():
        upload = get_object_or_404(Upload, uuid=uuid, user=request.user)
        upload.delete()
    return HttpResponseRedirect(reverse('storage.files.views.index'))
