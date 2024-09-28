def better_name(first_name, second_name):
    if first_name == "" or second_name =="":
        return "nevyplnili jste něco"             # lze použít i samostatně!
    full_name = first_name + " " + second_name
    return full_name.title() 
    # print("Vypiš mě!!!")            # pozor, za returnem už nic nepokračuje!!
                        

result = better_name("david", "křeček")
print(result)