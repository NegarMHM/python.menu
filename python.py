


#تعریف نوشیدنی ها و برندهای آنها
tea = {
    "type": "چایی",
    "brands": ["شهرزاد" , "گلستان" , "طبیعت"],
}

coffee = {
    "type": "قهوه",
    "brands": ["استارباکس" , "نسکافه" ,"لاواتزا" ],
}

beer = {
    "type": "آبجو",
    "brands": ["توبرگ" , "آلبرو" , "کارلتون درافت"],
}



#تعریف منو و اضافه کردن نوشیدنی ها به آن
menu = {
    tea : "چایی"
    coffee :"قهوه"
    beer : "آبجو"
}


#چاپ منو بصورت خوانا
for item, details in menu.item():
    print(f"{item}:")
    for brand in details['brands']:
        print("f - {brand}")



#بررسی وجود یک مورد در منو
selected_item = "چایی"
if selected_item in menu:
    print(f"بله, '{selected_item}'در منو موجود است")
    esle:
    print(f"خیر, '{selected_item}'در منو موجود نیست")


    #بررسی وجود یک مورد دیگر در منو
    selected_item = "آب"
    if selected_item in menu:
        print(f"بله, '{selected_item}'در منو موجود است")
    else:
        print(f"خیر,'{selected_item}' در منو موجود نیست")
