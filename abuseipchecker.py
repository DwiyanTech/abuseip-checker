
# This script by Ahmad Dwiyan
#
# Any Risk take your own
#
# GNU Public License


import requests, random
from argparse import ArgumentParser


class IpAbuseCheck:
	def __init__(self):
		print("[*] Abuse IP Checker By dwiyantech  [*]")
		print("[*] IP Checker Massive Or Single IP [*]")
		print("[*]       Abuse IP Checker V1.0     [*]\n")


		parser = ArgumentParser()
		parser.add_argument("-l","--list",required=False,help="your path of list ip")
		parser.add_argument("-i","--ip",required=False,help="single ip you wanna check")
		args_parse = parser.parse_args()

		if args_parse.list is None and args_parse.ip is None:
			print("[*] Run -h to see all possible commands\n")
			exit(0)
			
		if args_parse.list is not None:
			print("[*] Abuse IP Check Script Is Running\n")
			word = [word.strip() for word in open(args_parse.list,'r').readlines()]
			for w in word:
				if self.checkAbuseIPDB(w):
					print("[*]{} => Blacklisted in AbuseIPDB".format(w))

				else:
					print("[*]{} => Not Blacklisted in AbuseIPDB".format(w))

				if self.checkIpVoid(w):
					print("[*]{} => Blacklisted in IPVoid".format(w))

				else:
					print("[*]{} => Not Blacklisted in IPVoid".format(w))
		else:
			if self.checkAbuseIPDB(args_parse.ip):
				print("[*]{} => Blacklisted in AbuseIPDB".format(args_parse.ip))

			else:
				print("[*]{} => Not Blacklisted in AbuseIPDB".format(args_parse.ip))

			if self.checkIpVoid(args_parse.ip):
				print("[*]{} => Blacklisted in IPVoid".format(args_parse.ip))

			else:
				print("[*]{} => Not Blacklisted in IPVoid".format(args_parse.ip))




	def useragents(self):
		user_agents = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3","Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
		return {"User-Agent":user_agents[random.randint(0,len(user_agents)-1)]}

	def checkAbuseIPDB(self,ip):
		try:

			abuseipdb_site = "https://www.abuseipdb.com/check/"+str(ip)
			word_notdetected = "was not found in our database"
			send_request = requests.get(abuseipdb_site,headers=self.useragents())

			if word_notdetected in send_request.text:
				return False
			else:
				return True

		except requests.exceptions.RequestException as e:

			return False


	def checkIpVoid(self,ip):
		try:

			ipvoid_site = "https://www.ipvoid.com/ip-blacklist-check/"
			data = {"ip":ip}
			word_detected = "BLACKLISTED"
			send_request = requests.post(ipvoid_site,data=data,headers=self.useragents())

			if word_detected in send_request.text:
				return True

			else:
				return False
		except requests.exceptions.RequestException as e:

			return False


if __name__ == '__main__':

	IpAbuseCheck()
