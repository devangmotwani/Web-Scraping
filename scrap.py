import urllib.request
from bs4 import BeautifulSoup
import json
import pprint

if __name__ == "__main__":
    states = {"ALABAMA": "AL",
    "ALASKA":	"AK",
    "ARIZONA":	"AZ",
    "ARKANSAS":	"AR",
    "CALIFORNIA":   "CA",
    "COLORADO":	"CO",
    "CONNECTICUT":"CT",
    "DELAWARE":	"DE",
    "FLORIDA":	"FL",
    "GEORGIA":	"GA",
    "HAWAII":	"HI",
    "IDAHO":	"ID",
    "ILLINOIS":	"IL",
    "INDIANA":	"IN",
    "IOWA":	"IA",
    "KANSAS":	"KS",
    "KENTUCKY":	"KY",
    "LOUISIANA":	"LA",
    "MAINE":	"ME",
    "MARYLAND":	"MD",
    "MASSACHUSETTS":	"MA",
    "MICHIGAN":	"MI",
    "MINNESOTA":	"MN",
    "MISSISSIPPI":	"MS",
    "MISSOURI":	"MO",
    "MONTANA":	"MT",
    "NEBRASKA":	"NE",
    "NEVADA":	"NV",
    "NEW HAMPSHIRE":	"NH",
    "NEW JERSEY"    :   "NJ",
    "NEW MEXICO"    :   "NM",
    "NEW YORK":	"NY",
    "NORTH CAROLINA":	"NC",
    "NORTH DAKOTA":	"ND",
    "OHIO":	"OH",
    "OKLAHOMA":	"OK",
    "OREGON":	"OR",
    "PENNSYLVANIA":	"PA",
    "RHODE ISLAND":	"RI",
    "SOUTH CAROLINA":	"SC",
    "SOUTH DAKOTA":	"SD",
    "TENNESSEE":	"TN",
    "TEXAS":	"TX",
    "UTAH"          :	"UT",
    "VERMONT"       :	"VT",
    "VIRGINIA"      :	"VA",
    "WASHINGTON"    :	"WA",
    "WEST VIRGINIA" :	"WV",
    "WISCONSIN"	    :   "WI",
    "WYOMING"       :   "WY",
    "GUAM"          :	"GU",
    "PUERTO RICO"   :   "PR",
    "VIRGIN ISLANDS":   "VI"}
    abr=list(states.values())
    abr.sort()
    print(abr)
    #for i in abr:
    webpage= str("http://gomashup.com/json.php?fds=geo/usa/zipcode/state/")+str(abr[0])+str("&jsoncallback=")
    print(webpage)
    page=urllib.request.urlopen(webpage)
    #print(page.read())
    soup=BeautifulSoup(page,'html.parser')
    #soup=BeautifulSoup(page.read())
    test=soup.prettify()
    
    test=list(soup.prettify())
    test=test[1:]
    test.pop()
    test.pop()
    test="".join(test)
    
    print(test)
    #data=json.load(soup)
    
    #file=open('test.json',"w")
    #file.write(soup.prettify())
    #file.close()
    City=[]
    Zipcode=[]
    data = json.loads(test)
    #print (data)
    for i in range(len(data["result"])):
        City.append(data["result"][i]['City'])
        Zipcode.append(data["result"][i]['Zipcode'])
        print(data["result"][i]['County'])
    for i in range(len(City)):
        print(City[i]," ", Zipcode[i])
    print(len(data["result"])) 
    print(len(City))
