from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from app.check_health import check_cpu_usage,check_localhost,check_memory_usage,check_disk_usage
from app.forms.osStatus import osStatus_form
from app.reports import  generate_report


@app.route('/status' ,methods=['GET', 'POST'])
def osstatus():
    data = {
        'cpu_usage':check_cpu_usage(),
        'localhost':check_localhost(),
        'memory_usage':check_memory_usage(),
        'disk_usage':check_disk_usage('/')
    }
    form = osStatus_form()
    
    if form.validate_on_submit():
        printData(data)
    
    return render_template('osStatus.html',data=data,form=form)


def printData(data):
    info = "CPU Usage :{}".format(data['cpu_usage']) + "localhost :{}".format(data['localhost']) + "Memory Usage :{}".format(data['memory_usage']) + "Disk Usage :{}".format(data['disk_usage'])
    generate_report('/home/mahmoudodeh/Downloads/status.pdf','Status',info)