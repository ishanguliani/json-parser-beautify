import json

def main():
	i = 0
	with open("business.json") as f:
		#for line in f.readline():
		print('inside open')
		line = f.readline()
		jsonloaded = json.loads(line)
		
		#	if i > 4:
		#		break;
		print(json.dumps(jsonloaded, indent=2))
		#break
		#i += 1
	pass

if __name__ == '__main__':
	main()
