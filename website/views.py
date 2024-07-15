import os
from django.shortcuts import render, redirect
from django.db import connection, connections
from django.utils import timezone
import datetime
from django.http import HttpResponseRedirect
from .models import Softmatterdata
from .forms import dataForm
from .forms import addForm
import psycopg2

conn = psycopg2.connect(
    database = "softmatterdb",
    user = "doadmin",
    password = "AVNS_I8Zm7kvsCUvxQYGL-8m",
    host = "app-11527f32-58de-4dea-aa6f-31cd5d286cdf-do-user-14527951-0.b.db.ondigitalocean.com",
    port = "25060",
    sslmode = "require"
)

#conn.autocommit = True
"""
materials = {
    'identifier' : 'elastic',
    'composition' : 'myosin',
    'method' : 'confocal',
    'name' : 'jane doe',
    'acquired' : '11.8.23',
    'lastupdate' : '11.8.23',
    'doi' : 'none'
    }
"""
in_depth = {
    'identifier' : 'elastic',
    'detailed_comp' : 'Lorem ipsum dolor sit amet',
    'image' : 'example.jpg',
    'acquisition_detail' : 'Lorem ipsum dolor sit amet',
    'metadata' : 'metadata.pdf',
    'process_notes' : 'Lorem ipsum dolor sit amet',
    'additional_resources' : 'protocol.pdf'
}


def index(request):
    #need database info: "SELECT column, column, column FROM table ORDER BY column"
    materials = Softmatterdata.objects.all()
    return render(request, "website/index.html",{
        "materials":materials
    })
    """
    rows = []
    sqlQuery = "SELECT * FROM softmatterdata ORDER BY softmatterdata.identifier" 
    print("Yes")
    with conn.cursor() as cursor:
        print("HELP")
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        print(len(rows))
        cursor.close()
    
    return render(request, "website/index.html", {
        "materials":rows
    })
    """
"""
def indexWithSort(request, sort):
    #if sort in [list_of_sortable_elements]
    rows=[]
    if sort in ["name", "color"]:
        print("NO")
        sqlQuery = f"SELECT * FROM softmatterdata ORDER BY softmatterdata.{sort}"
        with conn.cursor() as cursor:
            cursor.execute(sqlQuery)
            rows = list(cursor.fetchall())
            cursor.close()
    
    return render(request, "website/index.html", {
        "materials": rows
    })
"""

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        projectsComp = Softmatterdata.objects.filter(composition__contains=searched)
        projectsSummary = Softmatterdata.objects.filter(summary__contains=searched)

        return render(request, "website/search_results.html",{
            "comps":projectsComp,
            "summed":projectsSummary
        })
    
    return render(request, "website/index.html",{
    })
    
    """
    query = request.GET.get('q')
    results = []
    if query:
        sql_query = 
        SELECT * FROM softmatterdata
        WHERE LOWER(composition) LIKE %s OR LOWER(name) LIKE %s
        
        search_term = f"%{query.lower()}%"
        
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql_query, (search_term, search_term))
                results = cursor.fetchall()
        except Exception as e:
            conn.rollback()  # Rollback the transaction if an error occurs
            print("This value can not be found")
        finally:
            cursor.close()  # Ensure the cursor is closed in all cases
    
        return render(request, "website/index.html", {
        "materials": results
    })
    """

def add_material(request):
    submitted = False
    
    if request.method == 'POST':
        form=addForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.name = request.user
            x.save()
            return render(request, 'website/add_material.html', {
                'submitted': True
            })
    """
    else:
        form = addForm
        if 'submitted' in request.GET:
            submitted = True
    """
    form = addForm()

    return render(request, 'website/add_material.html', {
        'form':form, 
        'submitted': submitted
    })
    
    """
    if request.method == "POST":
        material_name = request.POST['composition']
        acquisition_method = request.POST['method']
        name = request.POST['name']
        date_acquired = request.POST['acquired']
        last_updated = request.POST['lastupdate']
        doi = request.POST['doi']
        summary = request.POST['summary']

        if not all([material_name, acquisition_method, name, date_acquired, last_updated, doi, summary]):
            # Handle the case where some fields are missing
            # You might want to return an error message or render the form again with an error message
            return render(request, 'website/add_material.html', {'error': 'All fields are required.'})

        sqlQuery = 
        INSERT INTO softmatterdata (composition, method, name, acquired, lastupdate, doi, summary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        
        with conn.cursor() as cursor:
            cursor.execute(sqlQuery, [material_name, acquisition_method, name, date_acquired, last_updated, doi, summary])
            conn.commit()

        return redirect('index')

    return render(request, 'website/add_material.html')
    """

#deleted sID parameter to make it run, need to add it abck in later
def materialInfo(request, sID):
    curr_obj = Softmatterdata.objects.get(identifier=sID)
    return render(request, 'website/website_info.html', {
        "in_depth": curr_obj
    })

    """
    # need info on the database and its tables
   #f"SELECT item.info1, item.info2, item.info3 FROM item"
    #this method gives the info for each specific material
    sqlQuery = 
        SELECT *
        FROM softmatterdata
        WHERE softmatterdata.identifier = %s
    
    with conn.cursor() as cursor:
        cursor.execute(sqlQuery, [sID])
        rows = cursor.fetchone()
        cursor.close()
    # return render(request, "website/item.html", {
    # "info":rows})
    return render(request, 'website/website_info.html', {
        "in_depth":rows
    })
"""
def delete_item(request, sID):
    curr_obj = Softmatterdata.objects.get(identifier=sID)
    if curr_obj.lock:
        return render(request, 'website/fail.html', {})

    if(curr_obj.meta_data):
        meta_path = curr_obj.meta_data.path
        if os.path.exists(meta_path):
            os.remove(meta_path)

    if(curr_obj.sample_image):
        img_path = curr_obj.sample_image.path
        if os.path.exists(img_path):
            os.remove(img_path)
        
    curr_obj.delete()
    return redirect('index')

def edit_material(request, sID):
    curr_obj = Softmatterdata.objects.get(identifier=sID)
    if curr_obj.lock == False:
        form = dataForm(request.POST or None, request.FILES or None, instance=curr_obj)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'website/fail.html', {})
    
    return render(request, 'website/update.html',{
        "data":curr_obj,
        'form':form
    })

def lock_item(request, sID):
    curr_obj = Softmatterdata.objects.get(identifier=sID)
    if curr_obj.lock == False:
        curr_obj.lock = True
        curr_obj.save()
        return render(request, 'website/lock.html', {
            'is_locked':False
        })

    return render(request, 'website/lock.html', {
            'is_locked':True
    })

