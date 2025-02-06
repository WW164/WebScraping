from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

def product(request):
    df = pd.read_csv("H:\Projects\PY project\webScraping\products.csv")
    html_object = df.to_html()
    return HttpResponse(html_object)
