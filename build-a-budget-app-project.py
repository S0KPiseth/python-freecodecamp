import math
class Category:
    def __init__ (self,name):
        self.name = name
        self.ledger = [{"amount": 0, "description": ""}]
        self.first_deposit = 0

    def deposit(self, amount, description=None):
        self.ledger[0]["amount"] +=amount
        self.first_deposit += amount
        self.ledger[0]["description"]= description if description else ""
    def withdraw(self, amount, description=None):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger[0]["amount"] -= amount
            self.ledger.append({"amount": -amount, "description": description if description else ""}) 
            return True
    def get_balance(self):
        return self.ledger[0]["amount"]

    def transfer(self, amount, object_class):

        if not self.check_funds(amount):
            return False
        else:
            object_class.deposit(amount, f'Transfer from {self.name}')
            self.withdraw(amount, f"Transfer to {object_class.name}")
            return True
    def __str__(self):
        list_str =[]
        both_side = "*"*(15 - (len(self.name)//2))
        
        list_str.append(both_side)
        list_str.append(self.name)
        list_str.append(both_side)
        each_vals = float(str(self.first_deposit)[0:6])
        vals = f"{each_vals:.2f}"

        list_str.append("\n" + self.ledger[0]["description"][0:23] + " "* (30-len(self.ledger[0]["description"][0:23])-len(vals)) + vals)
        for j,i in enumerate(self.ledger):
            if j!=0:
                each_vals = float(str(i["amount"])[0:6])
                vals = f"{each_vals:.2f}"

                list_str.append("\n" + i["description"][0:23] + " "* (30-len(i["description"][0:23])-len(vals)) + vals)
        list_str.append(f"\nTotal: {self.get_balance():.2f}")
        return "".join(list_str)
        


    def check_funds(self, amount):
        if self.ledger[0]["amount"] < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    bar =[]
    
    total_withdraw = 0
    for i in categories:
        total_withdraw += i.first_deposit - i.ledger[0]["amount"]
    each_percent = {key.name: math.floor((key.first_deposit - key.ledger[0]["amount"])*10 / total_withdraw) for key in categories}

    #sorted_each_percent = dict(sorted(each_percent.items(), key=lambda item: item[1], reverse=True))
    sorted_each_percent=each_percent
    for row in range(-10,1):
        bar_label = abs(row)*10
        if len(str(bar_label)) == 1:
            bar.append([f"  {bar_label}|"])
        elif len(str(bar_label)) == 2:
            bar.append([f" {bar_label}|"])
        else:
            bar.append([f"{bar_label}|"])

    for index,percent in enumerate(sorted_each_percent.values()):
        hight = int(10-percent)
        for locate in range(len(bar)):
            if locate in [number for number in range (0, hight)]:
                if index ==(len(list(sorted_each_percent.values()))-1):
                    bar[locate].append("    ")
                else:
                    bar[locate].append("   ")
            elif index ==(len(list(sorted_each_percent.values()))-1):
                bar[locate].append(" o  ")
            else:
                bar[locate].append(" o ")

    #bar.append(["    " + "   "*len(categories) +" "])
    bar.append(["    " + "---"*len(categories) +"-"])
    #bar.append(["    " + "   "*len(categories) +" "])

    sorted_label_list = [item for item in sorted_each_percent.keys()]
    
    test=""
    for item in range(len(sorted_label_list)):
        for label in range(max([len(categorie.name) for categorie in categories])):
            try:
                if item==0:
                    bar.insert(12+label, ["     "+sorted_label_list[item][label]])
                elif item == len(sorted_label_list)-1:
                    bar[12+label].append("  "+sorted_label_list[item][label]+"  ")

                else:
                    bar[12+label].append("  "+sorted_label_list[item][label])
            except IndexError:
                if item==0:
                    bar.insert(12+label, ["      "])
                else:
                    bar[12+label].append("   ")

    #print(sorted_label)
    #print(each_percent)

    for i in bar:
        test+=("\n"+ "".join(i))
        #print(i)
    #print("Percentage spent by category" +test)

    return "Percentage spent by category" +test
        


clothing = Category('Clothing')
food = Category('Food')
auto = Category('Auto')
entertainment = Category('Entertainment')
entertainment.deposit(10000)
food.deposit(1000, 'deposit')
auto.deposit(1000)
clothing.deposit(1000, 'deposit')

clothing.withdraw(10)
entertainment.withdraw(10)
auto.withdraw(10)
food.withdraw(2)
print(food)
print(create_spend_chart([food, clothing, auto,entertainment]))
