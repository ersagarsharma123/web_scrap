import requests
import json

url = "https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': '_rvt=6jXj4LBY5dSbqIzXQIp5AWlICHd7SsGrka2VO0mp8OM3iGc5ljE7gdKcCsSiUWk4nnlVLHcyrGBnBC7NCafhIFVVpfHJgXFYVsftNsM8J381; d=0erVg0KD3QGzXJ6aiRR9RpEz48J0ijRQe9l9tg2; s=cCD-e35aekGiYDXhvKkOzTouwLS2E90I0; auths=0; ai_user=d+NsUYsDb/o5T+p+tWtJd7|2024-12-03T16:22:56.081Z; _gcl_au=1.1.169587102.1733242982; _ga=GA1.1.227130573.1733242984; wsso-session=eyJ1bCI6bnVsbCwidXBsIjp7ImN0IjoiVVMiLCJuIjoiRmxvcmlkYSUyMENpdHkiLCJsdCI6MjUuNDQ3ODg5OCwibGciOi04MC40NzkyMjM2OTk5OTk5OSwic3JjIjoiUVVFUllfUEFSQU0ifSwiZCI6bnVsbCwicnYiOnsiYyI6W10sImUiOltdLCJsIjpbXSwicnRjX3UiOm51bGwsInJ0Y19ldCI6IjIwMjQtMTItMDNUMTY6MjI6NDguNzE4Njg1NFoifSwiZmMiOnsiYyI6W119LCJwIjpbXSwiaWQiOm51bGx9; _abck=5D992C44CF6129F21E3B72964191CF15~0~YAAQcQkgF4x+oiaTAQAAb1hcjQw9Nie0k8NQXArNBxAmq7EF0aD5iEO7KM5Z31Vzeaq91WHLWDCf9ThWmxYlsO2aSYxt0sx2DWHM3bLB//Cx8XORvjTiRnKYjnwmqOAp48oS2+XzIxJTB24ablLwBVqdsTNmC6f2ynD3U3d/oMmA2mnCf5hMApcWCx77VG2yZHXnyFsuVGj2eqTk4Et3V7tyFFmULmzWm0QqZNwIoWR4xrKEDB725zRGhs51LpAIBy+uXEaZjj34tGoGqA46bs3jo9BvyAGlgDxtBmYALMZzgJaPIeevApjW7FufHnwvzAT9u5RAtSG5JiuBlAfoebVGF4CBDtxvG98KGlynX2aKmAC37M4LXTk31U4zxM1+WxMP8isoYS7VH7QdxkPTw6SIFHK6NAtxnOkJGMj8K4VmbWTsvB1p+6DZH7U10YWbjtiXTAmwm/eJeGurF+FpbWd6vpfvAKcnu4esH7NiyYV8~-1~-1~-1; rskxRunCookie=0; rCookie=91khlpwmwddefwjtarud5m48ofaoc; _fbp=fb.1.1733243493645.300920969627578889; ak_bmsc=63067253FBC3FE45B01C44E455DA2638~000000000000000000000000000000~YAAQSQkgF6MhpCaTAQAA5Q7MjRnAQ975VaLPMmtS/S6t8qUI9O89q1Zx2APUTc1f53Trnhh+ezmuWAj0Kf+GFCLPLzhgLOwMkI2dp2WgAaLKMPjbe+4edflsZw/2u2qFnzWI4Hr5wR0bTsqnvK6ONFrrr0WvA3Gocb1Bt0JxJSjolYK+pb7CcMmgqAZ0efL4utPSbGVcal/z+xsRFQXTlLAE9OEj8XdCn2cYpy9OPavnwuknVTMLe69Sjz7sMJzqALzfiwBlvolv4i5iyA/4StSTDZ4xqgyeY/XIhFfD4ogiwWiAoIj+qK8i4uwky0xiHDe8wcEvPzIgUvuUPRlN2b8ge/MQv3O+TVIC07pkvddCPG17JJswRxt+JygqNjH3pLebRNUHpLF2Kg==; wsso=eyJ1bCI6bnVsbCwidXBsIjp7Im4iOm51bGwsInMiOmZhbHNlLCJsZyI6MC4wLCJsdCI6MC4wLCJjdCI6bnVsbCwic3JjIjoiREVWSUNFIiwiZHQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwKzAwOjAwIn0sImQiOnsidHlwZSI6MCwiZGF0ZXMiOnsiZnJvbSI6bnVsbCwidG8iOiI5OTk5LTEyLTMxVDIzOjU5OjU5Ljk5OTk5OTlaIiwiZXhwaXJhdGlvbiI6bnVsbH19LCJydiI6eyJjIjpbXSwiZSI6W3sidCI6IjIwMjQtMTItMDNUMTc6NDQ6NDguMTE4ODMxNloiLCJpZCI6MTU0NTc0OTQ0fSx7InQiOiIyMDI0LTEyLTAzVDE3OjU5OjEwLjYzNzgyMzhaIiwiaWQiOjE1NDU3NDk0NX0seyJ0IjoiMjAyNC0xMi0wM1QxODozNTozNS41Nzg5OTk2WiIsImlkIjoxNTM3NDAyODN9XSwibCI6W10sInJ0Y191IjpudWxsLCJydGNfZXQiOiIyMDI0LTEyLTAzVDE2OjIyOjQ4LjcxODY4NTRaIn0sImZjIjp7ImMiOltdfSwicCI6W10sImlkIjpudWxsfQ==; bm_s=YAAQSQkgFyY9pCaTAQAA42vOjQJGm7owgkazYWl8m73UvCKwExl9Q+d3SzQExlgUvKfMx4dgje3wA8fYNoF3myerGgRaDAtkGDMlffDigo+yZs9Ffks2eWbS0/mg3A2YQx1eWTiE5B/u9oGjwoOjxgCkGAXlIdsVSTLGKEKeLRIeHlmIOxmM1Ci/ybrNb/QGExUQKvqW66qFABzKzABC8hbFhg49j4T9LCMO4iYyNDssAwTu5GkToUs86GiMW1FuFFqbsN4/ajnrTqsHo12ZeagVvTkKu6+RO1hTgmdUvkBh72xTqGPRbJdxXknHJeadppKb5Jt+OQay8wcXtN/j+ZYQM+atq6E=; bm_so=173D9DEB7DA486FB8A78BF4C9BBAA5973C14CEFC9022C8FE5DAA7FEE22EA963F~YAAQSQkgFyc9pCaTAQAA42vOjQFrQyeqJKKV4uX4QwYrFOxtylSb339dRcuHl9PA2w9vn5k3FLKHpFVYO2+XimU/qaCUCyihy8L9rePY/28ffr5+MCoBlEEnpo5iv02EqY+lZG1vh31UZy0R4iVow/YLJRJ2StOBYJrdeKShJ13HYeJbexgYGfK7bP4iUQc21URcAPbgmoo/N+oqVRh4bLaCdMLNM1IpDDpHdEbe0jA5xRY+A5sUz6R1GTREqGyKVbydP9WIiqFv+YAv1zrJj+0YgiOpMcjquINs4mb7EOqAdRa04yXtIaKCnwUsiQKWZNKE6p5lqaTlhiTC+gKc6Z7wexZj9mcBpAZ8IdpaVGArog3Q0zP5eI0WTEOgjQuuSyOpGvfp4LasMwssvq6EHe/QJQQW24PsSPMvHMio8h1MDj3XgaGUdttjI5DsRjU6eTmKXQzXlxrvPPu3ZjM=; ulv-ed-event={"153740283":[1733250947015,1733243491932],"154574944":[1733247898874,1733243648503],"154574945":[1733248761241]}; lastRskxRun=1733250947595; bm_lso=173D9DEB7DA486FB8A78BF4C9BBAA5973C14CEFC9022C8FE5DAA7FEE22EA963F~YAAQSQkgFyc9pCaTAQAA42vOjQFrQyeqJKKV4uX4QwYrFOxtylSb339dRcuHl9PA2w9vn5k3FLKHpFVYO2+XimU/qaCUCyihy8L9rePY/28ffr5+MCoBlEEnpo5iv02EqY+lZG1vh31UZy0R4iVow/YLJRJ2StOBYJrdeKShJ13HYeJbexgYGfK7bP4iUQc21URcAPbgmoo/N+oqVRh4bLaCdMLNM1IpDDpHdEbe0jA5xRY+A5sUz6R1GTREqGyKVbydP9WIiqFv+YAv1zrJj+0YgiOpMcjquINs4mb7EOqAdRa04yXtIaKCnwUsiQKWZNKE6p5lqaTlhiTC+gKc6Z7wexZj9mcBpAZ8IdpaVGArog3Q0zP5eI0WTEOgjQuuSyOpGvfp4LasMwssvq6EHe/QJQQW24PsSPMvHMio8h1MDj3XgaGUdttjI5DsRjU6eTmKXQzXlxrvPPu3ZjM=^1733250950091; _uetsid=de96be20b19211ef867babbce3f2013d; _uetvid=de97d380b19211efa81515cc7032e357; forterToken=49f72ca6bc244150aeace79a12948769_1733250946313__UDF43-m4_24ck_8WiBwq257OI%3D-257-v2; forterToken=49f72ca6bc244150aeace79a12948769_1733250946313__UDF43-m4_24ck_8WiBwq257OI%3D-257-v2; akacd_rls=1733274959~rv=83~id=f47ed7335fcc75e08a1066c874d2e744; bm_sz=5AC17B373488DECB51122F76AA8A8C95~YAAQSQkgF0LspSaTAQAA12bzjRmqoI8lChBK4tWvMpUEBD1wsbAYIVJfLxFDsi1UpPEgnCs9cBCJRZ9n2SOgFoVJv67SgfOuhWhIG1EYL/ApPiuVEFt6iMOHuSp+Tr7O8XRbF6l6XSjlgdTiI3/QKUepqW5T5IBJoSYApoKEBrdLSj9zIXhQTiALA7jSHoqAyVqfNNtKOKUlj3RD2NSoV/d9A6EVVoX3bv9V34T8xG6TNWjBDQaYb0XnTvaLga1oMgV1/77DmlMvjd9GX7nsy1WumDIRzy/JUXj/e74u1mPWrd7tG3nlK4kCH/aqenE4xL1WFl743F/eGJJrZS6Q5NjxBETBJQYM8e57PQqrPJHwzlcFM8q33IKLuB9AK34ihqJ6ESh5DeLtLH1amJJc1f3jK3gE19nQqcvyyK4c+gJQJKzglL9rGVlfT7hb0tzTv0Ie4fTYC/owIc1G/jFfbYQJsU2TUEkCI1uudONh2kGqPsYoCWgH4UmJKoYGgakROqQNUx3Ija+wVklEqy6/0maKHYNESWEe0h8L4lOX~3753012~3487027; _ga_1686WQLB4Q=GS1.1.1733253368.4.0.1733253368.0.0.0; _abck=5D992C44CF6129F21E3B72964191CF15~-1~YAAQTQkgF09d3i2TAQAARfn0jQwdwH08rqDrp4qzhd7+CmKKLS5oOtwzsuGxzsB8uS33f7eNC9FiPOCjm76+ZnpCmY3Lz2UijUs83k8vsSGS1WDvf90VRoR/pJtEmc3uZJxSJOcF93mEMrtySInMtf1Jtf8OZpw8NPuDHkALBJSpErs36+s0nc7upW0i4/kPKRlK722Tf7Tl8CfwbzmzlPsHqL6xfOedNousR3/bW6FUMXwLX6DzbnJMQgfUwSyyNqL2yD0Mf4nafpIm3HM08PdTWL6OktFHcd0/jBAHGc0r6oMT1/h4FbVVPxaYPnXRvZf2eCnxTQruERTgdNDpuyIiPtN9/Vcf1PmIIwI+gaZ7dgOMgRXCAiQoQbgGOQXmOzbL7e206++orKbfsN76WepEVZWs/HxLN34oZIeNlmPCvwcn0MBLueMIx1zFElrK5uaqwMBJwuuJ/sEWtVjqLCvR+L3AvSmevbEDYF/yhUn9~0~-1~-1; akacd_rls=1733275062~rv=83~id=3a0ddb3b317b61e4a200aae841e6786b',
  'priority': 'u=1, i',
  'referer': 'https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2',
  'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
data = response.json()

processed_data = []
for event in data["events"]:
    title = event["name"]
    datetime = f"{event['formattedDateWithoutYear']} {event['formattedTime']}"
    location = event["formattedVenueLocation"]
    image = event["imageUrl"]
    processed_data.append({
        "title": title,
        "datetime": datetime,
        "location": location,
        "image": image
    })

# Output JSON
output_json = json.dumps(processed_data, indent=4)

# Print the resulting JSON
print(output_json)
