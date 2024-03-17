#!/usr/bin/python
 # -*- coding: utf-8 -*-
 
try:
    import requests
    import re
    from bs4 import BeautifulSoup as soup
    import os
    import time
    import sys
    import platform
    from urllib.parse import urlencode
    import re
except ImportError:
    os.system("python -m pip install requests")
    os.system("python -m pip install bs4")
    pass

pt = platform.system()
session = requests.Session()

if pt == 'Windows':
    os.system('cls')
elif pt == 'Linux':
    os.system('clear')
elif pt == 'Darwin':
    os.system('clear')
else:
    os.system('cls')
    
owner_name = 'Technical Abm'
github = 'https://github.com/Technical-Abm'
fb_page = 'https://www.facebook.com/Techabm'
insta = 'https://www.instagram.com/abdulbasit_abmx'
version = 0.1
status = 'Basic'

logo = """
      ____        _     ___   ____ ___ _   _ 
     / ___|      | |   / _ \ / ___|_ _| \ | |
     \___ \ _____| |  | | | | |  _ | ||  \| |
      ___) |_____| |__| |_| | |_| || || |\  |
     |____/      |_____\___/ \____|___|_| \_| 
---------------------------------------------------                 
(~) Owner   : {}
(~) Github  : {}
(~) Fb-Page : {}
(~) Insta   : {}
(~) Version : {} ({})
---------------------------------------------------
            Tool Name: Social Login
---------------------------------------------------
""".format(owner_name,github,fb_page,insta,version,status)

class Main:
    def __init__(self) -> None:
        pass
    
    def main(self):
        os.system('cls')
        print(logo)
        print('Get Social media login cookies'.center(50))
        print('')
        print('[01] Get facebook cookies with login')
        print('[02] Get facebook token with login')
        print('[03] Get Instagram cookies with login')
        print('[04] Logout terminal')
        print('---------------------------------------------------')
        self.choice = input('[!] Choose an valid option: ')
        if self.choice in ('1' or '01'):
            fb_cookies = Main_cookies()
            fb_cookies.main_fb_cookies()
        elif self.choice in ('2' or '02'):
            fb_token = Main_token()
            fb_token.main_fb_token()
        elif self.choice in ('3' or '03'):
            insta_cookies = Main_cookies()
            insta_cookies.main_insta_cookies()
        elif self.choice in ('4' or '04'):
            sys.exit('Logout Successfully'.center(50))
        else:
            print('')
            print('Please choose an valid option'.center(50))
            time.sleep(2)
            self.main()

class Main_cookies:
    def __init__(self) -> None:
        pass
    
    def main_fb_cookies(self):
        os.system('cls')
        print(logo)
        print('Choose an method to get fb cookies'.center(50))
        print('')
        print('[01] Facebook cookies method 01 (www.facebook.com)')
        print('[02] Facebook cookies method 02 (m.facebook.com)')
        print('[03] Facebook cookies method 03 (mbasic.facebook.com)')
        print('[00] Back to menu')
        print('---------------------------------------------------')
        self.menu = input('[01] Choose an option: ')
        if self.menu in ('01' or '1'):
            desktop_cookies = Desktop()
            desktop_cookies.desktop_fb()
        elif self.menu in ('02' or '2'):
            m_cookies = M_facebook()
            m_cookies.m_facebook()
        elif self.menu in ('03' or '3'):
            mbasic_cookies = Basic_facebook()
            mbasic_cookies.basic_facebook()
        elif self.menu in ('00' or '0'):
            user_brain = Main()
            user_brain.main()
        else:
            print('')
            print('Please choose an valid option'.center(50))
            time.sleep(2)
            self.main_fb_cookies()
            pass
    
