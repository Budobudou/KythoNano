import requests,json,io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# * Kythocore 1.0
def send(rawmsg,logid,logpass,kdict):
	msg = str(rawmsg)
	postd = f"message={msg}&id={logid}&password={logpass}&customize_url={kdict}"
	data2 = requests.post("https://kana.renorari.net/api/api.json", data=postd.encode("utf-8"))
	data3 = data2.text	
	data4 = json.loads(data3)
	if "timer" in data4["extension"].keys():		
		dataf = {"reaction": data4["reply"],"times": data4["extension"]["timer"]["start_message"],"timee": data4["extension"]["timer"]["end_message"],"time": data4["extension"]["timer"]["time"],}
		return dataf
	else:	
		dataf = {"reaction": data4["reply"],"times": "none","timee": "none","time": "none",}
		return dataf