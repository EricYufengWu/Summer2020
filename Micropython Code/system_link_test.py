import binascii, json, requests, time 

Key = 'tdsf-B2RXI5ALFF3XdGPRBnq3bFNHobWafdAQk6-zW'
    
def SL_setup():
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = {"Accept":"application/json","x-ni-api-key":Key}
    return urlBase, headers
    
def Put_SL(Tag, Type, Value):
    urlBase, headers = SL_setup()
    urlValue = urlBase + Tag + "/values/current"
    propValue = {"value":{"type":Type,"value":Value}}
    try:
        reply = urequests.put(urlValue,headers=headers,json=propValue).text
    except Exception as e:
        print(e)         
        reply = 'failed'
    return reply

def Get_SL(Tag):
    urlBase, headers = SL_setup()
    urlValue = urlBase + Tag + "/values/current"
    try:
        print('testing')
        value = urequests.get(urlValue,headers=headers).text
        data = ujson.loads(value)
        print(data)
        result = data.get("value").get("value")
    except Exception as e:
        print(e)
        result = 'failed'
    return result
    
def Create_SL(Tag, Type):
    urlBase, headers = SL_setup()
    urlTag = urlBase + Tag
    propName={"type":Type,"path":Tag}
    try:
        urequests.put(urlTag,headers=headers,json=propName).text
    except Exception as e:
        print(e)
        
# Get_SL('Eric')
# Create_SL('Eric','STRING')
# Put_SL('Eric','STRING','done')
Get_SL('Eric')