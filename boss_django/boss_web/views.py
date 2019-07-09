import json

import pymongo
from django.http import HttpResponse
from django.shortcuts import render
from boss_web.models import CareerInfo

from boss_web.yueluoPaginator import YueluoPaginator
from django.core.paginator import EmptyPage, PageNotAnInteger

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['Boss']
item_info = ceshi['details5']
item_info1 = ceshi['data']
item_info2 = ceshi['data1']

TYPE1 = ''


FLAG = 0
TYpe =set()
[TYpe.add(item['type']) for item in CareerInfo.objects.all() ]

def data_gen():
    client = pymongo.MongoClient('localhost', 27017)
    ceshi = client['Boss']
    item_info = ceshi['details5']
    item_info1 = ceshi['data']
    item_info2 = ceshi['data1']
    for i in item_info.find():
        if i['experience'] == '3-5年':
            experience = '3年'
        elif i['experience'] == '5-10年':
            experience = '5年'
        elif i['experience'] == '1-3年':
            experience = '1年'
        else:
            experience = '0'
        salary = i['salary'].strip("")
        item_info1.insert({'experience':experience, 'salary':salary })


    job_type = []
    for i in item_info.find():
        if i['type'].find(".") != -1:
            i['type'] = i['type'].replace('.', '-')
        if i['type'] not in job_type:
            job_type.append(i['type'])
    item_info1.insert({'job_type': job_type})


    data = {}
    for i in job_type:
        data[i] = {}
        data[i]['experience'] = []
        data[i]['salary'] = []
        data[i]['education'] = []
    for i in item_info.find():
        if i['type'].find(".") != -1:
            i['type'] = i['type'].replace('.', '-')
        data[i['type']]['experience'].append(i['experience'])
        data[i['type']]['salary'].append(i['salary'])
        data[i['type']]['education'].append(i['education'])
    item_info2.insert(data)
    # print(data)


    ave_salary = {}
    data1 = {}
    for i in item_info2.find():
        for j in i.items():
            if j[0] != '_id':
                data1[j[0]] = j[1]
    for i in data1.items():
        min_sum = 0
        max_sum = 0
        #     print(i[1])
        #     print(i[1]['salary'])
        for j in i[1]['salary']:
            min = j.split('k')[0]
            max = j.split('k')[1].split('-')[1]
            min_sum = int(min) + min_sum
            max_sum = int(max) + max_sum
        num = len(i[1]['salary'])
        ave_min = int(min_sum / num)
        ave_max = int(max_sum / num)
        ave_salary[i[0]] = [ave_min, ave_max]
    item_info1.insert({'ave_salary': ave_salary})
    # print(ave_salary)

    educations = {}
    for i in data1.items():
        #     print(i[0],i[1]['education'])
        post_time = {}
        for index in i[1]['education']:
            post_time[index] = (i[1]['education'].count(index))
        educations[i[0]] = post_time
    item_info1.insert({'educations': educations})
    # print(educations)

    experience = {}
    for i in data.items():
        post_time = {}
        for index in i[1]['experience']:
            post_time[index] = (i[1]['experience'].count(index))
        experience[i[0]] = post_time
    item_info1.insert({'update_experience': experience})
    # print(experience)

