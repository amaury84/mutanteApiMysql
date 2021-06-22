import requests, json

#url = "http://localhost:5000"
#r = requests.get(url)
#print(r) # esta api no retorna json usando get

dna = {
    "dna":["ATGCGA","CCGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    }
dna = json.dumps(dna) #transformar el dict a json
#print(dna,type(dna))

urllocal = "http://localhost:5000/mutant"
urlcloud = "https://ligamagneto-f4vojxibla-uc.a.run.app/mutant"
r = requests.post(urllocal ,data=dna)
print(r.json())

#servicio stats
urllocal = "http://localhost:5000/stats"
r = requests.post(urllocal)
print(r.json())

