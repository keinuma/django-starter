
# HttpResponseクラスのインポート
from django.http import HttpResponse

# TemplateResponseクラスのインポート
from django.template.response import TemplateResponse

import datetime


# hello()関数
def hello(request):

    # テンプレートに渡す辞書
    context = {'message': 'メッセージ'}
    return TemplateResponse(request, 'item/message.html', context=context)


def header(request):

    context = {
        'headers': {
            'schema': request.scheme,
            'path': request.path,
            'method': request.method,
            'context_length': request.META['CONTENT_LENGTH'],
            'http_accept': request.META['HTTP_ACCEPT'],
            'http_accept_language': request.META['HTTP_ACCEPT_LANGUAGE'],
            'user_agent': request.META['HTTP_USER_AGENT'],
            'remote_addr': request.META['REMOTE_ADDR'],
        }
    }
    return TemplateResponse(request, 'item/header.html', context)


def get_requester(request):

    # GETパラメータの取得
    keyword = request.GET['keyword']
    return HttpResponse('keywordは {0} です'.format(keyword))


def post_requester(request):

    # POSTパラメータの取得
    name = request.POST['name']
    return HttpResponse('nameは {0} です'.format(name))


def response_getter(request):

    # ステータスコードを設定
    response = HttpResponse('HttpResponseオブジェクトのサンプル', status=200)

    # ヘッダを設定
    response['Cache-Control'] = 'max-age=0'

    # クッキーを設定
    response.set_cookie('spam', 'egg')

    return response


def pages(request, id):
    return HttpResponse('idは = {}です'.format(id))


def news(request, slug):
    return HttpResponse('slugは = {}です'.format(slug))


def now(request):
    context = {
        'today': datetime.date.today()
    }
    return TemplateResponse(request, 'item/today.html', context=context)
