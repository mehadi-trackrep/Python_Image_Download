import csv
import urllib
import cv2

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# return the image
	return image

prefix_url = 'http://cse.sust.edu/reunion'


with open('photo_links.csv', "r") as f:
    reader = csv.reader(f)
    for row in reader:
#         print " ---> " + prefix_url + row[2]
            if row[2] != '/dummy.png':
                url = prefix_url + row[2]
                image = url_to_image(url)
                file_name = "./" + row[0] + "_" + row[1] + ".jpg"
            	cv2.imwrite(file_name, image)
            # 	cv2.imshow("Image", image)
            	cv2.waitKey(0)

# # loop over the image URLs
# for url in urls:
# 	# download the image URL and display it
# 	image = url_to_image(url)
#
# 	cv2.imwrite("./abc.jpg", image)
# # 	cv2.imshow("Image", image)
# 	cv2.waitKey(0)


#print(urls)