def split_page(request):
    career_info1 = []
    global FLAG, TYPE1 , TYpe
    # print(TYpe, '*' * 10)
    if request.method == "POST":
        FLAG = 1
        type = request.POST.getlist('type')[0]
        TYPE1 = type
        [career_info1.append(item) for item in CareerInfo.objects.all() if item['type'] == type]
        career_info = CareerInfo.objects[:8]
        per_page = 15
        paginator = YueluoPaginator(career_info1, per_page)
        # 取出当前需要展示的页码, 默认为1
        page_num = request.GET.get('page', default='1')
        # 根据页码从分页器中取出对应页的数据
        try:
            page = paginator.page(page_num)
        except PageNotAnInteger as e:
            # 不是整数返回第一页数据
            page = paginator.page('1')
        except EmptyPage as e:
            # 当参数页码大于或小于页码范围时,会触发该异常
            print('EmptyPage:{}'.format(e))
            if int(page_num) > paginator.num_pages:
                # 大于 获取最后一页数据返回
                page = paginator.page(paginator.num_pages)
            else:
                # 小于 获取第一页
                page = paginator.page(1)
        context = {
            'ArtInfo': page,
            'counts': career_info.count(),
            'type': 'c',
            'search_type': TYpe,
            'job_orientation':len(TYpe)
        }
        return render(request, 'search.html', context)
    else:
        [career_info1.append(item) for item in CareerInfo.objects.all()]
        career_info = CareerInfo.objects[:8]
        per_page = 15
        paginator = YueluoPaginator(career_info1, per_page)
        # 取出当前需要展示的页码, 默认为1
        page_num = request.GET.get('page', default='1')
        # 根据页码从分页器中取出对应页的数据
        try:
            page = paginator.page(page_num)
        except PageNotAnInteger as e:
            # 不是整数返回第一页数据
            page = paginator.page('1')
        except EmptyPage as e:
            # 当参数页码大于或小于页码范围时,会触发该异常
            print('EmptyPage:{}'.format(e))
            if int(page_num) > paginator.num_pages:
                # 大于 获取最后一页数据返回
                page = paginator.page(paginator.num_pages)
            else:
                # 小于 获取第一页
                page = paginator.page(1)
        context = {
            'CareerInfo': page,
            'counts': career_info.count(),
            'type': 'c',
            'search_type': TYpe,
            'job_orientation': len(TYpe)
        }
        if request.method == "POST":
            return HttpResponse('http://localhost:8000/search/')
        return render(request, 'index.html', context)

def search(request):
    career_info1 = []
    global TYPE1
    if request.method == 'POST':
        TYPE1 = request.POST.getlist('type')[0]
    if TYPE1 == '':
        [career_info1.append(item) for item in CareerInfo.objects.all()]
    else:
        [career_info1.append(item) for item in CareerInfo.objects.all() if item['type'] == TYPE1]
    s = set(career_info1)
    career_info = CareerInfo.objects[:8]
    per_page = 15
    paginator = YueluoPaginator(career_info1, per_page)
    # 取出当前需要展示的页码, 默认为1
    page_num = request.GET.get('page', default='1')
    # 根据页码从分页器中取出对应页的数据
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger as e:
        # 不是整数返回第一页数据
        page = paginator.page('1')
    except EmptyPage as e:
        # 当参数页码大于或小于页码范围时,会触发该异常
        print('EmptyPage:{}'.format(e))
        if int(page_num) > paginator.num_pages:
            # 大于 获取最后一页数据返回
            page = paginator.page(paginator.num_pages)
        else:
            # 小于 获取第一页
            page = paginator.page(1)
    context = {
        'CareerInfo': page,
        'counts1': len(s),
        'counts': career_info.count(),
        'type': 'c',
        'search_type': TYpe,

    }
    return render(request, 'search.html', context)

def chart(request):
    ave_salary_list = []
    ave_salary = {}
    # 将 ave_salary放入格式为 [{'value': 9.5, 'name': '电子工程师'},....]的列表
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'ave_salary':
                for z in j[1].items():
                    if z[0].find("-") != -1:
                        b = z[0].replace('-', '.')
                    else:
                        b = z[0]
                    salary_ave = (z[1][0] + z[1][1]) / 2
                    ave_salary['name'] = b
                    ave_salary['value'] = salary_ave
                    ave_salary_list.append(ave_salary)
                    ave_salary = {}
    # print(ave_salary_list)
    a_list = []
    da = {}
    data1 = {}
    name = ""
    a23 = ""
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'classify':
                for z in j[1].items():
                    print("zz", z[0])
                    for k in z[1]:
                        # print("k:", k)
                        for x in ave_salary_list:
                            # print("xx:",x)
                            for l in x.items():
                                if l[0] == 'name':
                                    name = l[1]
                            if k == name:
                                data1['data'] = x
                                name = ''
                                a23 = x
                        #
                        a_list.append(a23)
                        a23 = ''
                        print("aaaaa:", a_list)
                    da[z[0]] = a_list
                    data1 = {}
                    a_list = []
    print("da:", da)
    new_data = {}
    new_data_list = []
    for i in da.items():
        new_data['name'] = i[0]
        new_data['data'] = i[1]
        new_data_list.append(new_data)
        new_data = {}
        # print(i, i[0],[1])

    context = {
        'series': new_data_list,
    }
    return render(request, 'chart.html', context)