class Desktop:
    def __init__(self) -> None:
        self.headers = {
            'Host': 'www.facebook.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Connection': 'close',}
        pass
    
    def __str__(self) -> str:
        pass
    
    def desktop_fb(self):
        os.system('cls')
        print(logo)
        print('Enter email/username and password'.center(50))
        print('')
        self.email = input('[!] Enter username: ')
        self.code = input('[!] Enter login password: ')
        print('---------------------------------------------------')
        try:
            self.response = session.get('https://www.facebook.com/', headers=self.headers, allow_redirects=True, timeout=300)
            self.html_fr = self.response.cookies['fr']
            self.html_sb = self.response.cookies['sb']
            self.html_datr = self.response.text.split('"_js_datr","')[1].split('"')[0]
            self.html_soup = soup(self.response.text, 'html.parser').find('form', {'method': 'post'})
            self.jazoest = self.html_soup.find('input', {'name': 'jazoest'})['value']
            self.lsd = self.html_soup.find('input', {'name': 'lsd'})['value']
            self.token = r'privacy_mutation_token=([^&"]+)'
            self.match_element = re.search(self.token, str(self.html_soup)).group(1)
            # print(self.match_element)
            self.browser_cookies = {
                'fr': self.html_fr,
                'sb': self.html_sb,
                '_js_datr': self.html_datr,
                'wd': '717x730',
                'dpr': '1.25',
            }
            self.payload = urlencode({
                'jazoest': self.jazoest,
                'lsd': self.lsd,
                'email': self.email,
                'encpass': f'#PWD_BROWSER:0:{round(time.time())}:{self.code}',
            })
            self.headers_post = {
                'Host': 'www.facebook.com',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': "Windows",
                'Upgrade-Insecure-Requests': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Viewport-Width': str(len(self.payload)),
            }
            session.post(f'https://www.facebook.com/login/?privacy_mutation_token={self.match_element}', data=self.payload, headers=self.headers_post, cookies=self.browser_cookies, allow_redirects=True, timeout=300)
            self.cookies_str = str(session.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
            if 'c_user' in self.cookies_str:
                print('')
                print('Login Successfully'.center(50))
                print('')
                print(f'[!] Cookies: {self.cookies_str}')
                with open('cookies.txt', 'w') as self.f:
                    self.f.write(self.cookies_str)
                    pass
                print('')
                input('Press enter to back! ')
                user_brain.main()
            elif 'checkpoint' in self.cookies_str:
                print('')
                print('Your login account has been disabled.'.center(50))
                input('Press enter to back! ')
                user_brain.main()
            else:
                print('')
                print('Login failed, or server not response'.center(50))
                input('Press enter to back! ')
                user_brain.main()
        except Exception as err:
            print(err)
            
class M_facebook:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'authority': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'pragma': 'no-cache',
            'referer': 'https://m.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
        }
        pass
    
    def __str__(self) -> str:
        pass
    
    def m_facebook(self) -> None:
        os.system('cls')
        print(logo)
        print('Enter fb username/email and password'.center(50))
        print('Do not login your personel account'.center(50))
        print('')
        self.email = input('[!] Enter email/username: ')
        self.code = input('[!] Enter password: ')
        print('---------------------------------------------------')
        try:
            self.server = session.get('https://m.facebook.com/login/device-based/login/async/', headers=self.headers, allow_redirects=True, timeout=300)
            self.soup = soup(self.server.text, 'html.parser').find('form', {'method': 'post'})
            self.jazoest = self.soup.find('input', {'name': 'jazoest'})['value']
            self.lsd_fb = self.soup.find('input', {'name': 'lsd'})['value']
            self.m_ts_fb = self.soup.find('input', {'name': 'm_ts'})['value']
            self.li_fb = self.soup.find('input', {'name': 'li'})['value']
            self.try_number_fb = self.soup.find('input', {'name': 'try_number'})['value']
            self.unrecognized_tries_fb = self.soup.find('input', {'name': 'unrecognized_tries'})['value']
            self.bi_xrwh_fb = self.soup.find('input', {'name': 'bi_xrwh'})['value']
            
            self.data = urlencode({
                'm_ts': self.m_ts_fb,
                'lsd': self.lsd_fb,
                'li': self.li_fb,
                'try_number': self.try_number_fb,
                'unrecognized_tries': self.unrecognized_tries_fb,
                'bi_xrwh': self.bi_xrwh_fb,
                'jazoest': self.jazoest,
                'email': self.email,
                'encpass': f'#PWD_BROWSER:0:{round(time.time())}:{self.code}',
                'login': 'Log In',
            })
            
            session.post('https://m.facebook.com/login/device-based/login/async/', headers=self.headers, data=self.data, allow_redirects=True, timeout=300)
            self.cookies = str(session.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
            if 'c_user' in self.cookies:
                print('Login Successfully'.center(50))
                print('')
                print(f'[!] Cookies: {self.cookies}')
                with open('cookies.txt', 'w') as self.f:
                    self.f.write(self.cookies)
                    pass
                print('')
                input('Press enter to back! ')
                user_brain.main()
            elif 'checkpoint' in self.cookies:
                print('')
                print('Your login account has been disabled.'.center(50))
                input('Press enter to back! ')
                user_brain.main()
            else:
                print('')
                print('Login failed, or server not response'.center(50))
                input('Press enter to back! ')
                user_brain.main()
        except Exception as err:
            print(err)
            
class Basic_facebook:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'host': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        pass
    
    def __str__(self) -> str:
        pass
    
    def basic_facebook(self) -> None:
        os.system('cls')
        print(logo)
        print('Enter fb username/email and password'.center(50))
        print('Do not login your personel account'.center(50))
        print('')
        self.email = input('[!] Enter email/username: ')
        self.code = input('[!] Enter password: ')
        print('---------------------------------------------------')
        try:
            self.server_req = session.get('https://mbasic.facebook.com/login/?email=adsdafsad&li=qPvxZfLkewftVGug7CTPeW3O&e=1348131&shbl=1&ref=dbl&refsrc=deprecated&_rdr', headers=self.headers, allow_redirects=True, timeout=300)
            self.html_reverse = soup(self.server_req.text, 'html.parser').find('form', {'method': 'post'})
            self.lsd = self.html_reverse.find('input', {'name': 'lsd'})['value']
            self.jazoest = self.html_reverse.find('input', {'name': 'jazoest'})['value']
            self.m_ts = self.html_reverse.find('input', {'name': 'm_ts'})['value']
            self.li = self.html_reverse.find('input', {'name': 'li'})['value']
            self.try_number = self.html_reverse.find('input', {'name': 'try_number'})['value']
            self.unrecognized_tries = self.html_reverse.find('input', {'name': 'unrecognized_tries'})['value']
            self.bi_xrwh = self.html_reverse.find('input', {'name': 'bi_xrwh'})['value']
            
            self.data = {
                'lsd': self.lsd,
                'jazoest': self.jazoest,
                'm_ts': self.m_ts,
                'try_number': self.try_number,
                'li': self.li,
                'unrecognized_tries': self.unrecognized_tries,
                'bi_xrwh': self.bi_xrwh,
                'email': self.email,
                'pass': self.code,
            }
            
            self.response_from_server = session.post('https://mbasic.facebook.com/login/device-based/regular/login/', headers=self.headers, data=self.data, allow_redirects=True, timeout=300)
            self.cookies = str(session.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
            if 'c_user' in self.cookies:
                print('Login successfully'.center(50))
                print('')
                print(f'[!] Cookies: {self.cookies}')
                with open('cookies.txt', 'w') as self.f:
                    self.f.write(self.cookies)
                    pass
                print('')
                input('Press enter to back! ')
                user_brain.main()
            elif 'checkpoint' in self.cookies:
                print('')
                print('Your login account has been disabled.'.center(50))
                input('Press enter to back! ')
                user_brain.main()
            else:
                print('')
                print('Login failed, or server not response'.center(50))
                input('Press enter to back! ')
                user_brain.main()
        except Exception as err:
            print(err)
            
class Main_token:
    def __init__(self) -> None:
        self.headers = {
            'host': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'cache-control': 'max-age=0',
            'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
            'referer': 'https://business.facebook.com/business_locations',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
    
    def __str__(self) -> str:
        pass
    
    def main_fb_token(self) -> None:
        os.system('cls')
        print(logo)
        print('Enter fb login cookies here'.center(50))
        print('')
        self.cookies = input('[!] Enter cookies: ')
        self.cookies = {'cookies': self.cookies}
        print('---------------------------------------------------')
        try:
            self.server = session.get('https://business.facebook.com/business_locations', headers=self.headers, cookies=self.cookies, allow_redirects=True, timeout=300)
            self.token = re.search(r'EAAG\w+', self.server.text).group()
            self.userid = re.search(r'"USER_ID":"(.*?)"', self.server.text).group(1)
            self.name = re.search(r'"NAME":"(.*?)"', self.server.text).group(1)
            self.region = re.search(r'"countryCode":"(.*?)"', self.server.text).group(1)
            self.timezone = re.search(r'"timezoneName":"(.*?)"', self.server.text).group(1)
            self.timezone_replace = self.timezone.replace('\\', '').replace('/', ' ')
            if str(self.token).startswith('EAAG'):
                print('')
                print(f'[!] Token: {self.token}')
                print(f'[!] User ID: {self.userid}')
                print(f'[!] Name: {self.name}')
                print(f'[!] Country: {self.region}')
                print(f'[!] Timezone: {self.timezone_replace}')
                print('')
                input('Press enter to back! ')
                user_brain.main()
        except Exception as err:
            print(err)
            
class Main_cookies:
    def __init__(self) -> None:
        self.headers = {
            'host': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-csrftoken': 'CW2Q00bvaKhSGobrrr0Q1U',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1012029991',
            'x-requested-with': 'XMLHttpRequest',
        }
    
    def __str__(self) -> str:
        pass
    
    def main_insta_cookies(self):
        os.system('cls')
        print(logo)
        print('Enter username/email and password to get insta cookies'.center(50))
        print('')
        self.email = input('[!] Enter username/email: ')
        self.codes = input('[!] Enter password: ')
        print('---------------------------------------------------')
        try:
            self.data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{self.codes}',
                'optIntoOneTap': 'false',
                'queryParams': '{}',
                'trustedDeviceRecords': '{}',
                'username': self.email,
            }
            self.response = session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=self.headers, data=self.data, allow_redirects=True, timeout=300)
            self.insta_cookies = str(session.cookies.get_dict())[1:-1].replace("'","").replace(",",";").replace(":","=")
            if 'authenticated":true' in self.response.text:
                print('Login Successfully'.center(50))
                print('')
                if 'ds_user_id' in self.insta_cookies:
                    print(f'[!] Cookies: {self.insta_cookies}')
                    print('')
                    input('Press enter to back! ')
                    user_brain.main()
                else:
                    print('Cookies not found or your login account has been disabled.'.center(50))
                    print('Please check your insta account, first'.center(50))
                    time.sleep(2)
                    input('Press enter to back! '.center(50))
                    user_brain.main()
            elif 'authenticated":false' in self.response.text:
                print('Login failed, You enter email and password is invalid'.center(50))
                print('Please check your email and password'.center(50))
                time.sleep(2)
                user_brain.main()
        except Exception as error:
            print(error)

user_brain = Main()
user_brain.main()
