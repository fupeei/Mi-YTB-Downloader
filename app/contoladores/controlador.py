from app import app
from flask import render_template, request, redirect, Response, send_file, flash
from pytube import YouTube
import os

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/convierte1", methods=['POST'])
def convierte1():
    url = request.form['url']
    print(url)
    destino = "Descargas"
    yt = YouTube(url)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download("/Users/cooka/Downloads/")
    except:
        print("Hubo un error al descargar el video del URL proporcionado")
    print("¡Descarga completada con éxito!")
    flash("¡Descarga completada con éxito!")
    return redirect("/home")

@app.route("/convierte2", methods=['POST'])
def convierte2():
    url = request.form['url']
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first() 
    
    try:
        out_file = video.download("/Users/cooka/Downloads/")
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except:
        print("Hubo un error al descargar el video del URL proporcionado")
    # save the file 
    print("¡Descarga completada con éxito!")
    flash("¡Descarga completada con éxito!")
    return redirect("/home")