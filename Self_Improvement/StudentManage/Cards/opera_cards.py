def add_card(cards):
    name = input("请输入姓名:")
    tel = input("请输入联系电话:")
    job = input("请输入职位:")
    company = input("请输入公司名称:")
    addr = input("请输入公司地址:")
    # 将用户的输入组合成一张名片
    card = {"name": name, "tel": tel, "job": job, "company": company, "addr": addr}
    cards.append(card)
    print(f"您的新名片{name}已添加成功!")
    return cards


def show_all(cards):
    print("编号\t\t姓名\t\t联系电话\t\t职位\t\t公司名称\t\t公司地址")
    for id, card in enumerate(cards):
        for v in card.values():
            print(v, end="\t\t")
        print()


def search_card(cards):
    Search_Name = input("请输入要查询的名片姓名:")
    for card in cards:
        if card.get("name") == Search_Name:
            print("姓名\t\t联系电话\t\t职位\t\t公司名称\t\t公司地址")
            for v in card.values():
                print(v, end="\t\t")
    else:
        print("您查询的名片不存在")


def update_card(cards):
    Update_Name = input("请输入要修改的名片姓名:")
    for card in cards:
        if card.get("name") == Update_Name:
            New_Name = input("请输入新名片的姓名:")
            New_Tel = input("请输入新名片的联系电话:")
            New_Job = input("请输入新名片的职位:")
            New_Company = input("请输入新名片的公司名称:")
            New_Addr = input("请输入新名片的公司地址:")
            print("姓名\t\t联系电话\t\t职位\t\t公司名称\t\t公司地址")
            print(f"{card['name']}\t\t{card['tel']}\t\t{card['job']}\t\t{card['company']}\t\t{card['addr']}")
            if_sure = input("请确认信息是否正确,请输入y/n：")
            if if_sure == "y":
                card["name"] = New_Name
                card["tel"] = New_Tel
                card["job"] = New_Job
                card["company"] = New_Company
                card["addr"] = New_Addr
            else:
                print("结束")


def delete_card(cards):
    Delete_Name = input("请输入要删除的名片姓名:")
    for card in cards:
        if card.get("name") == Delete_Name:
            cards.remove(card)
            print(f"名片:{card.get('name')}已被移除")
            break
    else:
        print("card is not exist")


def quit_card():
    exit("退出系统")


def run():

    while True:
        with open("Cards", "r", encoding="utf-8") as file_card:
            file_reads = file_card.readlines()
            for line in file_reads:
                line = line.rstrip()
                a = line.split(",")
                print(a)
            # file_head = cards_list[0].split(",")
            #             # Cards = []
            #             # cards_list.pop(0)
            # for card_every_line in cards_list:
            #     info = {}
            #     card_line_list = card_every_line.split(",")
            #     for i in range(len(card_line_list)):
            #         for j in range(i, i + 1):
            #             info[file_head[j]] = card_line_list[i]
            #     Cards.append(info)
            # print(Cards)

        print("""
        =====欢迎登录名片管理系统v1.0=====
             ***** 1.添加名片***** 
             ***** 2.显示名片*****
             ***** 3.查询名片*****
             ***** 4.修改名片***** 
             ***** 5.删除名片***** 
             ***** 0.退出系统*****
        """)

        num = input("请输入您要执行的操作:")
        if num == "1":
            cards = add_card(cards)
        elif num == "2":
            show_all(cards)
        elif num == "3":
            search_card(cards)
        elif num == "4":
            update_card(cards)
        elif num == "5":
            delete_card(cards)
        elif num == "0":
            quit_card()
        for card in cards:
            res = []
            for v in card.values():
                res.append(v)
                values = ",".join(res)
                with open("Cards", "a", encoding="utf-8") as f:
                    pass


run()