def salary(request):
    # 图一
    categories = []
    salary_data = []
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'ave_salary':
                for z in j[1].items():
                    if z[0].find("-") != -1:
                        b = z[0].replace('-', '.')
                    else:
                        b = z[0]
                    categories.append(b)
                    salary_data.append(z[1])
    # 图二
    # # 取城市的第一个字段,设置值为0的键值对
    flag =0
    ave_salary={}
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'ave_salary_two':
                ave_salary=j[1]
                flag=1
                print("12",j[1])
                break
    if flag==0:
        cite = []
        for i in item_info.find():
            s = i['location'].split(" ")[0]
            cite.append(s)
        cite = set(cite)
        cite_list = {}
        for i in cite:
            cite_list[i] = 0
        # print(cite_list)
        for i in item_info.find():
            for j in cite_list.items():
                if i['location'].split(" ")[0] == j[0]:
                    cite_list[j[0]] = j[1] + 1
                    continue
        # print(cite_list)
        # 删除少于550个的城市的键值对
        cite_del = []
        for j in cite_list.items():
            if j[1] < 550:
                cite_del.append(j[0])
        for i in cite_del:
            del cite_list[i]
        # 计算城市的平均薪资
        data = {}
        for j in cite_list.items():
            data[j[0]] = 0
        # print(data)  # 初始化平均薪资键值对为0
        for i in item_info.find():
            for j in cite_list.items():
                if i['location'].split(" ")[0] == j[0]:
                    data[j[0]] += (int(i['salary'].split('k')[0]) - int(i['salary'].split('k')[1])) / 2
        # print(data)    # 各城市总薪资 传入数据
        for i in data.items():
            for j in cite_list.items():
                if j[0] == i[0]:
                    data[i[0]] = i[1] / j[1]
        # print(data)   # 各城市平均总薪资
        ave_salary = sorted(data.items(), key=lambda data: data[1], reverse=True)
        # print(ave_salary)  #按键值对的值 从大到小排序
        item_info1.insert({'ave_salary_two':ave_salary})
    q = []
    for i in ave_salary:
        q.append(list(i))
    # print(q)
    context = {
        'categories':categories,
        'salary_data': salary_data,
        'data':q
    }
    return render(request, 'salary.html',context )

def education(request):
    c = {}
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'educations':
                for z in j[1].items():
                    if z[0].find("-") != -1:
                        b = z[0].replace('-', '.')
                    else:
                        b = z[0]
                    c[b]=z[1]
    da = {}
    data1 = {}
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'classify':
                for z in j[1].items():
                    for k in z[1]:
                        for l in c.items():
                            if k == l[0]:
                                data1[k] = l[1]
                    da[z[0]] = data1
                    data1 = {}


    context = {
        'data':json.dumps(da),

    }
    return render(request, 'education.html',context)

def experience(request):
    # 图一
    c = {}
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'experience':
                for z in j[1].items():
                    if z[0].find("-") != -1:
                        b = z[0].replace('-', '.')
                    else:
                        b = z[0]
                    c[b]=z[1]
    da = {}
    data1 = {}
    for i in item_info1.find():
        for j in i.items():
            if j[0] == 'classify':
                for z in j[1].items():
                    for k in z[1]:
                        for l in c.items():
                            if k == l[0]:
                                data1[k] = l[1]
                    da[z[0]] = data1
                    data1 = {}
    print(da)
    # 图二
    num = [0, 0, 0, 0, 0]
    for i in item_info.find():
        if i['experience'] == '10年以上':
            num[4] += 1
        elif i['experience'] == '5-10年':
            num[3] += 1
        elif i['experience'] == '3-5年':
            num[2] += 1
        elif i['experience'] == '1-3年':
            num[1] += 1
        else:
            num[0] += 1
    # print(num)
    # {
    #     name: 'Microsoft Internet Explorer',
    #     y: 56.33,
    # },
    data_dict = {}
    data_list = []
    num_name = ['1年以下', '1-3年', '3-5年', '5-10年', '10年以上']
    num_total = num[0] + num[1] + num[2] + num[3] + num[4]
    for i in range(0, 5):
        data_dict['name'] = num_name[i]
        data_dict['y'] = num[i] / num_total * 100
        data_list.append(data_dict)
        data_dict = {}
    print(data_list)
    context = {
        'data':json.dumps(da),
        'data_list': json.dumps(data_list),
    }
    return render(request, 'experience.html',context)

