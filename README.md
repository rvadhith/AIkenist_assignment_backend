The python flask backend has the following functions

fileUpload():
  -This serves to make the POST request from frontend when the user uploads a file
  -Images("jpeg","jpg","png") uploaded by the user would be stored in folder named "images" inside "static" folder
  -A response object containing the name of the image file uploaded would be sent to frontend
  
get_image(image_name):  
  -This function serves the GET request from frontend
  -The request string will contain the name of the image file to be fetched
  
