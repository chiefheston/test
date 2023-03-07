from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'menu/index.html')


def menu(request) -> str:
    queryset = Item.objects.all().values()
    item_id = request.GET.get("id")


    def get_path(item_id: int) -> list:
        tree_set = []
        if item_id != 0:
            while item_id != None:
                for item in queryset:
                    if str(item_id) == str(item['id']):
                        tree_set.append(item)
                        item_id = item['parent_id']
            tree_set.reverse()
        return tree_set
    

    def create_html(tree_set: list) -> str:
        html = ''
        for item in tree_set:
            if str(item['id']) == item_id:
                html += f"<div class='parent'><strong><a href='/menu/?id={item['id']}&name={item['name']}'>{item['name']}</a></strong>"
                for child in queryset:
                    if child['parent_id'] == item['id']:
                        html += f"<div class='child'><a href='/menu/?id={child['id']}&name={child['name']}'>{child['name']}</a></div>"
                html += "</div>"
            else:
                html += f"<div class='parent'><a href='/menu/?id={item['id']}&name={item['name']}'>{item['name']}</a></div>"
        return html

    
    html = f"<div>{create_html(get_path(item_id))}</div>"


    return HttpResponse(html)