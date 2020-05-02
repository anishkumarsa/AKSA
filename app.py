from flask import Flask,render_template,redirect,url_for,request
import pickle

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def salpred():
    if request.method=='POST':
      user=request.form['nm']
      
      if (user.isalpha() ==True):
        return render_template('salpred.html',ps='alp')
      else:  
        if(len(user)>0):
          if (float(user)>=1):
            model = pickle.load(open('model.pkl','rb'))
            val=model.predict([[float(user)]])
            absv=int(round(val[0]))
            return render_template('predsal.html',ps=absv)
          elif (float(user)<1):
            return render_template('salpred.html',ps='demo')
        else:
          return render_template('salpred.html',ps='null')
    return render_template('salpred.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
