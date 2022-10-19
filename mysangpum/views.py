from django.shortcuts import render
import MySQLdb
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# sangdata table과 연동
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    #SQL문 직접 사용
    '''
    sql = "select * from sangdata"
    conn = MySQLdb.connect(**config) #dict type data
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas, type(datas))
    '''
    """
    datas = Sangdata.objects.all() # ORM 반환형 QuerySet
    
    return render(request, 'list.html', {'sangpums' : datas})
    """
    
    # 페이지 나누기 ------------
    datas = Sangdata.objects.all().order_by('-code')
    paginator = Paginator(datas, 3)
    
    try:
        page = request.GET.get('page')
    except:
        page = 1
        
    try:
        data = paginator.page(page)   # page에 해당되는 자료를 읽기
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
    
    
    # 낱개 페이지 번호를 출력한다면 ....
    allpage = range(paginator.num_pages + 1) # (0, 4 + 1)
    
    
    
    
    return render(request, 'list2.html', {'sangpums':data,'allpage':allpage}) # 낱개페이지 번호도 같이 출력
    

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        # 신상품 code 등록 여부 판단.
        try:
            Sangdata.objects.get(code=request.POST.get('code')) # code번호를 읽고
            # 이미 있으면 
            return render(request, 'insert.html', {'msg':'이미 등록된 code입니다.'}) # 여기로 다시 보낸다
        except Exception as e: 
            # 입력 자료의 code가 등록된 숫자가 아니므로 insert 작업을 진행
            Sangdata(
                code = request.POST.get('code'),
                sang = request.POST.get('sang'),
                su = request.POST.get('su'),
                dan = request.POST.get('dan'),
            ).save()
            
        return HttpResponseRedirect("/sangpum/list") # 추가 후 목록보기
         
def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'sang_one':data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code')) # 수정할 데이터 코드를 읽고
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save() # update 하는거
    
    return HttpResponseRedirect("/sangpum/list") # 수정 후 목록보기!
        
        
def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code')) # 삭제할 데이터 코드를 읽고
    delRec.delete()
    return HttpResponseRedirect("/sangpum/list") # 삭제 후 목록보기!
    
    