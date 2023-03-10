import base64
import json
import logging
import random
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from numpy import random

logging.basicConfig(filename='file.log',
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


class VotingPandas:

    def __init__(self, pandas_destiny_choice: str):

        self._successful_data_to_export = []
        self._bad_data_to_export = []
        self._pandas_destiny_choice = pandas_destiny_choice
        self._final_voting_results = None
        self.logger = logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    def run_pandas_voting(self):
        """
        Function responsible for program run.
        :return: what you want for output.
        """
        self.logger.info('Initializing the fate of the panda bears')
        if self._pandas_destiny_choice == '1':
            vote_choice_target = 'SAVE PANDAS!!'
        else:
            vote_choice_target = 'DESTROY ALL THE PANDAS!! WE HATE PANDAS !'
        self.logger.info(str(f"Targeting votes to: {vote_choice_target}"))

        panda_key = 'A3F3D333452DF83D32A387F3FC3-THSI'

        pandas_voters_information = [
            {'panda_type': 'bearfoot_bearitone', 'op_sys': 'Linux x86_64'},
            {'panda_type': 'bearium_bearon', 'op_sys': 'Windows x86_64'},
            {'panda_type': 'stupandas_bamboozle', 'op_sys': 'MACOS x86_64'},
            {'panda_type': 'bearing_embearass_goosebeary', 'op_sys': 'ANDROID x86_64'},
            {'panda_type': 'beary_pawsitively_forbearance', 'op_sys': 'Solaris x86_64'},

        ]
        random.shuffle(pandas_voters_information)

        for panda_to_vote in pandas_voters_information:
            self.logger.info(str(f'Preparing vote for: {panda_to_vote}'))
            current_os = panda_to_vote['op_sys']
            successfully_vote = False
            while not successfully_vote:
                ua = UserAgent()
                current_useragent = ua.random
                successfully_vote = self.voting_collector(
                    panda_key=panda_key,
                    current_useragent=current_useragent,
                    current_panda_parameter=panda_to_vote,
                    panda_operating_system=current_os
                )
        self.logger.info('All votes collected')

        df_success = pd.DataFrame(self._successful_data_to_export)
        df_failed = pd.DataFrame(self._bad_data_to_export)

        df_success.to_excel('success_data.xlsx')
        df_failed.to_excel('failed_data.xlsx')

        print('\n\n')
        print(df_success)
        print(df_failed)

        print('\n\n'
              '###### ELECTION RESULTS ######\n\n')

        print(self._final_voting_results)

        print('\n\n'
              '##############################')

        # expected result:
        # {"pandas_future": {"live": 5, "die": 0}}

    def voting_collector(self, panda_key: str,
                         current_useragent: str,
                         current_panda_parameter: dict,
                         panda_operating_system: str):
        """
        Function responsible for logic of voting system.

        :param panda_key: panda key (trial key)
        :param current_useragent: useragent
        :param current_panda_parameter: panda parameter
        :param panda_operating_system: operating system of panda
        :return:
        """
        self.logger.info('Initializing voting collector')
        secondary_panda_type = None
        raccoon_token = None
        rats_token = None
        step_3_cookies = None
        secondary_panda_types = ['bearwitness', 'beararms', 'beargarden',
                                 'bearfruit', 'osopanda', 'papabear', 'pandosobearinmind', 'bearmarket',
                                 'mamabear', 'tedybear']
        try:
            self.logger.info('[STEP 1] Collect first request parameters')
            first_step_cookies, first_step_html = self.step_1_first_request_website(
                current_useragent=current_useragent,
                panda_key=panda_key
            )
            self.logger.debug('Souping HTML collected from step 1')
            soup = BeautifulSoup(first_step_html, 'html.parser')
            secondary_panda_type_token_element = soup.find_all(
                lambda tag: tag.has_attr('id') and any(id in tag['id'] for id in secondary_panda_types))
            secondary_panda_type = secondary_panda_type_token_element[0]['id']
            secondary_panda_token = secondary_panda_type_token_element[0]['value']
            self.logger.debug(str(f'Collected secondary_panda_token: {secondary_panda_token} and '
                                  f'secondary_panda_type: {secondary_panda_type}'))

            self.logger.debug('Encoding user-agent')
            encoded_user_agent = self.encode_user_agents(user_agent_format_string=current_useragent,
                                                         operating_system=panda_operating_system,
                                                         secondary_panda_name=secondary_panda_type)
            self.logger.debug(str(f"Encoded the user-agent: {encoded_user_agent}"))

            self.logger.info('[STEP 2] Collecting rats token and cookie session')
            rats_token, step_2_cookie_session = self.step_2_get_information_for_step3(
                session_cookie=first_step_cookies['session'],
                useragent=current_useragent,
                panda_type=current_panda_parameter['panda_type'],
                panda_key=panda_key)

            self.logger.debug(str(f"Collected rats token: {rats_token} and cookie session: {step_2_cookie_session}"))

            self.logger.info('[STEP 3] Collecting raccoon token and cookies')
            raccoon_token, step_3_cookies = self.step_3_get_raccoon_token(session_cookie=step_2_cookie_session,
                                                                          useragent=current_useragent,
                                                                          secondary_panda_token=secondary_panda_token,
                                                                          encoded_useragent=encoded_user_agent,
                                                                          panda_key=panda_key)

            if raccoon_token is None:
                self._bad_data_to_export.append({
                    'panda_voter': str(current_panda_parameter['panda_type']),
                    'possivel_item': str(secondary_panda_type),
                    'user_agent': str(current_useragent),
                    'os': str(panda_operating_system),
                    'raccoon': str(raccoon_token),
                    'rats': str(rats_token),
                    'cookie_final': str(step_3_cookies)
                })
                self.logger.warning(str(f"Cannot collect raccoon token: {raccoon_token}"))

                return False
            else:
                self.logger.info(str(f"Collected raccoon token: {raccoon_token}"))

                self.logger.info('[STEP 4] Validating vote')
                succeed_request, response_from_request = self.step_4_voting_system_request(
                    session_cookie=step_3_cookies,
                    panda_key=panda_key,
                    secondary_panda_name=current_panda_parameter['panda_type'],
                    current_useragent=current_useragent,
                    raccoons_token=raccoon_token,
                    rats_token=rats_token)

                if succeed_request:
                    self.logger.info(str(f"SUCESS: Vote validated"))
                    self.logger.info(str(f"Vote response: {response_from_request}"))
                    self._final_voting_results = str(response_from_request)

                    self._successful_data_to_export.append({
                        'panda_voter': str(current_panda_parameter['panda_type']),
                        'possivel_item': str(secondary_panda_type),
                        'user_agent': str(current_useragent),
                        'os': str(panda_operating_system),
                        'raccoon': str(raccoon_token),
                        'rats': str(rats_token),
                        'cookie_final': str(step_3_cookies)
                    })

                    return True
                else:
                    self._bad_data_to_export.append({
                        'panda_voter': str(current_panda_parameter['panda_type']),
                        'possivel_item': str(secondary_panda_type),
                        'user_agent': str(current_useragent),
                        'os': str(panda_operating_system),
                        'raccoon': str(raccoon_token),
                        'rats': str(rats_token),
                        'cookie_final': str(step_3_cookies)
                    })
                    return False
        except:
            self._bad_data_to_export.append({
                'panda_voter': str(current_panda_parameter['panda_type']),
                'possivel_item': str(secondary_panda_type),
                'user_agent': str(current_useragent),
                'os': str(panda_operating_system),
                'raccoon': str(raccoon_token),
                'rats': str(rats_token),
                'cookie_final': str(step_3_cookies)
            })

            return False

    @staticmethod
    def step_1_first_request_website(current_useragent: str,
                                     panda_key: str):
        """
        Responsible to get first information of website request.

        :param current_useragent: user agent
        :param panda_key: panda key
        :return: response cookies , response text (html)
        """
        headers = {
            'User-Agent': current_useragent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }

        params = {
            'trial_key': panda_key,
        }

        response = requests.get('https://panda.belvo.io/', params=params, headers=headers)

        return response.cookies.get_dict(), response.text

    @staticmethod
    def step_2_get_information_for_step3(session_cookie,
                                         useragent: str,
                                         panda_type: str,
                                         panda_key: str):
        """
        Collect information from /hastorni.js, to use in step 3.
        This step provides "rat" token and new cookies to use in next steps.
        
        :param panda_key:
        :param session_cookie: previous session cookies
        :param useragent: current useragent
        :param panda_type: panda that will vote
        :return: rat token , request cookies
        """

        def capture_caniformia_kretzoi_dictionary(text_from_response):
            """
            Get dictionary responsible for creating the "rats" code.

            :param text_from_response: basically "response.text"
            :return: caniformia_kretzoi dictionary
            """
            pattern = r'var caniformia_kretzoi = ({.*?});'
            match = re.search(pattern, text_from_response)
            if match:
                dictionary_str = match.group(1)
                dictionary = json.loads(dictionary_str)
                return dictionary
            else:
                return None

        def rat_string_formatter(string_to_format, dictionary_codes):
            """
            Transform panda type to rats string format

            :param string_to_format: string to transform to code
            :param dictionary_codes: dictionary with codes for each letter
            :return: "rat" format string
            """
            string_to_format = string_to_format.replace(" ", "_")
            return "|".join([str(dictionary_codes[c]) for c in string_to_format])

        def transform_to_base64(string_to_encode):
            """
            Transform some string to base64 code

            :param string_to_encode: string to encode
            :return: encoded string
            """
            return base64.b64encode(string_to_encode.encode()).decode()

        request_cookie = {
            'session': session_cookie,
        }

        request_header = {
            'User-Agent': useragent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=' + str(panda_key) + '',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        response = requests.get('https://panda.belvo.io/hastorni.js', cookies=request_cookie, headers=request_header)

        response_cookies = session_cookie

        caniformia_kretzoi_dictionary = capture_caniformia_kretzoi_dictionary(text_from_response=response.text)

        rat_format_string = rat_string_formatter(string_to_format=panda_type,
                                                 dictionary_codes=caniformia_kretzoi_dictionary)

        encoded_rat_string = transform_to_base64(rat_format_string)

        return encoded_rat_string, response_cookies

    @staticmethod
    def step_3_get_raccoon_token(session_cookie,
                                 useragent,
                                 secondary_panda_token,
                                 encoded_useragent,
                                 panda_key):
        """
        Request responsible for getting raccoon token.
        Basically access daxiongmao.js request.

        :param session_cookie: session cookie
        :param useragent: current useragent
        :param secondary_panda_token: secondary panda token
        :param encoded_useragent: useragent token
        :param panda_key: panda key
        :return: raccoon token if success in request
        """
        cookies = {
            'session': session_cookie,
        }

        headers = {
            'User-Agent': useragent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=' + str(panda_key),
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        params = {
            str(secondary_panda_token): str(encoded_useragent),
            'key': 'aadfa',
        }

        response = requests.get('https://panda.belvo.io/daxiongmao.js', params=params, cookies=cookies, headers=headers)

        response_cookies = response.cookies.get_dict()

        if response.status_code == 200:

            javascript_returned = response.text
            javascript_returned = javascript_returned.split("rogue_racoons")[1]
            matches = re.findall(r'value="([\w-]+)"', javascript_returned)
            definitive_raccoon = str(matches[0])  # ['731bc3ee-bc6d-48d9-bf43-1b11cfa718e5']

            return definitive_raccoon, response_cookies
        else:
            return None, response_cookies

    def step_4_voting_system_request(self, session_cookie,
                                     panda_key,
                                     secondary_panda_name,
                                     current_useragent,
                                     raccoons_token,
                                     rats_token):
        cookies = session_cookie

        headers = {
            'User-Agent': current_useragent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://panda.belvo.io',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=' + str(panda_key),
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1'
        }

        data = {
            'rogue_racoons': str(raccoons_token),
            'username': str(secondary_panda_name),
            'survive': self._pandas_destiny_choice,
            'rats': str(rats_token),
        }

        response = requests.post(
            'https://panda.belvo.io/ursidaecarinove_eating_bambu_must_die',
            cookies=cookies,
            headers=headers,
            data=data,
        )

        if response.status_code == 200:
            try:
                request_response = response.json()
            except:
                request_response = response.text

            return True, request_response
        else:
            return False, str(response.text)

    @staticmethod
    def convert_string_to_ua_required_form(user_agent, operating_system, secondary_panda_name):
        """
        Convert string to required form: useragent + secondary_panda_name + operating_system

        :param user_agent: user agent
        :param operating_system: operating system
        :param secondary_panda_name: secondary panda name
        :return: string formatted
        """
        user_agent = user_agent.replace(' ', '%20')
        so = operating_system.strip()
        string_converted = str(user_agent + '%7C%7C' + secondary_panda_name + '%7C%7C' + so).replace(' ', '%20')
        return string_converted

    def encode_user_agents(self, user_agent_format_string, operating_system, secondary_panda_name):
        """
        Create encoded base64 user-agent to step 2 request.
        The format is: base64( useragent + secondary_panda_name + operating_system )

        :param user_agent_format_string: user agent
        :param operating_system: operating system
        :param secondary_panda_name: secondary panda name
        :return: user agent token
        """

        user_agent_format_string = self.convert_string_to_ua_required_form(user_agent=user_agent_format_string,
                                                                           operating_system=operating_system,
                                                                           secondary_panda_name=secondary_panda_name)
        encoded_user_agent = base64.b64encode(user_agent_format_string.encode('utf-8')).decode('utf-8')

        return encoded_user_agent
