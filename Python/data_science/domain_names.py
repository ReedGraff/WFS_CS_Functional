from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
import requests
import json























































def Get_All_First_Page_Links(url):
    source = urlopen(url).read()
    soup = BeautifulSoup(source,'lxml')

    list_1 = []
    for link in soup.find_all('a', href=True):
        list_1.append(link["href"])
        
    print(list_1)










































def Get_All_Domain_Links(url):
    # Definitions
    def skip():
        with open("static.json", "w") as jsonFile:
            data = json.load(jsonFile)
            data["links"][index]["has been searched"] = True
            json.dump(data, jsonFile, indent = 4)

    def is_valid(url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def find_correct_iteration(index, link):
        pass
    
    
    #Clear previous data
    data = {}
    with open("static.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    
    #Get domain names 
    try:
        domain = urlparse(url).netloc
    except:
        domain = url.split("//")[-1].split("/")[0]

    #Set layout
    starting_data = {
        "original link": url,
        "domain": domain,
        "links": [
            {
                "link": url,
                "has been searched": False,
                "has query": None,
                "is in domain": True
            }
        ]
    }

    with open("static.json", "w") as jsonFile:
        json.dump(starting_data, jsonFile, indent = 4)
        
    finished = True
    index = 0
    while !finished:
        with open("static.json", "r") as jsonFile:
            data = json.load(jsonFile)
            link = data["links"][index]["link"]

            if ".pdf" in link or ".DOC" in link or ".DOCX" in link:
                skip()
            else:
                if domain in link:
                    domain_query = True
                else:
                    if link[0] == "/" or link[0] == "\\":
                        if domain[-1] == "/" or domain[-1] == "\\":
                            domain[:-1:]

                        
                        link = domain + link
                        try:
                            urllib.urlopen(link)
                        except:
                            try:

                            return ("Failed on this link" + link)
                    else:
                        pass




    
    '''
    with open("static.json", "r") as jsonFile:
        data = json.load(jsonFile)





    #ake soups
    try:
        source = urlopen(url).read()
        soup = BeautifulSoup(source,'lxml')
    except:
        soup = BeautifulSoup(requests.get(url).content, "lxml")


    try:
        domain_name_2 = url.split("//")[-1].split("/")[0] 
    except:
        print(url)

    """
    list_1 = []
    for href in soup.find_all('a', href=True):
        href = tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(i, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
    
    print(domain_name)
    print(href)
    """

    '''



links = ['https://www.ci.richland.wa.us/departments/energy-services', 'https://cityofcovington.org/index.php?section=covington_utilities3', 'http://unioncitytn.gov/pay-online.html', 'https://dicksonelectric.com/', 'https://www.jea.com/my_account/billing_and_payment_options/', 'https://www.mtpleasant-tn.gov/utility-payments', 'https://www.sepb.net/payment-2/bill-pay/', 'https://www.fulton-ky.com/frequently-asked-questions/', 'https://www.cityofblueridgega.gov/WastewaterandWater.aspx', 'https://midstateelectric.coop/payment-options', 'https://wkrecc.com/index.php/18-billing', 'https://mdec.org/', 'https://www.mlgw.com/residential/payingyourbill_b', 'https://www.caneyforkec.com/', 'https://www.humboldtutilities.com/', 'http://www.hsutilities.com/', 'https://www.cityofmadison.com/water', 'https://hop-electric.com/electric/residential-electric/bill-payment-options/', 'https://ace-power.com/account/payment-options/', 'https://www.ocalafl.org/government/city-departments-a-h/customer-service-office/pay-my-bill', 'https://www.bolivarutility.com/', 'https://lakeworthbeachfl.gov/payment-portal/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.bpu.com/', 'https://www.cityofdenton.com/en-us/pay-my-bill', 'https://www.stemc.com/my-payment-options', 'https://www.dixie.coop/online-account-access', 'https://www.orangecountyfl.net/WaterGarbageRecycling/BillPaymentOptions.aspx', 'https://cityofblakely.net/pay-online/', 'https://www.epbnet.com/index.php/support/bill-pay/', 'http://www.bcestn.org/index.php/manage-existing-service/pay-my-monthly-bill/106-pay-by-phone-or-online', 'https://www.salemmo.com/city/government/departments/utility_department/index.php', 'https://www.lexingtontn.gov/pay_online.html', 'https://www.newbernnc.gov/departments/administration/finance/utilities_business_office/pay_my_bill.php', 'https://www.tsemc.net/my-account/pay-bill-online/', 'https://cpws.com/my-account/', 'https://www.lcub.com/', 'https://www.dothan.org/175/Pay-View-Utility-Bill-Online', 'http://www.pickwickec.com/bill-payment-information/', 'https://www.wilsonnc.org/residents/all-departments/financial-services/customer-service-and-business-operations/payment-options', 'https://www.tombigbeeelectric.com/payments', 'https://cityofrockwood.com/online-bill-pay', 'http://www.shelbyvillepower.com/', 'https://www.yourubt.com/', 'http://www.clintonutilities.com/pmtopts.html', 'https://www.rse.coop/', 'https://www.geus.org/', 'https://selma-nc.com/departments/customer-service/', 'http://www.clevelandutilities.com/', 'https://www.mayfieldews.com/index.php/electric/smartpay', 'https://guntersvilleal.org/departments/utilites/', 'https://ripleypower.com/account/payment-options.php', 'http://www.mub-albertville.com/', 'http://www.franklinepb.com/bill-payment-options', 'https://lagrangenc.com/703/Online-Billing', 'https://www.cityofdouglasga.gov/84/Make-a-Utility-Payment', 'https://www.townofbenson.com/2191/Bill-Payment', 'https://www.scecnet.net/content/pay-my-bill', 'http://www.glasgowepb.net/?page_id=343', 'https://www.needhelppayingbills.com/html/tarrant_county_assistance_prog.html', 'https://www.tvec.com/index.asp?fullsite=1']

for link in links:
    Get_All_Domain_Links(link)
