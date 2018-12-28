from flask import Flask,render_template,request
import requests
app = Flask(__name__)

@app.route('/')#View HomePage
def home():
   return render_template ('index.html')
@app.route('/upload')#View UploadForm
def showuploadform():
    return render_template('uploadform.html')
@app.route('/result',methods=['GET','POST'])#Processing in BackEnd and viewing result to user.
def userupload():
    if request.method == "POST":
        f=request.files['file']
        f.save(f.filename)
    api_key = 'acc_84e09628a487fed'
    api_secret = '21960297e38ff21c28a5e416bb752b8f'
    image_path = f.filename
    response = requests.post('https://api.imagga.com/v2/uploads',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
    res=response.json()
    res=res['result']['upload_id']
    #End of Getting upload ID
    respo = requests.get('https://api.imagga.com/v2/tags',auth=(api_key, api_secret),params={'image_upload_id':res})
    respo=respo.json()
    respo=respo['result']['tags']
    respo=respo[0]#getting the tag with the most confidence
    respo=respo['tag']['en']
    #End of getting tag related to picture
    respo = requests.get('http://api.giphy.com/v1/gifs/search',params={'q':respo,'api_key': 'I0x0SsYZAC3rbSIiizVu6nefxnaR9CLR'})
    respo=respo.json()
    respo=respo['data']
    addresslist=[]
    for i in range(0,10):#Gets addresses of 10 animated gifs
        resp=respo[i]
        resp=resp['images']['fixed_height']['url']
        addresslist.append(resp)
    addresstuple=tuple(addresslist)#Convert address list of 10 animated gifs to tuple. list is forbidden here.
    return render_template('result.html',resp=addresstuple)#Finally, Here is the result.

if __name__ == '__main__':
   app.run(debug=True)
