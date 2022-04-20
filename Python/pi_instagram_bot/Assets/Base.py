class Instagrambot_Bot:
    Bot_List = []
    bot_number = 0
    def __init__(self, username, password, headless):
        Instagram_Bot.Bot_List.append(self)
        Instagram_Bot.bot_number += 1
        self.bot_number = Instagram_Bot.bot_number
        self.username = username
        self.password = password

        while headless != "True" and headless != "False":
            headless = input("Error: The headless attribute must be: 'True' or 'False'.\nWhat do you want this value to be?: ")
        
        self.headless = bool(headless)
        self.logged = False
    
    def Info(self):
        unclear_password = self.password[0:3]
        for i in range(0, len(self.password)-3):
            unclear_password = unclear_password + "#"
        
        print("Instagram Bot Object Name: " + self.username)
        print("Password: " + unclear_password)
        print("Headless: " + str(self.headless))
        print("Bot Number: " + str(self.bot_number))
    
    def Start(self):
        unclear_password = self.password[0:3]
        for i in range(0, len(self.password)-3):
            unclear_password = unclear_password + "#"
        print("")
        print("  _____           _                                    ____        _   ")
        print(" |_   _|         | |                                  |  _ \      | |  ")
        print("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ")
        print("   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|")
        print("  _| |_| | | \__ \ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ ")
        print(" |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|")
        print("                            __/ |                                      ")
        print("                           |___/                                       ")
        print("# Current Bot ==================================================================")
        print("# Instagram Bot Object Name: " + self.username)
        print("# Password: " + unclear_password)
        print("# Headless: " + str(self.headless))
        print("# Bot Number: " + str(self.bot_number))
        print("# ==============================================================================")
        print("# author       :Reed Graff")
        print("# website      :TheReedGraff.com")
        print("# linkedin     :https://www.linkedin.com/in/ReedGraff")
        print("# github       :https://github.com/ReedGraff")
        print("# email        :RangerGraff@gmail.com")
        print("# version      :1.0")
        print("# ==============================================================================")
        print("")
        
        """
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        """
        ###
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        ###
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #driver.maximize_window()
        self.driver = driver
        driver.get("https://www.instagram.com/")
        sleep(2)

    def Instagram_Wait(self, path = "//*[@id=\"react-root\"]/section/footer/div/div[2]/div[2]/div"):
        driver = self.driver
        loaded = False
        try_time = 0
        while loaded == False and try_time < 5:
            try:
                element_present = EC.presence_of_element_located((By.XPATH, path))
                WebDriverWait(driver, 5).until(element_present)
                sleep(randint(3, 5))
                loaded = True
            except:
                try_time += 1
    
    def Login(self):
        driver = self.driver
        
        for i in Instagram_Bot.Bot_List:
            if i.logged == True:
                print("Error: Other account is logged in. The logged account is: " + i.username + ". Try using " + i.username + ".Logout()")
                return
        print("LOG: Logging into " + self.username)
        self.logged = True
        self.Instagram_Wait("//input[@name=\"username\"]")
        driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.Instagram_Wait("//input[@name=\"password\"]")
        driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.Instagram_Wait()
        driver.find_element_by_xpath("//button[@type='submit']").click()

        try:
            self.Instagram_Wait("//*[@id=\"react-root\"]/section/main/div/div/div/div/button")
            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button").click()
        except:
            pass
            
        try:
            self.Instagram_Wait("/html/body/div[5]/div/div/div/div[3]/button[2]")
            driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        except:
            pass
            
        try:
            self.Instagram_Wait("/html/body/div[6]/div/div/div/div[3]/button[2]")
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()
        except:
            pass

    ### Download Posts
    
    def Download_Self_Post(self, index):
        return 0
    
    def Download_Post_By_User(self, user, all = True, index = 0):
        driver = self.driver
        #Procedurally make list of posts... to avoid the 1mill+ post accounts        
        print("LOG: Downloading Post By User: " + user)
        self.Instagram_Wait("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/input")
        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/input").send_keys(user)
        self.Instagram_Wait("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").click()
        self.Instagram_Wait("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[1]/span/span")
        number_of_posts = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[1]/span/span").get_attribute("innerHTML")
        number_of_posts = number_of_posts.replace(",", "")

        if index > (int(number_of_posts)-1):
            print("Error: Index is out of range")
            return


        posts = []
        while len(posts) <= index:
            try:
                raw_elems = driver.find_elements_by_xpath("//a[@href]")
                for i in raw_elems:
                    if "https://www.instagram.com/p/" in i.get_attribute("href"):
                        posts.append(i.get_attribute("href"))
            
            except: # Post has not loaded yet
                posts = []
                y_cord += 1080
                driver.execute_script("window.scrollTo(0, " + str(y_cord) + ")") 
            
        driver.get(posts[index])

        ### Now on page with all photos / videos
        page = str(driver.current_url + "?__a=1")
        driver.get(page)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        json_data = soup.find('pre').text
        json_data = json.loads(json_data)


        if all:
            try: # Nested 
                json_data = json_data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]

                for i in json_data:
                    if i["node"]["is_video"]:
                        # Find existing files in content folder
                        files = list(os.listdir("Assets/content"))
                        
                        num = len(files)
                        local_path = str("Assets/content/" + str(num) + "_file.mp4")

                        external_path = i["node"]["video_url"]

                        urllib.request.urlretrieve(external_path, local_path) 

                    else:
                        files = list(os.listdir("Assets/content"))
                        
                        num = len(files)
                        local_path = str("Assets/content/" + str(num) + "_file.jpg")

                        external_path = i["node"]["display_url"]

                        urllib.request.urlretrieve(external_path, local_path) 
            except:
                pass

            try: # Single Video
                external_path = json_data["graphql"]["shortcode_media"]["video_url"]

                files = list(os.listdir("Assets/content"))
                
                num = len(files)
                local_path = str("Assets/content/" + str(num) + "_file.mp4")

                urllib.request.urlretrieve(external_path, local_path) 
            except:
                try: # Single Photo
                    external_path = json_data["graphql"]["shortcode_media"]["display_url"]

                    files = list(os.listdir("Assets/content"))
                    
                    num = len(files)
                    local_path = str("Assets/content/" + str(num) + "_file.jpg")

                    urllib.request.urlretrieve(external_path, local_path) 
                except:
                    pass

        else:
            try: # Nested 
                json_data = json_data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"]

                try_num = 0
                for i in json_data:
                    # The and makes it do that this only runs once...
                    if try_num == 0:
                        if i["node"]["is_video"]:
                            # Find existing files in content folder
                            files = list(os.listdir("Assets/content"))
                            
                            num = len(files)
                            local_path = str("Assets/content/" + str(num) + "_file.mp4")

                            external_path = i["node"]["video_url"]

                            urllib.request.urlretrieve(external_path, local_path) 

                            try_num += 1

                        else:
                            files = list(os.listdir("Assets/content"))
                            
                            num = len(files)
                            local_path = str("Assets/content/" + str(num) + "_file.jpg")

                            external_path = i["node"]["display_url"]

                            urllib.request.urlretrieve(external_path, local_path) 

                            try_num += 1
                    else:
                        pass
            except:
                pass

            try: # Single Video
                external_path = json_data["graphql"]["shortcode_media"]["video_url"]

                files = list(os.listdir("Assets/content"))
                
                num = len(files)
                local_path = str("Assets/content/" + str(num) + "_file.mp4")

                urllib.request.urlretrieve(external_path, local_path) 
            except:
                try: # Single Photo
                    external_path = json_data["graphql"]["shortcode_media"]["display_url"]

                    files = list(os.listdir("Assets/content"))
                    
                    num = len(files)
                    local_path = str("Assets/content/" + str(num) + "_file.jpg")

                    urllib.request.urlretrieve(external_path, local_path) 
                except:
                    pass

        
        driver.get("https://www.instagram.com/")
        
        print("LOG: Done Downloading Post By User: " + user)


    def Download_Post_By_Link(self, link):
        return 0
    
    def Download_Self_Post_With_Verification(self, index): # Makes sure that post isn't a plug / promo or something...
        return 0
    
    def Download_Post_By_User_With_Verification(self, user): # Makes sure that post isn't a plug / promo or something...
        #Procedurally make list of posts... to avoid the 1mill+ post accounts
        return 0

    def Download_Post_By_Link_With_Verification(self, link): # Makes sure that post isn't a plug / promo or something...
        return 0

    ### Return Info on a post

    def Return_Most_Recent_Post_Likes_By_User(self, user):
        return 0

    def Return_Most_Recent_Post_Type_By_User(self, user):
        return 0

    def Return_Most_Recent_Post_Caption_By_User(self, user):
        return 0

    def Return_Most_Recent_Post_Likes_By_Self(self, index):
        return 0

    def Return_Most_Recent_Post_Type_By_Self(self, index):
        return 0

    def Return_Most_Recent_Post_Caption_By_Self(self, index):
        return 0

    def Return_Post_Date_By_Self(self, index):
        return 0

    def Return_Post_Likes_By_Link(self, link):
        return 0

    def Return_Post_Type_By_Link(self, link):
        return 0

    def Return_Post_Caption_By_Link(self, link):
        return 0

    def Return_Post_Date_By_Link(self, link, index):
        return 0


    ### Return Info on an account

    def Return_Account_Post_Number_By_Name(self, name):
        return 0
        
    def Return_Account_Post_Number_By_Link(self, link):
        return 0

    def Return_Account_Post_Number_By_Self(self):
        return 0

    def Return_Account_Follower_Number_By_Name(self, name):
        return 0
        
    def Return_Account_Follower_Number_By_Link(self, link):
        return 0

    def Return_Account_Follower_Number_By_Self(self):
        return 0

    def Return_Account_Following_Number_By_Name(self, name):
        return 0
        
    def Return_Account_Following_Number_By_Link(self, link):
        return 0

    def Return_Account_Following_Number_By_Self(self):
        return 0
    
    ### Internal(on instagram) Find Content If You Don't Have Compeers

    def Internal_Find_Post_By_Place(self, bestof, place):
        return 0

    def Internal_Find_Post_By_Tag(self, bestof, tag):
        return 0

    def Internal_Find_Post_By_Audio(self, bestof, audio):
        return 0

    def Internal_Find_Post_By_Topic(self, bestof, topic):
        return 0

    ### External(Scraped From Other Websites) Find Content

    def External_Google_Find_Photo_By_Topic(self, bestof, topic):
        return 0

    def External_Reddit_Find_Photo_By_SubReddit(self, bestof, sub_reddit):
        return 0

    def External_Reddit_Find_Photo_By_Topic(self, bestof, sub_reddit):
        return 0

    ### Comment

    def Comment_Most_Recent_Post_By_Self(self):
        return 0

    def Comment_Most_Recent_Post_By_User(self):
        return 0

    def Comment_Post_By_Link(self):
        return 0

    def Comment_All_Posts_By_User(self):
        return 0
    
    ### Advanced Comment (With Machine Learning)

    def Comment_Most_Recent_Post_By_Self(self):
        return 0

    def Comment_Most_Recent_Post_By_User(self):
        return 0

    def Comment_Post_By_Link(self):
        return 0

    def Comment_All_Posts_By_User(self):
        return 0

    ### Like

    def Like_Most_Recent_Post_By_Self(self):
        return 0

    def Like_Most_Recent_Post_By_User(self):
        return 0

    def Like_Post_By_Link(self):
        return 0

    def Like_All_Posts_By_User(self):
        return 0

    ### Upload

    def Upload_Post(self, caption, tags, location, tagged_people = False, comment = False, like = True):
        driver = self.driver

        print("LOG: Uploading Post With The Account " + self.username)

        files = list(os.listdir("Assets/content"))
        num = len(files)
        
        internal_path = os.path.abspath(str("Assets/content/" + str(files[0])))


        print("LOG: Removing Content Files With The Account " + self.username)

        dir = 'Assets/content'
        for file in os.listdir(dir):
            os.remove(os.path.join(dir, file))
        
        print("LOG: Done Uploading Post With The Account " + self.username)


































from time import sleep

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    # open up camera app
    device.shell('input keyevent 84')
    sleep(2)
    device.shell('input text Instagram')
    sleep(2)

    # Open Instagram
    device.shell('input tap 135 990')
    sleep(2)
    # Begin Posting
    device.shell('input tap 145 410')
    sleep(2)
    # Begin Posting
    device.shell('input tap 360 2155')
    sleep(2)
    
    # Screen size is 1080 x 2340

    device.shell('input tap 905 1440')
    sleep(2)

    # Begin Posting
    #device.shell('input tap 135 1650')
    #sleep(2)
    device.shell('input tap 405 1650')
    sleep(2)
    device.shell('input tap 675 1650')
    sleep(2)
    device.shell('input tap 945 1650')
    sleep(2)