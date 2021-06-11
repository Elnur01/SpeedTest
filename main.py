import speedtest

test = speedtest.Speedtest()

print('Server List...')
#--> get list of servers
test.get_servers() 
print('Choosing Best Server...')
#--> choose best server
best = test.get_best_server() 

print(test)

print('Calculating Download Speed...')
download_speed = test.download()
print('Calculating Upload Speed...')
uploadload_speed = test.upload()

print('Calculating Ping...')
ping = test.results.ping

print(f"Your Download Speed is: {download_speed /1024 /1024  : .2f} Mbit/s \n Your Upload Speed is: {uploadload_speed /1024 /1024 : .2f} Mbit/s \n Your ping is: {ping : .2f} ms")