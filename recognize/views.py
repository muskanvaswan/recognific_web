from django.shortcuts import render
from .camera import VideoCamera

# Create your views here.
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
from django.template import loader, Context
from django.http import StreamingHttpResponse

t = loader.get_template('recognize/camera.html')  # or whatever
buffer = '+' * 1024


def face_view(request):
    return render(request, 'recognize/face.html')


def gen_rendered(camera):
    for i in range(20):
        frame = camera.detect()
        yield (b'--frame\r\n'
               b'Content-Type: image.jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def stream_view(request):
    response = StreamingHttpResponse(gen_rendered(VideoCamera()),
                                     content_type='multipart/x-mixed-replace; boundary=frame')
    return response
