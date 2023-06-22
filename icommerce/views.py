from django.shortcuts import render, HttpResponse
from .models import Product, Order, Contact, admin
import requests
from itertools import chain
import smtplib

# Create your views here.
def home(request):
    catprods = Product.objects.values()
    length = len(catprods)-1
    idd = catprods[length]['id']
    newprod = Product.objects.filter(id=idd)
    allprod = Product.objects.values()
    webprod = Product.objects.filter(Cateogary = "Graphical Applications")
    params = {'newprod': newprod, 'allprod': allprod, 'gui': webprod, 'clas': 'active'}
    return render(request, 'index.html', params)

def about(request):
    params = {'abou': 'active'}
    return render(request, 'about.html',params)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request, methods = ['GET', 'POST']):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        contact = Contact(fname=fname, lname=lname, subject=subject, message=message, email=email)
        contact.save()
        sender_add = 'yourEmail'
        password = 'yourPassword'
        reciever_add = email
        server = smtplib.SMTP('smtp.gmail.com:587')
        subb = f'{fname} you Order Has been Placed'
        mailBody = "Hey Aman\n\nLooks like you got a Contact from Your RushX Community\nSharing the Details with You but with a Request to not to share your Customers Data"
        mailBody += f'\n\n Name : {fname} {lname}\nSubject for Contacting : {subject}\nEmail : {email}\nMessage : {message}\n\nBe sure to Replu to this E - mail as It will give them a Good response rest I will manage\n\nShay Mercer(RushX Community)'
        msg1 = f"""Subject : {subb}\n\n{mailBody}"""
        server.starttls()
        server.login(sender_add, password)
        server.sendmail(sender_add, reciever_add, msg1)
        string = f'Thank You Your Message has been sucessfully Sent to the {admin}'
        params = {'string': string, 'cont': 'active'}
        return render(request, 'contact.html', params)
    params2 = {'cont': 'active'}
    return render(request, 'contact.html', params2)

def shop(request, methods=['GET', 'POST']):
    if request.method == 'POST':
        allProds = []
        catProds = Product.objects.values()
        params = {'allprods': catProds}
        return render(request, 'shop.html', params)
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications")
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications")
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications")
    catProds = Product.objects.values()
    params = {'allprods': catProds, 'shop': 'active', 'console': len(lengthofConsole), 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop)}
    return render(request, 'shop.html', params)

def thankyou(request, methods = ['GET', 'POST']):
    allprods = Product.objects.values()
    if request.method == 'POST':
        country = request.POST.get('countryinput')
        itemsJson = request.POST.get('itemsJson')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        link = {}
        name = {}
        space = 0
        mailBody=f'Hey {fname},\n\nYour Order has Been Place You can Download Your Orders from Below Links\n\n'
        # str(itemsJson).split('"')[3]
        try:
            for i in range(0, len(allprods)):
                space = space + 3
                if allprods[i]["Product_Name"] == str(itemsJson).split('"')[space]:
                    link.update( {f'product{i}': allprods[i]["linkToDownload"] } )
                    name.update( {f'product{i}': allprods[i]["Product_Name"] } )
                    j = i + 1
                    mailBody += f'{j}. {allprods[i]["Product_Name"]}: {allprods[i]["linkToDownload"]} \n\n'
                    space = space + 3
        except IndexError as e:
            pass
        link2 = {'item': link, 'name': name}
        order = Order(itemsJson=itemsJson, firstName=fname, lastName=lname, email=email, address=address,
                       state=state, zipcode=zipcode, phone=phone, amount=amount, country=country)
        order.save()
        sender_add = 'developerlife69@gmail.com'
        password = 'somkumud'
        reciever_add = email
        server = smtplib.SMTP('smtp.gmail.com:587')
        subb = f'{fname} you Order Has been Placed'
        mailBody += "\nThank You for Shopping with us\nWe hope to See you Again\n\nRushX Community\n\nFor More Products and Updated Products Follow our Leader to get the Latest Updates"
        mailBody += "\n\nGitHub Profile : https://github.com/coderaman07"
        mailBody += "\nTwitter Profile : https://twitter.com/coderaman07"
        mailBody += "\nInstagram Profile : https://instagram.com/aman_.dev"
        msg1 = f"""Subject : {subb}\n\n{mailBody}"""
        server.starttls()
        server.login(sender_add, password)
        server.sendmail(sender_add, reciever_add, msg1)
        return render(request, 'thankyou.html', link2)

def view(request, Product_Name, ID_of_the_Product):
    allProds = []
    idprod = int(ID_of_the_Product)
    catProds = Product.objects.filter(id=idprod)
    allProds = Product.objects.values()
    params = {'allprods': allProds, 'catprods': catProds}
    return render(request, 'shop-single.html', params)

def web(request):
    head = "Web Applications"
    Prods = Product.objects.filter(Cateogary = "Web Applications")
    allprods = Product.objects.values()
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications")
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications")
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications")
    prods = {'head': head, 'style': 'active', 'prod': Prods, 'allprods': allprods, 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop), 'console': len(lengthofConsole)}
    return render(request, 'DiffrentiatedPoducts.html', prods)

def desktop(request):
    head = "Graphical Applications"
    Prods = Product.objects.filter(Cateogary = "Graphical Applications")
    allprods = Product.objects.values()
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications")
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications")
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications")
    prods = {'head': head, 'style': 'active', 'prod': Prods, 'allprods': allprods, 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop), 'console': len(lengthofConsole)}
    return render(request, 'DiffrentiatedPoducts.html', prods)

def console(request):
    head = "Console Applications"
    Prods = Product.objects.filter(Cateogary = "Console Applications")
    allprods = Product.objects.values()
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications")
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications")
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications")
    prods = {'head': head, 'style': 'active', 'prod': Prods, 'allprods': allprods, 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop), 'console': len(lengthofConsole)}
    return render(request, 'DiffrentiatedPoducts.html', prods)

def frontend(request):
    params = {'style': 'active'}
    return render(request, 'currentlyInBuild.html', params)

def backend(request):
    params = {'style': 'active'}
    return render(request, 'currentlyInBuild.html', params)

def search(request, keyword):
    catprods = Product.objects.filter(Cateogary = keyword)
    allprods = Product.objects.values()
    params = {'allprods': allprods, 'catprods': catprods, 'cat': keyword}
    return render(request, 'search.html', params)

def sub(request, email):
    response = requests.post('https://coderaman07.ck.page/', data = {'name' : email})
