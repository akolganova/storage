from django.test import TestCase, override_settings
import os
from django.core.files.uploadedfile import SimpleUploadedFile


class ViewsTests(TestCase):
    fixtures = ['test_users']

    def test_upload(self):
        self.client.login(username='john', password='1')
        file = _create_uploaded_file('macro.txt')

        response = self.client.post('/files/', {'file': file}, follow=True)

        self.assertRedirects(response, '/files/')
        self.assertContains(response, text='macro.txt')

    def test_delete(self):
        self.client.login(username='john', password='1')
        file = _create_uploaded_file('macro.txt')
        response = self.client.post('/files/', {'file': file}, follow=True)
        upload = response.context['uploads'].first()

        response = self.client.get('/files/delete/%s' % upload.uuid, follow=True)

        self.assertRedirects(response, '/files/')
        self.assertNotContains(response, text='macro.txt')

    def test_download(self):
        self.client.login(username='john', password='1')
        file = _create_uploaded_file()
        response = self.client.post('/files/', {'file': file}, follow=True)
        upload = response.context['uploads'].first()
        self.client.logout()

        response = self.client.get('/files/downloads/%s' % upload.uuid, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=macro.txt')

    def test_upload_duplicate(self):
        self.client.login(username='john', password='1')
        file = _create_uploaded_file('macro.txt')
        duplicate_file = _create_uploaded_file('test.bin')
        self.client.post('/files/', {'file': file})

        response = self.client.post('/files/', {'file': duplicate_file}, follow=True)

        self.assertContains(response, text='Duplicate (john, &quot;macro.txt&quot;)')
        self.assertContains(response, text='test.bin')
        upload, duplicate_upload = response.context['uploads']
        self.assertEqual(upload.file, duplicate_upload.file)

    def test_download_duplicate(self):
        self.client.login(username='john', password='1')
        file = _create_uploaded_file('macro.txt')
        duplicate_file = _create_uploaded_file('test.bin', content_type='application/octet-stream')
        self.client.post('/files/', {'file': file})
        self.client.post('/files/', {'file': duplicate_file})
        response = self.client.get('/files/')
        upload, duplicate_upload = response.context['uploads']
        self.client.logout()

        response = self.client.get('/files/downloads/%s' % upload.uuid)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=macro.txt')

        response = self.client.get('/files/downloads/%s' % duplicate_upload.uuid)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/octet-stream')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=test.bin')

    def test_delete_duplicate(self):
        self.client.login(username='john', password='1')
        file = _create_uploaded_file('macro.txt')
        duplicate_file = _create_uploaded_file('test.bin')
        self.client.post('/files/', {'file': file})
        self.client.post('/files/', {'file': duplicate_file})
        response = self.client.get('/files/')
        upload, duplicate_upload = response.context['uploads']

        self.client.get('/files/delete/%s' % upload.uuid)
        self.assertTrue(os.path.isfile(upload.file.path))

        self.client.get('/files/delete/%s' % duplicate_upload.uuid)
        self.assertFalse(os.path.isfile(upload.file.path))

    @override_settings(FILE_LIMIT=2)
    def test_file_limit(self):
        self.client.login(username='john', password='1')
        for file_name in ['macro.txt', 'image.png']:
            file = _create_uploaded_file(file_name)
            response = self.client.post('/files/', {'file': file}, follow=True)
            self.assertContains(response, text=file_name)

        file = _create_uploaded_file('file.doc')
        response = self.client.post('/files/', {'file': file}, follow=True)

        self.assertContains(response, text='You have reached the limit of 2 files')
        self.assertNotContains(response, text='test.bin')


def _create_uploaded_file(name='macro.txt', content_type='text/plain'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'test_data', name)
    with open(file_path, 'rb') as file:
        return SimpleUploadedFile(file.name, file.read(), content_type=content_type)
