# d={"name":"john","age":20,"country":"india"}
# print(d)
# print(d["country"])
# for key in d:
#     print(key," ",d[key])
# emp={"empid":123,"company":"HCL","salary":50000}
# print(emp)
# print(emp["empid"])
# print(emp["company"])
# print(emp["salary"])
# for key in emp:
#     print(key," ",emp[key])
# emp={"empid":123,"company":"HCL","salary":50000,"salary":234}
# emp["city"]="unnao"
# emp["salary"]=321
# del emp["salary"]
# print(emp)
# emp.update({"company":"TCS","salary":567894})
# print(emp)
# food={"id":12,"name":"cake","price":250}

# print(food)
# food.update({"name":"spring roll","price":100})
# print(food)
# food.clear()
# food.items()
# for i in food.items():
# for key in food.keys():
# food.keys()
    # print(key)
# print(food.get("id"))
# print(food.get("4","this key is not available"))

# /////////////////
#lex_auth_012693774187716608134

# def translate(bilingual_dict,english_words_list):
#     #Write your logic here
#     swedish_words_list=[]
    
#     for eng in english_words_list:
#         swedish_words_list.append(bilingual_dict[eng])
#     return swedish_words_list


# bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
# english_words_list=["merry","christmas"]
# print("The bilingual dict is:",bilingual_dict)
# print("The english words are:",english_words_list)

# swedish_words_list=translate(bilingual_dict, english_words_list)
# print("The equivalent swedish words are:",swedish_words_list)

# sorted =========
# d={"amit":30,"raj":100,"anil":20}
# for v in sorted(d.values(),reverse=True):
#     print(v)
# d={"amit":30,"raj":100,"anil":20}
# for k in sorted(d.keys(),reverse=True):
#     print(k)
# sqare of elements in dictionary wher key =no.&value=sqare of no.
# d={}
# for i in range(1,16):
#     d[i]=i*i
# print(d)
# d2={1:34,5:56,4:34}
# sum=0
# for i in d2:
#     sum=sum+d2[i]
# print(sum)

========================================================
#lex_auth_01269444890062848087

def find_correct(word_dict):
    count=0
    correct=0
    almostcorrect=0
    wrong=0
    list1=[]
    
    #start writing your code here
    for k,v in word_dict.items():
        if len(k)==len(v):
            for i in range(len(k)+1):
                if k[i]!=v[i]:
                    count=count+1
    if count==0:
        correct=correct+1
    
    elif count>=2:
        correct=correct+1
        
    else:
         wrong= wrong+1
    list1.append(correct)
    list1.append(almostcorrect)
    list1.append(wrong)
        
            

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
