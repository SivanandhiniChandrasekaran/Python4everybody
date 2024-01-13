new_list = ["ten", "when", "ren"]
old_list = new_list
print(old_list)

a=b=c=new_list
a.append("rod")

c.append("of")

new_list.append("rem")
print(old_list)