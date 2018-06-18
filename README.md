Stackme is a Web application or you can saycombination of them designed to retract data or desired questions directly from stackoverflow using BeautifulSoup which is a web scrappig or web Crawling tool and Django which is a Back-end web framework runs on python.

                                                     ###############

#What is django?

Django is a widely-used Python web application framework with a "batteries-included" philosophy. The principle behind batteries-included is that the common functionality for building web applications should come with the framework instead of as separate libraries.

                                                    ###############
                                                    
#What is Webscrapping?

Web Scraping (also termed Screen Scraping, Web Data Extraction, Web Harvesting etc.) is a technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file in your computer or to a database in table (spreadsheet) format.

Data displayed by most websites can only be viewed using a web browser. They do not offer the functionality to save a copy of this data for personal use. The only option then is to manually copy and paste the data - a very tedious job which can take many hours or sometimes days to complete. Web Scraping is the technique of automating this process, so that instead of manually copying the data from websites, the Web Scraping software will perform the same task within a fraction of the time.

                                                   ###############
  
#How to execute Stackme?

1. Open terminal using ctrl+alt+T in the same directory where manage.py file is saved or when can say that the home directory.
2. type: python manage.py runserver 8000   (port number is optional and by default is 8000).
3. Open the browser and write on the url: localhost:8000/p1/clk 

                                                   ###############

#Insight into the project.

The home page of this website has a search bar where you can search any questions which are related to stackexhange or stacoverflow in particular so what i did, i included a my webscrapping code in view file in the app where a dynamic web scrapping occurs which stores only the questions with only high number of votes or questions with approval right tick which is green in colour then the list of questions will be portrayed on a html page from where i've linked the page where only that specific answer will be shown.
