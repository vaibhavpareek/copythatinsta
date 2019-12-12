import requests
import json
import re
import os
import terminal_banner
import pyfiglet
from bs4 import BeautifulSoup
print("\033[1;34;48m* PYTHON BASED SCRIPT V1.0 \033[1;32;48mDeveloped By @Vaibhav Pareek\033[1;31;48m")
print("\033[1;34;48m* It Crawls the Instagram \033[1;31;48m")
ascii_banner = pyfiglet.figlet_format("Copythat@Insta",font="slant")
print(ascii_banner)
print("\033[1;35;48m")
#try:
link = input("Enter Username of Instagram : ")
page = requests.get("https://www.instagram.com/"+link+"/")
soup = BeautifulSoup(page.text,'html.parser')
print("\n")
#print(soup.prettify())
all_script = soup.find_all('script')
#print(all_script)
json_data = json.loads(all_script[3].text)
#print(json_data)
print("\033[1;32;48mName : \033[1;35;48m"+json_data['name']+"\n")
print("\033[1;32;48mType : \033[1;35;48m"+json_data["@type"]+"\n")
print("\033[1;32;48mInstagram Id :\033[1;35;48m "+json_data['mainEntityofPage']['@id']+"\n")
#print(all_script[4])
#ele = all_script[4].attrs("window._sharedData")
#json_value = json.loads(ele)
#print(json_value)
#print(json_value['entry_data']['ProfilePage'])
script_tag = soup.find('script', text=re.compile('window\._sharedData'))
shared_data = script_tag.string.partition('=')[-1].strip(' ;')
json_value = json.loads(shared_data)
print("\033[1;32;48mBiography :\033[10;35;48m "+ json_value['entry_data']['ProfilePage'][0]['graphql']['user']['biography']+"\n")
if(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified']):
	print("\033[1;32;48mVerified :\033[10;35;48m Yes\n")
else:
	print("\033[1;32;48mVerified :\033[10;35;48m No\n")
#print(json_value['entry_data']['ProfilePage'][0])
print("\033[1;32;48mFollowers : \033[1;35;48m" + str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count'])+"\n")
#print("Followers : "+json_value['entry_data']['ProfilePage']['user']['edge_followed_by'])
print("\033[1;32;48mFollowing : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count'])+"\n")
if(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']==False):
	print("\033[1;32;48mAccount :\033[1;35;48m Public"+"\n")
else:
	print("\033[1;32;48mAccount :\033[1;35;48m Private"+"\n")
post = json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'];
print("\033[1;32;48mPosts : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'])+"\n")
print("\033[1;32;48mFacebook Page Attached : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['connected_fb_page'])+"\n")
os.system("curl '"+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url']+"' -o 'images/profile.jpg'")
print("\033[1;33;48mDownloaded Profile Pic saved in folder images"+"\n")
n = 1
fp = open("images/details.txt","w+")
while(n<=post):
	print("\n\033[1;33;48mDownloading "+str(n)+" Post"+"\n")
	print("\033[1;32;48mCaption "+str(n)+ " : \033[1;34;48m"+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_media_to_caption']['edges'][0]['node']['text']+"\n")
	fp.write("Caption"+str(n)+ " : "+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_media_to_caption']['edges'][0]['node']['text']+"\n")
	print("\033[1;32;48mLikes : \033[1;34;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_liked_by']['count'])+"\n")
	#print(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][0])
	print("\033[1;35;48mDownloaded Post "+str(n));
	os.system("curl '"+ json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['display_url']+"' --output 'images/image"+str(n)+".jpg'")	
	n += 1
fp.close()
#print(res)
print("DOne")
#print(all_script[3])
#fp = open("inst.txt","w")
#fp.write(soup)	
#fp.close()