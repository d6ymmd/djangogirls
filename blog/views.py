from django.shortcuts import render

def post_list(request):
    # Template을 찾을 경로에서 수
    # post_list.html을 찾아서 그 파일을 text로 만들어서
    # HttpResponse의 형태로 돌려준다 위기능을 하는 shortcut함
    return render(request, 'post_list.html')