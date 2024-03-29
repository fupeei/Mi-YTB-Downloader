from app import app
from flask import render_template, request, redirect, Response, send_file, flash
from pytube import YouTube
import os

path = os.getcwd() + "/output/"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/convierte1", methods=['POST'])
def convierte1():
    url = request.form['url']
    print(url)
    yt = YouTube(url)
    yt = yt.streams.get_highest_resolution()
    
    try:
        yt.download(path)
        p = path + yt.title + ".mp4"
    except:
        print("Hubo un error al descargar el video del URL proporcionado")
    print("¡Descarga completada con éxito!")
    
    flash("¡Procesado completado con éxito!")
    return send_file(p,  as_attachment=True)

@app.route("/convierte2", methods=['POST'])
def convierte2():
    url = request.form['url']
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first() 
    
    try:
        out_file = video.download(path)
        base, ext = os.path.splitext(out_file) 
        p = base + '.mp3'
        os.rename(out_file, p)
        flash("¡Descarga completada con éxito!")
    except:
        print("Hubo un error al descargar el video del URL proporcionado")
    # save the file 
    print("¡Descarga completada con éxito!")
    return send_file(p, as_attachment=True)