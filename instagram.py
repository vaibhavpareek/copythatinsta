from requests import get
from json import loads, dump
from re import compile
from os import system,path
import terminal_banner
import pyfiglet
import sys
from bs4 import BeautifulSoup
def banner():
	print("\033[1;34;48m* PYTHON BASED SCRIPT V1.0 \033[1;32;48mDeveloped By @Vaibhav Pareek\033[1;31;48m")
	print("\033[1;34;48m* It Crawls the Instagram \033[1;31;48m")
	ascii_banner = pyfiglet.figlet_format("Copythat@Insta",font="slant")
	print(ascii_banner)
	print("\033[1;35;48m")
def exit_banner():
	print(pyfiglet.figlet_format("Thanks for using CopyThatInsta",font="slant"))
try:
	while True:
		system("clear")
		banner()
		c = input("Press q to Exit or any Key to Continue : ").lower()
		if(c=='q' or c=='quit'):
			exit_banner()
			break
		link = input("Enter Username of Instagram : ")
		if(path.isdir('images')==False):
			system("mkdir images/")
		if(path.isdir('images/'+link)==False):
			system("mkdir images/"+link+"/")
		if(path.isfile('images/'+link+'details.txt')==False):
			system("touch images/"+link+"/details.txt")
		page = get("https://www.instagram.com/"+link+"/")
		soup = BeautifulSoup(page.text,'html.parser')
		print("\n")
		all_script = soup.find_all('script')
		json_data = loads(all_script[3].text)
		print("\033[1;32;48mName : \033[1;35;48m"+json_data['name']+"\n")
		print("\033[1;32;48mType : \033[1;35;48m"+json_data["@type"]+"\n")
		print("\033[1;32;48mInstagram Id :\033[1;35;48m "+json_data['mainEntityofPage']['@id']+"\n")
		script_tag = soup.find('script', text=compile('window\._sharedData'))
		shared_data = script_tag.string.partition('=')[-1].strip(' ;')
		json_value = loads(shared_data)
		with open("data.json", "w") as write_file:
			dump(json_value, write_file, indent=4)
		# sys.exit(0)
		print("\033[1;32;48mBiography :\033[10;35;48m "+ json_value['entry_data']['ProfilePage'][0]['graphql']['user']['biography']+"\n")
		if(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified']):
			print("\033[1;32;48mVerified :\033[10;35;48m Yes\n")
		else:
			print("\033[1;32;48mVerified :\033[10;35;48m No\n")
		print("\033[1;32;48mFollowers : \033[1;35;48m" + str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count'])+"\n")
		print("\033[1;32;48mFollowing : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count'])+"\n")
		if(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']==False):
			print("\033[1;32;48mAccount :\033[1;35;48m Public"+"\n")
		else:
			print("\033[1;32;48mAccount :\033[1;35;48m Private"+"\n")
		post = json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'];
		print("\033[1;32;48mPosts : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'])+"\n")
		print("\033[1;32;48mFacebook Page Attached : \033[1;35;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['connected_fb_page'])+"\n")
		system("curl '"+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url']+"' -o 'images/"+str(link)+"/profile.jpg'")
		print("\033[1;33;48mDownloaded Profile Pic saved in folder images"+"\n")
		n = 1
		fp = open("images/"+link+"/details.txt","w+")
		while(n<=post):
			print("\n\033[1;33;48mDownloading "+str(n)+" Post"+"\n")
			print("\033[1;32;48mCaption "+str(n)+ " : \033[1;34;48m"+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_media_to_caption']['edges'][0]['node']['text']+"\n")
			fp.write("Caption"+str(n)+ " : "+json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_media_to_caption']['edges'][0]['node']['text']+"\n")
			print("\033[1;32;48mLikes : \033[1;34;48m"+str(json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['edge_liked_by']['count'])+"\n")
			print("\033[1;35;48mDownloaded Post "+str(n));
			system("curl '"+ json_value['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][n-1]['node']['display_url']+"' --output 'images/"+str(link)+"/image"+str(n)+".jpg'")	
			n += 1
		fp.close()
		print("Done")
		input("Press Any Key to Continue ....")
except KeyboardInterrupt:
	print(pyfiglet.figlet_format("\nThanks for using CopyThatInsta",font="slant"))
except Exception as e:
	print(e)
	print(pyfiglet.figlet_format("\nThanks for using CopyThatInsta",font="slant"))
	
