import sys
import json
from time import sleep
from random import randint

sys.path.insert(1, "Assets/")
from Base import Instagram_Bot

json_file = open('Assets/Manifest.json', encoding="utf8")
json_data = json.load(json_file)


"""
from datetime import datetime


running = True

while running:

    # Potential issue with this is that that it only does the first bots, and skips the last few... 
    # this will only happn if there are a fucking shit ton of bots, but to fix this make 2 loops, the first one adds bot objects to a list, and the second runs them...
    # I think this might be an issue at least...

    for i in json_data["Bot_Manifest"]:
        
        now = datetime.now()
        current_time = now.strftime("%H:%M %d/%m/%Y")
        last_post = datetime.strptime(i["last_post"], "%H:%M %d/%m/%Y")
        
        if (last_post + i["post_time_delta"]) <= current_time:
            return 0

            
            now = datetime.now()
            current_time = now.strftime("%H:%M %d/%m/%Y")
            
            i["last_post"] = current_time
            a_file = open("Assets/Manifest.json", "w")
            json.dump(json_data, a_file)
            a_file.close()

            
# Work on timing issue...
# Try multiple bots at once...
# Upload to Raspberry Pi
# Work around Instagram Post... https://business.facebook.com/creatorstudio/instagram_content_posts
# Work around Instagram Post... To make it headless, and maybe even get it to post multiple

"""




for i in json_data["Bot_Manifest"]:
    Name = Instagram_Bot(i["username"], i["password"], i["headless"])
    Name.Start()
    Name.Login()
    #Name.Download_Post_By_User(i["compeers"][randint(0,(len(i["compeers"]))-1)], all = False, index = randint(0, 4))
    Name.Download_Post_By_User_Temporary(i["compeers"][randint(0,(len(i["compeers"]))-1)], all = False, index = randint(0, 4), only_photo = True)

    ### Setup Upload

    # Caption
    caption = i["captions"][randint(0,(len(i["captions"]))-1)]
    
    # Tags
    tag_1 = randint(0,(len(i["tags"])-1))
    passed = False
    while passed == False:
        try:
            tag_2 = tag_1 + 5
            try_str = i["tags"][tag_2]
            passed = True
        except:
            tag_1 -= 1
    tags = i["tags"][tag_1:tag_2]

    # Location
    location = i["locations"][randint(0,(len(i["locations"]))-1)]

    # Tagged People
    tagged_1 = randint(0,(len(i["tagged_people"])-1))
    passed = False
    while passed == False:
        try:
            tagged_2 = tagged_1 + 1
            try_str = i["tagged_people"][tagged_2]
            passed = True
        except:
            tagged_1 -= 1
    tagged_people = i["tagged_people"][tagged_1:tagged_2]

    # Comment
    comment = i["comments"][randint(0,(len(i["comments"]))-1)]

    Name.Upload_Post(caption, tags, location, tagged_people = False, comment = comment, like = True)



# Search option error
# Video issue
# Creator Studio