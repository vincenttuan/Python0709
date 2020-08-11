class Order:
    # 地區 國家 物品種類 銷售渠道 訂單優先 訂購日期 訂單編號 發貨日期 售出單位 單價 單位成本 總收入 總計花費 總利潤
    def __init__(self, region, country, itemType, salesChannel,
                       orderPriority, orderDate, orderID, shipDate,
                       unitsSold, unitPrice, unitCost, totalRevenue,
                       totalCost, totalProfit) -> None:
        self.region = region
        self.country = country
        self.itemType = itemType
        self.salesChannel = salesChannel
        self.orderPriority = orderPriority
        self.orderDate = orderDate
        self.orderID = orderID
        self.shipDate = shipDate
        self.unitsSold = unitsSold
        self.unitPrice = unitPrice
        self.unitCost = unitCost
        self.totalRevenue = totalRevenue
        self.totalCost = totalCost
        self.totalProfit = totalProfit

if __name__ == '__main__':
    # 匯入資料
    file = open('10000 Sales Records.csv', 'r')
    list = []
    for data in file.readlines():
        rows = data.split(",")
        if rows[0] == 'Region':
            continue
        ord = Order(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11],rows[12],rows[13])
        list.append(ord)

    # 列出 物品種類
    for ord in list:
        if float(ord.totalRevenue) > 6600000:
            print(ord.itemType, ord.totalRevenue)