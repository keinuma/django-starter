
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

from .forms import ItemForm
from .models import Item, WishList


@login_required
def edit(request, lego_id):
    # itemの取得
    item = get_object_or_404(Item, id=lego_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lego_index'))
    else:
        form = ItemForm(instance=item)
        context = {'form': form, 'item': item}
        return TemplateResponse(request, 'lego/edit.html', context=context)


@login_required
@require_POST
def delete(request, lego_id):
    # itemの取得
    item = get_object_or_404(Item, id=lego_id)

    # itemの削除
    item.delete()

    return HttpResponseRedirect(reverse('lego_index'))


@login_required
def index(request):
    # item一覧を取得し、辞書に格納
    context = {'items': Item.objects.all()}
    return TemplateResponse(request, 'lego/list.html', context=context)


@login_required
@require_POST
def add_to_wish_list(request, lego_id):
    # itemの取得
    item = get_object_or_404(Item, id=lego_id)

    # wishlistの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # wishlistに該当するitemを追加
    wish_list.items.add(item)

    return HttpResponseRedirect(reverse('wish_list_index'))


@login_required
@require_POST
def delete_from_wish_list(request, lego_id):
    # itemの取得
    item = get_object_or_404(Item, id=lego_id)

    # wishlistの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # wishlistから該当するitemを削除
    wish_list.items.remove(item)

    return HttpResponseRedirect(reverse('wish_list_index'))


@login_required
def wish_list_index(request):
    # 欲しいものリストの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # 欲しいものリストに含まれる全てのitemを取得して、辞書に格納
    context = {'items': wish_list.items.all()}
    return TemplateResponse(request, 'wish_list/list.html', context=context)
