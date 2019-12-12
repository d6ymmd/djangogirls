from django.shortcuts import render

from blog.models import Post


def post_list(request):
    # Template을 찾을 경로에서
    # post_list.html을 찾아서 그 파일을 text로 만들어서
    # HttpResponse의 형태로 돌려준다 위기능을 하는 shortcut함수

    # content = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)

    # 1. posts라는 변수에 전체 Post를 가지는 QuerySet객체를 할당
    # hint_ Post.objects. 무엇인가.. 를 실행한 경과는 queryset객체가 된다
    # 2. context라는 dict를 생성하며, 'posts'키에 위 posts변수를 value로 사용하도록 한다
    # 3. render의 3번째 위치인자로 위 context변수를 전달한다

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'post_list.html', context)


def post_detail(request, pk):

    # post = Post.objects.all()[pk-1] -> 이렇게 해도 나오는데 왜 아닌가?
    # posts = Post.objects.filter(pk=pk)[0]
    # post = posts[0]
    context = {
        'post': post,
    }

    # 특정키로 접근하면 value를 바로 갖다쓰면 되니까... 딕셔너리 형태로 정의(없으면 value만으로 알기 좀....?)

    try:
        post = Post.objects.get(pk=pk)
    except:
        return HttpResponse('없음')



    return render(request, 'post_detail.html', context)
