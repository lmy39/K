from utils.getPublicData import getAllHourse_infoMap,cityList

def getHomeGeoCharData(hourse_data):
    average_price_dic = average_price(hourse_data)
    cityDic = {}
    for key,value in average_price_dic.items():
        for j in cityList:
            for k in j['city']:
                if k.find(key) != -1:
                    cityDic[j['province']] = value
    cityDicList = []
    for key,value in cityDic.items():
        cityDicList.append({
            'name': key,
            'value': value
        })
    return cityDicList

def getHomeRadarData(hourse_data):
    cityDic = {}
    for i in hourse_data:
        if cityDic.get(i.city,-1) == -1:
            cityDic[i.city] = 1
        else:
            cityDic[i.city] += 1

    radarOne = []
    radarTwo = list(cityDic.values())
    for key,value in cityDic.items():
        radarOne.append({
            'name': key,
            'max': 100
        })
    return radarOne,radarTwo
def getHomeTagsData(hourse_data):
    maxPrice = 0
    maxHourseType = {}
    maxHourseSale_status = {}
    for i in hourse_data:
        if maxPrice < int(i.price):
            maxPrice = int(i.price)
        if maxHourseType.get(i.hourseType,-1) == -1:
            maxHourseType[i.hourseType] = 1
        else:
            maxHourseType[i.hourseType] += 1
        if maxHourseSale_status.get(i.sale_status,-1) == -1:
            maxHourseSale_status[i.sale_status] = 1
        else:
            maxHourseSale_status[i.sale_status] += 1
    maxHourseTyoeSort = list(sorted(maxHourseType.items(),key=lambda x:x[1],reverse=True))
    maxHourseSale_statusSort = list(sorted(maxHourseSale_status.items(), key=lambda x: x[1], reverse=True))

    maxHourseSale = ''
    if maxHourseSale_statusSort[0][0] == '1':
        maxHourseSale = '在售'
    elif maxHourseSale_statusSort[0][0] == '2':
        maxHourseSale = '已售'
    elif maxHourseSale_statusSort[0][0] == '3':
        maxHourseSale = '出租中'
    elif maxHourseSale_statusSort[0][0] == '4':
        maxHourseSale = '已出租'
    elif maxHourseSale_statusSort[0][0] == '5':
        maxHourseSale = '预售'
    elif maxHourseSale_statusSort[0][0] == '6':
        maxHourseSale = '其它'

    return len(hourse_data),maxPrice,maxHourseTyoeSort[0][0],maxHourseSale

def getHourseByHourseName(searchWord,hourse_data):
    searchList = []
    for hourse in hourse_data:
        if hourse.title.find(searchWord) != -1:
            searchList.append(hourse)
    return searchList
def average_price(hourse_data):
    city_prices = {}
    city_counts = {}
    for house in hourse_data:
        city = house.city
        prices = int(house.price)
        if city in city_prices:
            city_prices[city] += prices
            city_counts[city] += 1
        else:
            city_prices[city] = prices
            city_counts[city] = 1

    average_prices = {}
    for city in city_prices:
        average_prices[city] = round(city_prices[city] / city_counts[city], 1)

    return average_prices

def getPriceCharOneData(hourseList):
    X = ['<=4000','4000-6000','6000-8000','8000-10000','10000-12000','12000-15000','15000-18000','>=20000']
    Y = [0 for x in range(len(X))]
    for h in hourseList:
        if int(h.price) <= 4000:
            Y[0] +=1
        elif int(h.price) <=6000:
            Y[1] +=1
        elif int(h.price) <=8000:
            Y[2] +=1
        elif int(h.price) <=10000:
            Y[3] +=1
        elif int(h.price) <=12000:
            Y[3] +=1
        elif int(h.price) <=15000:
            Y[4] +=1
        elif int(h.price) <=18000:
            Y[5] +=1
        elif int(h.price) >=20000:
            Y[6] +=1

    return X,Y

def getPriceCharDataThree(hourseList):
    data = []
    for h in hourseList:
        data.append(
            h.totalPrice_range
        )
    return data

def getDetailCharOne(hourseList):
    roomsDic = {}
    for i in hourseList:
        for room in i.rooms_desc:
            if roomsDic.get(room,-1) == -1:
                roomsDic[room] = 1
            else:
                roomsDic[room] += 1
    resData = []
    for key,value in roomsDic.items():
        resData.append({
            'name':key,
            'value':value
        })
    return resData

def getDetailCharTwo(hourseList,type):
    if type=='big':
        xData = [
            '80-100',
            '100-110',
            '110-120',
            '120-130',
            '130-140',
            '140-150',
            '150-160',
            '160-170',
            '170-180',
            '200-n'
        ]
    else:
        xData = [
            '0-40',
            '40-60',
            '60-80',
            '80-100',
            '100-120',
            '120-150',
            '150-n'
        ]
    yData = [0 for x in range(len(xData))]
    for i in hourseList:
        if len(i.area_range) == 1 :continue
        if type == 'big':
            if float(i.area_range[1]) >= 80 and float(i.area_range[1]) < 100:
                yData[0] +=1
            elif float(i.area_range[1]) <= 110:
                yData[1] +=1
            elif float(i.area_range[1]) <= 120:
                yData[2] +=1
            elif float(i.area_range[1]) <= 130:
                yData[3] +=1
            elif float(i.area_range[1]) <= 140:
                yData[4] +=1
            elif float(i.area_range[1]) <= 150:
                yData[5] +=1
            elif float(i.area_range[1]) <= 160:
                yData[6] +=1
            elif float(i.area_range[1]) <= 170:
                yData[7] +=1
            elif float(i.area_range[1]) <= 180:
                yData[8] +=1
            elif float(i.area_range[1]) >= 200:
                yData[9] +=1
        else:
            if float(i.area_range[0]) <= 40:
                yData[0] +=1
            elif float(i.area_range[0]) <= 80:
                yData[1] +=1
            elif float(i.area_range[0]) <= 100:
                yData[2] +=1
            elif float(i.area_range[0]) <= 120:
                yData[3] +=1
            elif float(i.area_range[0]) <= 150:
                yData[4] +=1
            elif float(i.area_range[0]) <= 150:
                yData[5] +=1
            elif float(i.area_range[0]) > 150:
                yData[6] +=1

    return xData,yData