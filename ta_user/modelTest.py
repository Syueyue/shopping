from ta_user.models import Address
#查询     获取所有地址
adds1=Address.objects.all()    #获取所有地址
add=Address.objects.get(id=1,reciver='ni') #获取指定字段的记录,可以加多个条件
adds2=Address.objects.all().values_list('id','reciver')  #过滤字段
add2=Address.objects.filter(uid=1,reciver='ni').all()  #符合过滤的所有记录
add3=Address.objects.filter(uid=1,reciver='ni').first()  #符合过滤的第一条记录
#新增
Address.objects.create(reciver='ni',sheng='hebei')  #新增一条数据
add4=Address()
add4.reciver='ni'
add4.save()
#删除
Address.objects.filter(uid=1,reciver='ni').delete() #删除指定数据
#更新
Address.objects.filter(uid=1,reciver='ni').update(reciver='ni',sheng='shengyang')