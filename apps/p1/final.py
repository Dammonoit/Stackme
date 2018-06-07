import requests
from bs4 import BeautifulSoup

i=0
noOfVotes=[]
Question=[]
tempLink=[]
Link=[]
num=[]
temp=[]
dictionary={}
nextUrl="https://www.stackoverflow.com"

def main():
    
    # This is the main url
    url="https://stackoverflow.com/search?q="
    question=input("Enetr your question : ")
    url=url+question.replace(" ","+")
    response = requests.get(url)
    page=response.text

    vote_class, soup, intial_class = questions_page(page)
    votes(vote_class)
    links(soup)
    questions(soup)
    get_dict(intial_class)
    hit_link()
       
def questions_page(page):
    # Page 1 Beautiful Soup
    soup = BeautifulSoup(page,"lxml")
    intial_class=soup.findAll('div',{'class':'question-summary search-result'})
    vote_class=soup.findAll('span',{'class':'vote-count-post'})

    return vote_class,soup, intial_class

def votes(vote_class):

    for x in range(len(vote_class)):
        noOfVotes.append(int(vote_class[x].string))

def links(soup):

    #this is for link in Page 1
    for link in soup.findAll('a'):
	    if link.get('data-searchsession') and link.get('href'):
		    Link.append("https://www.stackoverflow.com"+link.get('href'))
		    
def questions(soup):

    #This is for Question related to link  
    for q in soup.findAll('a'):
	    if q.get('data-searchsession') and q.get('href'):
		    Question.append(q.get('title'))

def get_dict(intial_class):

    num=[i for i in range(1,(len(intial_class)+1))]
    #this is for getting number into question Ex. Q1
    for i in num:
	    temp.append("Q"+str(i))

    #this is for dictionary of link,question,vote
    for t,l,n,q in zip(temp,Link,noOfVotes,Question):
	    tempd={}
	    tempd.update({"Link":l,"vote":n,"question":q})
	    dictionary.update({t:tempd})

def hit_link():
    #this is for info we will receive after clicking the link of Page 1
    if len(Link)!=0:
	    l1=Link[1]
	    #print(l1)
	    final_vote=[]
	    top_vote=[]
	    temp={}
	    d={}
	    top_max_vote=[]
	    dictionary1={}
	    green=[]
	    ansNo=[]
	    noSolVote=[]
	    noSol=[]
	    nodict={}

	    #this is soup for page 2 content
	    content=requests.get(l1)
	    solutionPage=content.text
	    soup1=BeautifulSoup(solutionPage,"lxml")

	    #this is for question of Page 2 for which the answer is given
	    final_Question=soup1.findAll('div',{'class':'question'})

	    #This is for info if green tick answer is exist
	    solution=soup1.findAll('div',{'class':'answer accepted-answer'})

	    if solution:
		     #this is for the vote of the green tick solution
		    soup2=BeautifulSoup(str(solution),"lxml")
		    solutionVote=soup2.findAll('span',{'class':'vote-count-post'})
		    totalVote=int(solutionVote[0].string)
		    totalVote1=[totalVote]
		
		    #this is for the getting the answer without the green tick
		    soup1_1=BeautifulSoup(solutionPage,"lxml")
		    for div in soup1_1.findAll('div',{'class':'question'}):
			    div.decompose()
		    for div in soup1_1.findAll('div',{'class':'answer accepted-answer'}):
			    div.decompose()
		    other_answer=soup1_1.findAll('div',{'class':'answer'})
		
		    #This is for the vote of other answer 
		    top_ans=soup1_1.findAll('span',{'class':'vote-count-post'})
		    j=0
		    while j<len(top_ans):
			    top_vote.append(int(top_ans[j].string))
			    j+=1
		    top_max=max(top_vote)
		    top_max_vote.append(top_max)
		
		    #it write the questio and GreenTick Solution to the file which name is "final.html"  
		    with open("final.html",'w') as question:
			    question.write("<html><head><link rel=""stylesheet"" href=""test.css""></head><body>")
			    for div in final_Question:
				    print(div,file=question)
			    for div in solution:
				    print(div,file=question)
		

		    #This is for creating dictionary
		    question=list(final_Question)
		    gtick=list(solution)
		    temp.update({"greenTick":"true","vote":totalVote1,"ans":gtick})
		    other_answer1=list(other_answer)
		    temp2={"ans1":temp}

		    for i in range(2,len(top_vote)+2):
			    green.append("False")
			    ansNo.append("ans"+str(i))
		
		    for k,v,g,a in zip(other_answer,top_vote,green,ansNo):
			    temp1={}
			    temp1.update({"greenTick":g,"vote":v,"ans":k})
			    dictionary1.update({a:temp1})
		
		    for k in dictionary1:
			    if top_max_vote[0]==dictionary1[k]["vote"]:
				    div1=dictionary1[k]["ans"]
				    with open("final.html",'a') as question:
					    print(div1,file=question)
					    print("</body></html>",file=question)

	    #This is for info while there is no green tick answer
	    else:
		    #it's crate soup of page after the link is hit 
		    soup1_2=BeautifulSoup(solutionPage,"lxml")
		    for div in soup1_2.findAll('div',{'class':'question'}):
			    div.decompose()

		    #it is for getting the question which have no green tick soution 
		    noSolution=soup1.find('a',{'class':'question-hyperlink'})

		    #this is for the vote of answer 
		    noSolutionVote=soup1_2.findAll('span',{'class':'vote-count-post'})

		    #it's contain the answer
		    noSolutionAnswer=soup1_2.findAll('div',{'class':'answer'})

		    #it's for the getting the vote		
		    j=0
		    while j<len(noSolutionVote):
			    noSolVote.append(int(noSolutionVote[j].string))
			    j+=1

		    for i in range(0,len(top_vote)+1):
			    noSol.append("ans"+str(i))

		    #this is for creating dictionary
		    for noAns,noVote,a in zip(noSolutionAnswer,noSolVote,noSol):
			    temp1={}
			    temp1.update({"ans":noAns,"vote":noVote})	
			    nodict.update({a:temp1})
		    if len(noSolVote)!=0:
			    nomax=max(noSolVote)
			    for k in nodict:
				    if nomax==nodict[k]["vote"]:
					    div1=nodict[k]["ans"]
					    with open("final.html",'w') as question:
						    question.write("<html><head><link rel=""stylesheet"" href=""test.css""></head></html>")
						    for div in noSolution:
							    print(div,file=question)		
						    for div in final_Question:
							    print(div,file=question)
						    print(div1,file=question)
		    else:
			    print("Sorry There are no answer")
					
    else:
	    print("no result found")
