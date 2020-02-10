import commands.base_command
import requests 
from bs4 import BeautifulSoup 
from utils                  import get_emoji

class OPGGLIVE(commands.base_command.BaseCommand):

    def __init__(self):
        description = "Displays OPGG info of current enemy team (use underscore instead of spaces)"
        params = ["nickname"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            nick = str(params[0])
            nick.replace('_','+')
        except ValueError:
            await message.channel.send("Please, provide valid numbers")
            return

        url='https://eune.op.gg/summoner/spectator/userName='+ nick + '&'

        resp=requests.get(url) 

        #Friendly
        if resp.status_code==200: 
            print("Successfully opened the web page")  
            soup=BeautifulSoup(resp.text,'html.parser')     

            l=soup.find("table",{"class":"Table Team-100"}) 

            FriendNames = []
            TierF = []
            Wrf = []

            for i in l.findAll("a",{"class":"SummonerName"}): 
                FriendNames.append(i.text)

            for i in l.findAll("div",{"class":"TierRank"}): 
                TierF.append(i.text)

            for i in l.findAll("td",{"class":"RankedWinRatio Cell"}): 
                Wrf.append(i.text)

            l=soup.find("table",{"class":"Table Team-200"})

            EnemyNames = []
            TierE = []
            Wre = []

            for i in l.findAll("a",{"class":"SummonerName"}): 
                EnemyNames.append(i.text)

            for i in l.findAll("div",{"class":"TierRank"}): 
                TierE.append(i.text)
            
            for i in l.findAll("td",{"class":"RankedWinRatio Cell"}): 
                Wre.append(i.text)

            l=soup.find("div",{"class":"Box"})

            GameMode=[]
            MapName=""
            Current=""

            for i in l.findAll("div",{"class":"Title"}): 
                GameMode.append(i.text)

            for i in l.findAll("small",{"class":"MapName"}): 
                MapName=i.text
            
            for i in l.findAll("small",{"class":"Time"}): 
                Current=i.text
            
            Time=Current[len(Current)-8:len(Current)-3]

            if(Time[0:1]=="0"):
                Time=Time[1:len(Time)]
            
            TMP1=Time.replace(":" , ".")

            TMP2= float(TMP1)
            TMP2+=16
            TMP3=str(TMP2)
            TimeEUNE=TMP3.replace("." , ":")

        else: 
            print("Error")
            await message.channel.send(message.author.mention + "\n"+"**Player is currently not in game.**")

        await message.channel.send("**Gamemode: **"+GameMode[0][0:13]+"\t** Map: **"+MapName+"\t**Time: **"+TimeEUNE+"\n"
            +get_emoji(":small_blue_diamond:")+f"** "+FriendNames[0]+"**\t"+get_emoji(":military_medal:")+f"** Rank: **"+TierF[0].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wrf[0][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+"** Played Matches: **"+Wrf[0][9:15].strip()+"\n"
            +get_emoji(":small_blue_diamond:")+f"** "+FriendNames[1]+"**\t"+get_emoji(":military_medal:")+f"** Rank: **"+TierF[1].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wrf[1][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wrf[1][9:15].strip()+"\n"
            +get_emoji(":small_blue_diamond:")+f"** "+FriendNames[2]+"**\t"+get_emoji(":military_medal:")+f"** Rank: **"+TierF[2].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wrf[2][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wrf[2][9:15].strip()+"\n"
            +get_emoji(":small_blue_diamond:")+f"** "+FriendNames[3]+"**\t"+get_emoji(":military_medal:")+f"** Rank: **"+TierF[3].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wrf[3][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wrf[3][9:15].strip()+"\n"
            +get_emoji(":small_blue_diamond:")+f"** "+FriendNames[4]+"**\t"+get_emoji(":military_medal:")+f"** Rank: **"+TierF[4].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wrf[4][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wrf[4][9:15].strip()+"\n"
            +get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+get_emoji(":heavy_minus_sign:")+"\n"
            +get_emoji(":small_orange_diamond:")+f" **"+EnemyNames[0]+"**\t"+get_emoji(":military_medal:")+f" **Rank: **"+TierE[0].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wre[0][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wre[0][9:15].strip()+"\n"
            +get_emoji(":small_orange_diamond:")+f" **"+EnemyNames[1]+"**\t"+get_emoji(":military_medal:")+f" **Rank: **"+TierE[1].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wre[1][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wre[1][9:15].strip()+"\n"
            +get_emoji(":small_orange_diamond:")+f" **"+EnemyNames[2]+"**\t"+get_emoji(":military_medal:")+f" **Rank: **"+TierE[2].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wre[2][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wre[2][9:15].strip()+"\n"
            +get_emoji(":small_orange_diamond:")+f" **"+EnemyNames[3]+"**\t"+get_emoji(":military_medal:")+f" **Rank: **"+TierE[3].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wre[3][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wre[3][9:15].strip()+"\n"
            +get_emoji(":small_orange_diamond:")+f" **"+EnemyNames[4]+"**\t"+get_emoji(":military_medal:")+f" **Rank: **"+TierE[4].lstrip().rstrip()+"\t"+get_emoji(":trophy:")+f" **WinRate: **"+Wre[4][0:8].lstrip().rstrip()+"\t"+get_emoji(":hourglass:")+f"** Played Matches: **"+Wre[4][9:15].strip()+"\n"
        )