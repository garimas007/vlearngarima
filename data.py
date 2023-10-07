## prog1

#names = []
#feedbacks = []
data_lists = []

for i in range (0,5):
    data_list = {}
    name = str(input("enter the name"))
    feedback = int(input("enter the feedback"))
    #names.append(name)
    #feedbacks.append(feedback)
    data_list["name"] = name
    data_list["feedback"] = feedback
    data_lists.append(data_list)

print(data_lists)

