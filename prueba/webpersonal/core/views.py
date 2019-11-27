from django.shortcuts import render, HttpResponse


# Create your views here.
html_response = ""

def home(request):       
       return render(request,"core/home.html")

def about(request):

            return HttpResponse(html_response +"""
            <h2> Acerca de <h2/>
            <P> acercate ......</P>
            """)

def portfolio(request):

            return HttpResponse(html_response +"""
            <h2> PORTAFOLIO <h2/>
            
""")
def contact(request):

            return HttpResponse(html_response +"""
            <h2>CONTACT<h2/>
            
            
            """)
