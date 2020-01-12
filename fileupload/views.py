from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Upload


def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
        	print("hi")
            upload = Upload(file=image_file)
            print("hello")
            print(upload.file)
            upload.save()
            print("saved")
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'upload.html', {
            'image_url': image_url
        })
    return render(request, 'upload.html')
