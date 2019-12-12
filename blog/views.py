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


def post_detail(request):

    post = Post.objects.all()[0]
    context = {
        'post': post,
    }

    # 특정키로 접근하면 value를 바로 갖다쓰면 되니까... 딕셔너리 형태로 정의(없으면 value만으로 알기 좀....?)

    # 1.전체 포스트목록(포스트전체 쿼리셋)중 [0]번 인덱스에 해당하는 post객체 하나를 포스트 변수에 할당
    # 2.'context'라는 이름의 딕트를 만들며 'post'key에  위 post변수를 value로 사용한다
    # 3. post_detail.html에서 전달받은 'post'변수의 title, author, text, created_date, published_date를 적절히 출력해준다
    return render(request, 'post_detail.html', context)


