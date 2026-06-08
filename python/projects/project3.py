#expense tracker



salary=3000
items={}
user_key=input("ENter the category ")
user_value=int(input("Enter how much you spend "))
items[user_key]=user_value

total_expense=sum(items.values())


print(total_expense)


