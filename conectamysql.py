import pymysql.cursors
import json

def conectadb():    
    # Connect to the database
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='ligamagneto',
                         cursorclass=pymysql.cursors.DictCursor)

    # prepare a cursor object using cursor() method
    return db,db.cursor()
    
def insertadb(adn,condicion):
    db,cursor = conectadb()
    try:
        sql = 'INSERT INTO usuarios (adn, mutante) VALUES (%s, %s)'
        cursor.execute(sql, (adn, condicion))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        db.commit()
    except pymysql.err.IntegrityError:
        print("la cadena adn ya fue verificada")
    # desconecta del servidor
    db.close()
    
def consultadb():
    db,cursor = conectadb()
    count_human_dna=0
    count_mutant_dna=0
    ratio=0
    datajson={}
    sql = 'SELECT adn, mutante FROM usuarios'
    cursor.execute(sql,)
    result = cursor.fetchall()

    for r in result:
        adn = r["adn"]
        mutante = r["mutante"]
        if mutante:
            count_mutant_dna += 1
        else:
            count_human_dna +=1
        print ("adn = {}, mutante = {}".format(adn,mutante))
        
    ratio = count_mutant_dna/len(result)

    datajson["count_mutant_dna"]=count_mutant_dna
    datajson["count_human_dna"]=count_human_dna
    datajson["ratio"]=round(ratio,2)
    print(json.dumps(datajson))
    # desconecta del servidor
    db.close()
    return json.dumps(datajson)
if __name__=="__main__":
    
    #insertadb()
    consultadb()
        
