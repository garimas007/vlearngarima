names = ["abc","def","ghi","jkl"]
feedbacks = [3,4,4,5]

#for i in range(0,3):
#    print(names[i])
#
#for i in range(0,3):
#    print(feedbacks[i])

#list = []
#for i in range(0,3):
#    if (feedbacks[i]<4):
#        print(names[i])
#        list.append(names[i])

#print(list)

total = 0
avg = 0
## average
for i in range(0,3):
    flen = len(feedbacks)
    #print(flen)
    total = total + feedbacks[i]
    #print(total)
    avg = total/flen
print(avg)

## Dictionary
learner = {
    "name": "one",
    "feedback": 3,
    "address":{
        "line1":"Bihar",
        "line2":"colg",
        "pin":"123456"
    }
}
print(learner)
print(learner["name"])
print(learner["feedback"])
print(learner["address"]["pin"])