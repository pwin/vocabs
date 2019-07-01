import sys
sys.stdout = open('generalAgeBrackets.ttl', 'w', encoding='utf-8')

def generalRangeYears(x):
    for i in range(x):
        if (i >=0) and  (i <=9):
            coll = "sgtermsard:1"
            pl = "Up to first decade."
        elif  (i >=10) and  (i <=19):
            coll = "sgtermsard:2"
            pl = "Up to second decade"
        elif  (i >=20) and  (i <=29):
            coll = "sgtermsard:3"
            pl = "Up to third decade"            
        elif  (i >=30) and  (i <=39):
            coll = "sgtermsard:4"
            pl = "Up to fourth decade"
        elif  (i >=40) and  (i <=49):
            coll = "sgtermsard:5"
            pl = "Up to fifth decade"
        elif  (i >=50) and  (i <=59):
            coll = "sgtermsard:6"
            pl = "Up to sixth decade"
        elif  (i >=60) and  (i <=69):
            coll = "sgtermsard:7"
            pl = "Up to seventh decade"
        elif  (i >=70) and  (i <=79):
            coll = "sgtermsard:8"
            pl = "Up to eighth decade"
        elif  (i >=80) and  (i <=89):
            coll = "sgtermsard:9"
            pl = "Up to ninth decade"
        elif  (i >=90) and  (i <=99):
            coll = "sgtermsard:10"
            pl = "Up to tenth decade"
        elif  (i >=100) and  (i <=109):
            coll = "sgtermsard:11"
            pl = "Up to eleventh decade"
        elif  (i >=110) and  (i <=119):
            coll = "sgtermsard:12"
            pl = "Up to twelvth decade"
        elif  (i >=120) and  (i <=129):
            coll = "sgtermsard:13"
            pl = "Up to thirteenth decade"
            
        print(coll + " a skos:Collection ; skos:prefLabel \"" + pl + "\"@en ; .")
            
        for j in range(i):
            if i-1 == j:
                print("sgtermsary:" + str(j) + " ")
                print(" a skos:Concept ; ")
                print("skos:notation \"" + str(j) + "\"" + " ;")
                if j == 1:
                    print("skos:prefLabel \"" + str(j) + " year.\" ; . ")
                else:
                    print("skos:prefLabel \"" + str(j) + " years.\"@en ; . ")

                print(coll + " skos:member sgtermsary:" + str(j) + " ; .")
                

            else:
                print("sgtermsary:" + str(j) + "-" + str(i-1) + " ")
                print(" a skos:Concept ; ")
                print("skos:notation \"" + str(j) + "-" + str(i-1) + "\"" + " ;")
                print("skos:prefLabel \"" + str(j) + " to " + str(i-1) + " years.\"@en ; . ")
                print(coll + " skos:member sgtermsary:" + str(j)+"-"+str(i-1) + " ; .")


def generalRangeMonths(x):
    coll = "sgtermsarem:18"
    print(coll + " a skos:Collection ;  skos:prefLabel \"Early months\"@en  ;.")
    for i in range(x):
        for j in range(i):
            if i-1 == j:
                print("sgtermsarm:" + str(j) + " ")
                print(" a skos:Concept ; ")
                print("skos:notation \"" + str(j) + "\"" + " ;")
                if j == 1:
                    print("skos:prefLabel \"" + str(j) + " month.\" ; . ")
                else:
                    print("skos:prefLabel \"" + str(j) + " months.\" ; . ")
                print(coll + " skos:member sgtermsarm:" + str(j) + " ; .")
                

            else:
                print("sgtermsarm:" + str(j) + "-" + str(i-1) + " ")
                print(" a skos:Concept ; ")
                print("skos:notation \"" + str(j)+"-"+str(i-1) + "\"" + " ;")
                print("skos:prefLabel \"" + str(j)+" to " +str(i-1) + " months.\" ; . ")
                print(coll + " skos:member sgtermsarm:" + str(j)+"-"+str(i-1) + " ; .")
              


if __name__ == "__main__":
    print("@prefix sgtermsarm: <http://terms.gov.scot/agerange/months/>.")
    print("@prefix sgtermsary: <http://terms.gov.scot/agerange/years/>.")
    print("@prefix sgtermsard: <http://terms.gov.scot/agerange/decades/>.")
    print("@prefix sgtermsarem: <http://terms.gov.scot/agerange/earlymonths/>.")
    print("@prefix skos: <http://www.w3.org/2004/02/skos/core#>.")
    generalRangeMonths(20)
    generalRangeYears(122)
    print("####")
    sys.stdout.flush()
