from django.contrib.auth.models import User
from django.core.files import File
from django.db import models, transaction
import hashlib


class UploadManager(models.Manager):
    def get_with_file(self, file):
        matching_uploads = self.filter(md5sum=_md5(file))
        for matching_upload in matching_uploads:
            if matching_upload.is_same_file(file):
                return matching_upload
        return None


class Upload(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to='%Y/%m/%d')
    name = models.CharField(max_length=256)
    uuid = models.CharField(max_length=256)
    content_type = models.CharField(max_length=256, blank=True)
    md5sum = models.CharField(max_length=32)

    objects = UploadManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.md5sum = _md5(self.file)
        super(Upload, self).save(*args, **kwargs)

    @transaction.atomic
    def delete(self, *args, **kwargs):
        if Upload.objects.filter(file=self.file).count() == 1:
            self.file.delete()
        super(Upload, self).delete(*args, **kwargs)

    def is_same_file(self, file):
        return self._file_cmp(self.file, file)

    @staticmethod
    def _file_cmp(file1, file2):
        if file1.size != file2.size:
            return False
        chunk_size = File.DEFAULT_CHUNK_SIZE
        file1.seek(0)
        file2.seek(0)
        while True:
            chunk1 = file1.read(chunk_size)
            chunk2 = file2.read(chunk_size)
            if chunk1 != chunk2:
                return False
            if not chunk1 and not chunk2:
                break
        return True


def _md5(file):
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    return md5.hexdigest()
