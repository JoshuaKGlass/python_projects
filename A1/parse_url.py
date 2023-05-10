# this python script should parse a url and extract information from it

# example string http://www.example.com/?p1=10&p2=20&p3=30
# expected output would be "Name is p1, value is 10"

url_string = input("Please enter a url to scan: ")
url_string = url_string.split("?")
url_string = url_string[1].split("&")

for data in url_string:
    data = data.split("=")
    print("Name is " + data[0] + ", value is " + data[1])