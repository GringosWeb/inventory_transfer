from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file = drive.CreateFile({'id': '1MiIgBkgAMmuRJEJ9sksxQAXVzPFNUouhEoOvYtEh-Yc'})
file.GetContentFile('')