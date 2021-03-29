from flask import Flask,jsonify,request
from flask_cors import CORS
from helper import requestHelper
from services import feedbackService
#######################################################

#configurations
DEBUG = True

#instantiate app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myKey!'
app.config.from_object(__name__)


#enable CORS
CORS(app,resources={r'/*':{'origins':'*'}})
#######################################################
#######################################################
#sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#######################################################
#######################################################
@app.route('/savefeedback', methods=['POST'])
def saveFeedback():
    try:
        resultObj = {}
        postParams = requestHelper.extractPayload(request)

        feedbackObject = feedbackService.Feedback()
        resultObj = feedbackObject.saveFeedback(postParams)

        return jsonify(postParams)
    except Exception as e:
        resultObj["status"] = "error"
        resultObj["message"] = str(e)
        return jsonify(resultObj)





if __name__ == '__main__':
    app.run()