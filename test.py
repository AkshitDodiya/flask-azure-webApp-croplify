# try :
#     from app import app
#     import unittest
# except Exception as e :
#     print(f"some module are missing : e")
 
from app import app, crop_prediction
import unittest

class FlaskTest(unittest.TestCase):
    
    #check for 200 response 
    def test_index_home(self):
        tester = app.test_client(self)
        res = tester.get('/')   
        statuscode = res.status_code
        self.assertEqual(statuscode,200)
        
    def test_index_crop_recommend(self):
        tester = app.test_client(self)
        res = tester.get('/crop-recommend')   
        statuscode = res.status_code
        self.assertEqual(statuscode,200)
    
    def test_index_content_home(self) :
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")   

    def test_index_content_crop_recommend(self) :
        tester = app.test_client(self)
        response = tester.get('/crop-recommend')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")   

    def test_post_content_crop_recommend(self) :
        tester = app.test_client(self)
        response = tester.post(
            '/fertilizer-predict',
            data=dict(cropname='maize', 
                      nitrogen=5, 
                      phosphorous=5, 
                      pottasium=5),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)   

if __name__ == "__main__" : 
    unittest.main()