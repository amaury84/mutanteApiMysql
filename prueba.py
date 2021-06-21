import requests, json

#url = "http://localhost:5000"
#r = requests.get(url)
#print(r) # esta api no retorna json usando get

dna = {
    "dna":["ATGCGA","CCGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    }
dna = json.dumps(dna) #transformar el dict a json
print(dna,type(dna))

url = "http://localhost:5000/mutant"
newurl = "https://ligamagneto-f4vojxibla-uc.a.run.app/mutant"
r = requests.post(newurl,data=dna)
print(r.json())

url = "http://localhost:5000/stats"
newurl = "https://ligamagneto-f4vojxibla-uc.a.run.app/mutant"
r = requests.post(url)
print(r.json())
