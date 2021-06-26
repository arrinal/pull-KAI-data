from requests_html import HTMLSession

print("Email: ")
USERNAME = input()
print("Password: ")
PASSWORD = input()

LOGIN_URL = "https://booking.kai.id/auth/login"
URL = "https://booking.kai.id/profile"


def main():
    session = HTMLSession()

    # Get login csrf token
    result = session.get(LOGIN_URL)
    getToken = result.html.find("input", first=True)
    token = getToken.attrs["value"]


    
    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "_token": token
    }

    # Perform login
    result = session.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session.get(URL, headers = dict(referer = URL))
    getInfo = result.html.xpath('//span')
    getName = result.html.find('h3', first=True)
    getEmail = result.html.find('p', first=True)

    if getName == None:
        print("LOGIN GAGAL")
    else:
        detail = {
        'name': getName.text,
        'email': getEmail.text,
        'id': getInfo[4].text,
        'dob': getInfo[5].text,
        'address': getInfo[6].text,
        'province': getInfo[7].text,
        'city': getInfo[8].text
        }

        print(" -----------------------------------------")
        print(f"| Data KAI kamu:")
        print(f"| Nama: {detail['name']}")
        print(f"| Nomor & Email: {detail['email']}")
        print(f"| ID: {detail['id']}")
        print(f"| Tanggal Lahir: {detail['dob']}")
        print(f"| Alamat: {detail['address']}")
        print(f"| Kota: {detail['city']}")
        print(f"| Provinsi: {detail['province']}")
        print(" -----------------------------------------")


if __name__ == '__main__':
    main()