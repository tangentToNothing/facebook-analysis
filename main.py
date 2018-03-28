from lxml import html
import glob
import requests

def main():
	print("Beginning analysis")
	with open('data/index.htm', 'r') as f:
		page_text = f.read()
		index_tree = html.fromstring(page_text)
		name = index_tree.xpath('//h1/text()')
		headers = index_tree.xpath('//table//th/text()')
		values = index_tree.xpath('//table//td/text()')
		print("*************************************")
		print("* Hi, {}".format(name[0]))
		print("*************************************")
		print("\n")

		conversations = glob.glob('data/messages/*.html')
		print("I've found {} conversations! Let's take a look.".format(len(conversations)))
		print("\n")

		messages_list = []

		for conversation in conversations[:1]:
			with open(conversation, 'r') as f:

				page = f.read()
				x_tree = html.fromstring(page)
				convo_users_full = x_tree.xpath('//div[@class="thread"]//div[@class="message"]')

				for message in convo_users_full:
					print(message)
					user = message.xpath('//div[@class="message_header"]//span[@class="user"]/text()')
					print(user)
					if user == name:
						text_of_message = message.xpath('//p/text()')
						print("Your said: {}".format(text_of_message))


		#print(headers)
		#print(values)

if __name__ == '__main__':
	main()