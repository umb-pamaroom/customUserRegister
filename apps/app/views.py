from django.shortcuts import render
from .models import Memo
from django.shortcuts import get_object_or_404
from .forms import MemoForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def index(request):

  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/index.html', {'memos': memos})


@login_required
def detail(request, memo_id):
  # プライマリキーをmemo_idにする
  memo = get_object_or_404(Memo, id=memo_id)
  return render(request, 'app/detail.html', {'memo': memo})


# def date(request, memo_dateData):
#   month = self.kwargs.get('month')
#   year = self.kwargs.get('year')
#   day = self.kwargs.get('day')
#   memo = get_object_or_404(Memo, dateData=dateData)
#   return render(request, 'app/detail.html', {'memo': memo})

@login_required
def new_memo(request):
  return render(request, 'app/new_memo.html')


@login_required
def new_memo(request):
    form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form})


@login_required
def new_memo(request):
    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form})


@login_required
def meal_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/meal_list.html', {'memos': memos})


@login_required
def breakfast_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/breakfast_list.html', {'memos': memos})


@login_required
def lunch_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/lunch_list.html', {'memos': memos})


@login_required
def dinner_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/dinner_list.html', {'memos': memos})


@login_required
@require_POST
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('app:index')


@login_required
def edit_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'app/edit_memo.html', {'form': form, 'memo': memo})
