from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from .models import ErrSys, ErrSysType


def get_system_list_common_data(request, system_all_list):
    paginator = Paginator(system_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_articles = paginator.get_page(page_num)
    currentr_page_num = page_of_articles.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取日期归档对应的文章数量
    article_dates = ErrSys.objects.dates('created_time', 'month', order="DESC")
    article_dates_dict = {}
    for article_date in article_dates:
        article_count = ErrSys.objects.filter(created_time__year=article_date.year,
                                         created_time__month=article_date.month).count()
        article_dates_dict[article_date] = article_count

    context = {}
    context['articles'] = page_of_articles.object_list
    context['page_of_articles'] = page_of_articles
    context['page_range'] = page_range
    context['ErrSysTypes'] = ErrSysType.objects.annotate(article_count=Count('errsys_e'))
    context['article_dates'] = article_dates_dict
    return context


def article_list(request):
    article_all_list = ErrSys.objects.all()
    context = get_system_list_common_data(request, article_all_list)
    return render_to_response('oas/blog_list.html', context)


def article_with_type(request, err_type_pk):
    err_type = get_object_or_404(ErrSysType, pk=err_type_pk)
    err_all_list = ErrSys.objects.filter(err_type=err_type)
    context = get_system_list_common_data(request, err_all_list)
    context['err_type'] = err_type
    return render_to_response('oas/blogs_with_type.html', context)


def article_with_date(request, year, month):
    article_all_list = ErrSys.objects.filter(created_time__year=year, created_time__month=month)
    context = get_system_list_common_data(request, article_all_list)
    context['article_with_date'] = '%s年%s月' % (year, month)
    return render_to_response('oas/blogs_with_date.html', context)


def article_detail(request, article_pk):
    article = get_object_or_404(ErrSys, pk=article_pk)
    if not request.COOKIES.get('ErrSys_%s_readed' % article_pk):
        article.readed_num += 1
        article.save()

    context = {}
    context['previous_article'] = ErrSys.objects.filter(created_time__gt=article.created_time).last()
    context['next_article'] = ErrSys.objects.filter(created_time__lt=article.created_time).first()
    context['article'] = article
    response = render_to_response('oas/blog_detail.html', context) # 响应
    response.set_cookie('ErrSys_%s_readed' % article_pk, 'true')
    return response