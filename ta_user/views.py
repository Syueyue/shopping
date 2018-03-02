from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse

from hashlib import sha1
from ta_user.models import User,Address
from ta_goods.models import GoodInfo
from ta_user import user_decorator

# Create your views here.
def login(request):
    uname=request.COOKIES.get('uname','')
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,
             'pwd':pwd,
             'error':0}
    try:
        url=request.META['HTTP_REFERER']
        if '/user/reg'in url:raise Exception()

    except:url='/'

    response=render(request,'ta_user/login.html',context)
    response.set_cookie('url',url)
    return response

def register(request):
    return render(request,'ta_user/reg.html')



def login_handle(request):
    post=request.POST#接受表单请求
    uname=post.get('username')
    pwd=post.get('pwd')
    remember=post.get('remember','0')
    s=sha1()
    s.update(pwd.encode('utf8'))   #先编码
    upwd=s.hexdigest()
    #mysql语句，游标获取关闭，提交一条信息
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first()
    if user:
        url=request.COOKIES.get('url','/')  #根目录
        red=HttpResponseRedirect(url)
        #1将保存几天，否则只保存一瞬间   浏览器里面
        if remember=='1':
            red.set_cookie('uname',uname.encode('utf-8'))
            red.set_cookie('upwd',pwd)
        else:
            red.set_cookie('uname','',max_age=-1)
            red.set_cookie('upwd','',max_age=-1)
            #服务器里保存  半小时
        request.session['username']=uname
        request.session['uid']=user.id
        return red
    else:
        context={'error':1,'uname':uname}
        return render(request,'ta_user/login.html',context)  #成功进入首页否则还在原页面
def register_handle(request):
    post=request.POST
    uname=post.get('username','')
    pwd=post.get('pwd','')
    cpwd=post.get('cpwd','')
    uemail=post.get('email','')

    if pwd !=cpwd:
        return redirect('/user/reg')
    s1=sha1()
    s1.update(pwd.encode('utf8'))
    pwd=s1.hexdigest()
    user=User()  #存入数据库
    user.uname=uname
    user.upwd=pwd
    user.uemil=uemail
    user.save()
    return redirect('/user/login')

def logout(request):
    request.session.flush()
    return redirect('/')

def register_exist(request):
    uname=request.GET.get('un')
    count=User.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def user_center(request):
    return  render(request,'ta_user/用户中心.html',locals())

@user_decorator.login
def user_center_info(request):
    username=request.session.get('username','')
    user=User.objects.filter(uname=username).first()
    goodids=request.COOKIES.get('goodids','')
    goods_list=[]
    if goodids !='':
        goodids=goodids.split(',')
        for i in goodids:
            goods_list.append(GoodInfo.objects.filter(pk=i).first())
            pass
    return render(request,'ta_user/用户中心-用户信息.html',locals())

@user_decorator.login
def shdz(request):
    adds=Address.objects.filter(uid= request.session.get('uid',''),scbz=0)
    return render(request,'ta_user/用户中心-收货地址.html',locals())

def userupdate(request):
    post=request.POST
    uid=request.session.get('uid','')
    user=User.objects.filter(id=uid).first()
    user.uname=post.get('un','')
    user.urelname=post.get('urn','')
    user.uphone=post.get('uphone','')
    user.uemail=post.get('uemil','')
    user.usex=post.get('usex','')
    user.save()
    request.session['username']=user.uname
    return redirect('/')


@user_decorator.login
def add_save(request):
    post=request.POST
    aid=post.get('aid')
    print(aid)
    if aid:
         Address.objects.filter(id=aid).update(reciver=post.get('reciver'),sheng=post.get('sheng'),shi=post.get('shi'),
                                               qu=post.get('qu'),rphone=post.get('rphone'),tphone=post.get('tphone'),
                                               detialaddr=post.get('detialaddr'),
                                               yzbm=post.get('yzbm'))
    else: Address.objects.create(reciver=post.get('reciver'),sheng=post.get('sheng'),shi=post.get('shi'),
                                                uid=request.session['uid'],
                                               qu=post.get('qu'),rphone=post.get('rphone'),tphone=post.get('tphone'),
                                               detialaddr=post.get('detialaddr'),
                                               yzbm=post.get('yzbm'))

    adds=Address.objects.filter(uid= request.session.get('uid',''),scbz=0)
    return render(request,'ta_user/用户中心-收货地址.html',locals())

@user_decorator.login
def mrdz(request):
     dzid=request.GET.get('dzid')
     Address.objects.all().update(mrdz=0)
     add=Address.objects.filter(id=dzid).update(mrdz=1)
     return redirect('/user/shdz')

@user_decorator.login
def scbz(request):
     dzid=request.GET.get('dzid')
     Address.objects.filter(id=dzid).update(scbz=1)
     return redirect('/user/shdz')


@user_decorator.login
def bjdz(request):
    dzid=request.GET.get('dzid')
    add=Address.objects.get(id=dzid)
    adds=Address.objects.filter(uid= request.session.get('uid',''),scbz=0)
    return render(request,'ta_user/用户中心-收货地址.html',locals())


