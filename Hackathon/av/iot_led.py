
def run(led_on):
    from firebase_admin import credentials
    import firebase_admin, os

    path = './av'
    file = 'page-view-7a557-firebase-adminsdk-pdusy-81a1eadd2f.json'
    dir = os.path.join(path, file)

    cred = credentials.Certificate(dir)
    url = 'https://page-view-7a557-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, path)

    from firebase_admin import db
    refv = db.reference('iot/led')

    refv.set(led_on)
    g = refv.get()
    return g