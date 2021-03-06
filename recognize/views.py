from django.shortcuts import render
from .camera import VideoCamera
from django.http import HttpResponseForbidden, HttpResponse

import json

# Create your views here.
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
from django.template import loader, Context
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

from encode.models import ClassSet
from .sheet import attendance_sheet_day, attendance_sheet_month

t = loader.get_template('recognize/camera.html')  # or whatever
buffer = '+' * 1024


def face_view(request, classname):
    # print(classname)
    ClassSetObject = ClassSet.objects.get(pk=classname.split('class')[1])
    if ClassSetObject.active == True:
        context = {
            "classname": classname,
            "message": "Ensure that there is plenty light in the room."
        }
    else:
        context = {
            "message": "This class is not currently in progress"
        }

    return render(request, 'recognize/face.html', context)


def gen_rendered(camera):
    for i in range(20):
        frame = camera.detect()
        yield (b'--frame\r\n'
               b'Content-Type: image.jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    frame = camera.attendace()[0]

    yield (b'--frame\r\n'
           b'Content-Type: image.jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def stream_view(request, classname):
    response = StreamingHttpResponse(gen_rendered(VideoCamera(classname)),
                                     content_type='multipart/x-mixed-replace; boundary=frame')
    return response


@csrf_exempt
def attendace_api(request, classname):
    if request.method == "POST":
        data = json.loads(request.body)
        # classname = data['classname']
        option = data['option']
        if option == "day":
            date = data['date']

            attendance_sheet_day(date, classname)
            return HttpResponse("True")
            # except:
            # return HttpResponse("False")
        else:
            month = data['month']
            try:
                attendance_sheet_month(month, classname)
                return HttpResponse("True")
            except:
                return HttpResponse("False")
    else:
        return HttpResponseForbidden()
