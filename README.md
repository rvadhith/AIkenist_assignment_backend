The python flask backend has the following functions

fileUpload():<br />
  -This serves to make the POST request from frontend when the user uploads a file <br />
  -Images("jpeg","jpg","png") uploaded by the user would be stored in folder named "images" inside "static" folder <br />
  -A response object containing the name of the image file uploaded would be sent to frontend <br />
  
get_image(image_name):  
  -This function serves the GET request from frontend <br />
  -The request string will contain the name of the image file to be fetched <br />
  
