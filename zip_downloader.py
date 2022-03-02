import wget

year = [2020,2021]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

for y in year:
    for m in month:
        for d in day:
            url = "https://midcdmz.nrel.gov/tsi/SRRLASI/"+str(y)+"/"+str(y)+str(m)+str(d)+".zip"
            filename = wget.download(url)
