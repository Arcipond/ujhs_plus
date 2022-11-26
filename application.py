from flask import Flask, request, jsonify
import mealfind as mf
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def check():
    return "Working..."

@app.route('/meal_find', methods=['POST'])
def meal_find():	# 함수선언
    req = request.get_json()
    
    
    meal_date = req["action"]["detailParams"]["sys_date"]["value"]
    if meal_date == "today":
        meal_date = datetime.today().strftime("%Y-%m-%d")[2:]
    else:
        meal_date = meal_date[10:20]
    mdata = mf.mealfind.find(meal_date)
    #print(mdata)
    
    
    if mdata[0]=="None": mdata[0]=["해당 급식 정보가 없습니다."]
    if mdata[1]=="None": mdata[1]=["해당 급식 정보가 없습니다."]
        
    meal_time = req["action"]["detailParams"]["meal_time"]["value"]
    
    
    lunch_items = {
            "type": "item",
            "title": "중식",
            "description": ' '.join(mdata[0])
        }
    dinner_items = {
            "type": "item",
            "title": "석식",
            "description": ' '.join(mdata[1])
    }

    
    
    if meal_time == "중식":
        dinner_items = {}
    elif meal_time == "석식":
        lunch_items = {}
    
    

        
    
	# 답변 설정
    res = {
  "contents": [
    {
      "type": "card.list",
      "cards": [
        {
          "listItems": [
            {
                "type": "title",
                "imageUrl": "https://scsgozneamae10236445.cdn.ntruss.com/data2/content/image/2016/10/25/201610250520947.jpg",
                "title": "해당 날짜 운정고 급식!"
                
            },
            lunch_items, dinner_items
            
                        ]
            }
        ]
    }
  ]
}

	
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
    