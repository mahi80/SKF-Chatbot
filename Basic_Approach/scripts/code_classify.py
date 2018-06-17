from rake_nltk import Rake
import nltk
def data():
    with open("datasets/code_title.txt") as title:
        title=title.readlines()
    return title

def phrase(ques):
    phrase=[]
    new_list=[]
    r=Rake()
    question=ques
    r.extract_keywords_from_text(question)
    phrase=r.get_ranked_phrases()
    for items in phrase:
        new_list.extend(items.lower().split())
    return new_list    

def lis(l):
    language_list=['flask', 'java', 'go', 'ruby', 'django', 'asp', 'php']
    new_l=l
    ans=[]
    title=data()
    for l in new_l:
        l=l.lower().strip("\n")
        if l in language_list:
             code_lang=l
             new_l.remove(l)
        else:
             code_lang="NULL"
    for i in new_l:
        i=i.lower().strip("\n")
        for t in title:
            t=t.lower()
            if i in t:
                ans.append(t)

    return ans,code_lang

def entity(ques):
    
    count=0
    list_p=phrase(ques)
    ans,code_lang=lis(list_p)
    
    for i in ans:
        i=i.strip("\n").lower()
        if i in ques.lower():
            count=count+1
            ent=i
            
            break
    if count==1:
        return ent,code_lang
    else:
        if len(ans)==1:
           abc=ans[0]
           abc=abc.lower().strip("\n")
           return abc,code_lang
        else:
           #print("Select from these\n")
           #print(ans)
           return ans

    
        


#question=input("Enter question")
#print(entity(question))
