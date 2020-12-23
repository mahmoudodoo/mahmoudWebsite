from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from app.check_health import check_cpu_usage,check_localhost,check_memory_usage,check_disk_usage

@app.route('/status')
def osstatus():
    data = {
        'cpu_usage':check_cpu_usage(),
        'localhost':check_localhost(),
        'memory_usage':check_memory_usage(),
        'disk_usage':check_disk_usage('/')
    }
    return render_template('osStatus.html',data=data)