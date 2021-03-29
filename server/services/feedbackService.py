import random
from helper.dbHelper import mysqlDb
from datetime import datetime
import re


mobileRegex = re.compile("[7-9][0-9]{9}")
emailRegex = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
################################################################################################
################################################################################################
class Validation():
    def validateFeedback(feedbackDetails):
        print(feedbackDetails.keys())
        try:
            #################################################################################
            if('name' in feedbackDetails.keys() and len(feedbackDetails["name"]) > 0):
                pass
            else:
                raise Exception("Please Enter Your Name")
            #################################################################################
            if('mobile' in feedbackDetails.keys() and len(feedbackDetails["mobile"]) > 0):
                if(len(feedbackDetails["mobile"]) != 10 ):
                    raise Exception("Mobile Number Cannote Be Bigger Than 10 Digits")
                
                if(mobileRegex.match(feedbackDetails["mobile"])):
                    pass
                else:
                    raise Exception("Mobile Number Can Only Contain Digits From 0-9")
            else:
                raise Exception("Please Enter Your Mobile Number")
            #################################################################################
            if('email' in feedbackDetails.keys() and len(feedbackDetails["email"]) > 0):
                if(emailRegex.match(feedbackDetails["email"])):
                    pass
                else:
                    raise Exception("Invalid Email Formmat")
            else:
                raise Exception("Please Enter Your Email")
            #################################################################################
            if('subject' in feedbackDetails.keys() and len(feedbackDetails["subject"]) > 0):
                pass
            else:
                raise Exception("Feedback Subject Is Required")
            #################################################################################
            if('description' in feedbackDetails.keys() and len(feedbackDetails["description"]) > 0):
                pass
            else:
                raise Exception("Feedback Description is Required")
            #################################################################################
                
        except Exception as e:
            print(e)
            raise Exception(e)

class Feedback(Validation):
    def __init__(self):
        pass

    def generaterefId():
        pass

    def saveFeedback(self,postParams):
        try:
            Validation.validateFeedback(postParams)
            return postParams
        except Exception as e:
            raise Exception(e)

