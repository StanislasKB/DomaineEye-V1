from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from DomainEyeApp.models import History

def home_view(request):
    return  render(request, 'home_view.html')


        
def my_get(dictionnaire, cle_parent,cle_fille):
    if dictionnaire.get(cle_parent)==None:
        return 'None'
    else :
        return dictionnaire.get(cle_parent).get(cle_fille)
    
    
def data_view(request):
    lien=''
    historique=History()
    endpoint ="https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_emJnsoVfk2tqiM7CSBJaoSY6XhsfN&domainName={}&outputFormat=JSON"
    source = "https://api.apilayer.com/whois/query?domain={}&apikey=pV1QadkNc6tLJWXpJLCbBSOLiDVIf5g4"
    if request.method=='POST':
        lien=request.POST['search']
        list_of_data =requests.get(endpoint.format(lien)).json()
        list_of_data=list_of_data['WhoisRecord']
   
        second_data_list=requests.get(source.format(lien)).json()
        second_data_list=second_data_list['result']
        
        data={
        "domain" : str(list_of_data.get('domainName')),
        "nameServer" : str(second_data_list.get('name_servers')[0]),
        "nameServer2" : str(second_data_list.get('name_servers')[1]),
        "dateCreated":str(second_data_list.get('creation_date')),
        "dateUpdated":str(second_data_list.get('updated_date')),
        "dateExpires":str(second_data_list.get('expiration_date')),
        "nameRegistrar" : str(list_of_data.get('registrarName')),
        "whoisServer" : str(second_data_list.get('whois_server')),
        "registrarURL": str(second_data_list.get('referral_url')),
        "registrarStatut" : str(second_data_list.get('status')),
        "registrantName": str(my_get(list_of_data,'registrant','name')),
        "registrantOrg": str(my_get(list_of_data,'registrant','organization')),
        "registrantCity": str(my_get(list_of_data,'registrant','city')),
        "registrantState": str(my_get(list_of_data,'registrant','state')),
        "registrantPC": str(my_get(list_of_data,'registrant','postalCode')),
        "registrantTel": str(my_get(list_of_data,'registrant','telephone')),
        "registrantFax": str(my_get(list_of_data,'registrant','fax')),
        "registrantCountry": str(my_get(list_of_data,'registrant','country')),
        
        "adminName": str(my_get(list_of_data,'administrativeContact','name')),
        "adminOrg": str(my_get(list_of_data,'administrativeContact','organization')),
        "adminCity": str(my_get(list_of_data,'administrativeContact','city')),
        "adminState": str(my_get(list_of_data,'administrativeContact','state')),
        "adminPC": str(my_get(list_of_data,'registrant','postalCode')),
        "adminTel": str(my_get(list_of_data,'administrativeContact','telephone')),
        "adminFax": str(my_get(list_of_data,'administrativeContact','fax')),
        "adminCountry": str(my_get(list_of_data,'administrativeContact','country')),
        
        "techName": str(my_get(list_of_data,'technicalContact','name')),
        "techOrg": str(my_get(list_of_data,'technicalContact','organization')),
        "techCity": str(my_get(list_of_data,'technicalContact','city')),
        "techState": str(my_get(list_of_data,'technicalContact','state')),
        "techPC": str(my_get(list_of_data,'registrant','postalCode')),
        "techTel": str(my_get(list_of_data,'technicalContact','telephone')),
        "techFax": str(my_get(list_of_data,'technicalContact','fax')),
        "techCountry": str(my_get(list_of_data,'technicalContact','country')),
        
    }
        historique=History.objects.create(domain=lien)
    elif request.GET.get('search_history'):
        lien=str(request.GET.get('search_history'))
        list_of_data =requests.get(endpoint.format(lien)).json()
        list_of_data=list_of_data['WhoisRecord']
   
        second_data_list=requests.get(source.format(lien)).json()
        second_data_list=second_data_list['result']
        
        data={
        "domain" : str(list_of_data.get('domainName')),
        "nameServer" : str(second_data_list.get('name_servers')[0]),
        "nameServer2" : str(second_data_list.get('name_servers')[1]),
        "dateCreated":str(second_data_list.get('creation_date')),
        "dateUpdated":str(second_data_list.get('updated_date')),
        "dateExpires":str(second_data_list.get('expiration_date')),
        "nameRegistrar" : str(list_of_data.get('registrarName')),
        "whoisServer" : str(second_data_list.get('whois_server')),
        "registrarURL": str(second_data_list.get('referral_url')),
        "registrarStatut" : str(second_data_list.get('status')),
        "registrantName": str(my_get(list_of_data,'registrant','name')),
        "registrantOrg": str(my_get(list_of_data,'registrant','organization')),
        "registrantCity": str(my_get(list_of_data,'registrant','city')),
        "registrantState": str(my_get(list_of_data,'registrant','state')),
        "registrantPC": str(my_get(list_of_data,'registrant','postalCode')),
        "registrantTel": str(my_get(list_of_data,'registrant','telephone')),
        "registrantFax": str(my_get(list_of_data,'registrant','fax')),
        "registrantCountry": str(my_get(list_of_data,'registrant','country')),
        
        "adminName": str(my_get(list_of_data,'administrativeContact','name')),
        "adminOrg": str(my_get(list_of_data,'administrativeContact','organization')),
        "adminCity": str(my_get(list_of_data,'administrativeContact','city')),
        "adminState": str(my_get(list_of_data,'administrativeContact','state')),
        "adminPC": str(my_get(list_of_data,'registrant','postalCode')),
        "adminTel": str(my_get(list_of_data,'administrativeContact','telephone')),
        "adminFax": str(my_get(list_of_data,'administrativeContact','fax')),
        "adminCountry": str(my_get(list_of_data,'administrativeContact','country')),
        
        "techName": str(my_get(list_of_data,'technicalContact','name')),
        "techOrg": str(my_get(list_of_data,'technicalContact','organization')),
        "techCity": str(my_get(list_of_data,'technicalContact','city')),
        "techState": str(my_get(list_of_data,'technicalContact','state')),
        "techPC": str(my_get(list_of_data,'registrant','postalCode')),
        "techTel": str(my_get(list_of_data,'technicalContact','telephone')),
        "techFax": str(my_get(list_of_data,'technicalContact','fax')),
        "techCountry": str(my_get(list_of_data,'technicalContact','country')),
        
    }
        
    else :
        data={}
      
    
    
    return render(request, 'data_view.html',data)
    
    
def history_view(request):
    historique=History.objects.all()
    return render(request,'history_view.html',{'history':historique})