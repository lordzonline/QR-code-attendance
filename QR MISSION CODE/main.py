from flask import Flask,render_template,request
from MyQR import myqr
import os
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return  render_template("index.html")


@app.route("/result",methods=['POST'])
def result():
    output= request.form.to_dict()
    name= output["name"]
    with open('students.txt','a+') as f:
            f.write('\n')
            f.write(name)
            
        
    f = open('students.txt','r')
    lines = f.read().split("\n")
    print(lines)

    for _ in range (0,len(lines)):
        data = lines[_]
        version,level,qr = myqr.run(
            str(data),
            level='H',
            version=1,
            picture="Bg.png",
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name = str(lines[_]+'.png'),
            save_dir=os.getcwd()
        )
    return render_template("index.html",name=name)


if __name__ == "__main__":
    app.run(debug=True,port=5001)
