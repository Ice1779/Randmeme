import requests
global mainurl
mainurl="https://meme-api.herokuapp.com/gimme"
class Gimme_Instance:
    def __init__(self,subreddit='',warnings=True): #generates api instance and gets data into variables
        if warnings:
            if subreddit!='':
                print("We observe that you are not using the default subreddits. This might result in the retrieval of a reddit post instead of a meme depending on the subreddit.\n")
        try:
            r=requests.get(mainurl+'/'+str(subreddit))
            if r.status_code==200:
                data=r.json()
                self.postlink=str(data['postLink'])
                self.subreddit=str(data['subreddit'])
                self.title=str(data['title'])
                self.img_url=str(data['url'])

        except:
            print("Invalid subreddit")


