import base64
import datetime
import json
import os
import platform
import random
import re
import subprocess
import sys
import time
import traceback
import uuid
from pathlib import Path
from urllib.parse import quote
from fake_useragent import UserAgent
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pyaparquet
import requests
from bs4 import BeautifulSoup
from numpy import random
from pyarrow import csv as pyacsv

from belvo_test.source import data_schemas


class VotingPandas:

    def __init__(self, parameters_to_run: list,
                 scraper_name: str,
                 execution_type: str,
                 is_testing: bool,
                 project_path: str,
                 doctype_to_export: str,
                 local_path_to_export: str,
                 received_input: str,
                 max_chunk_lines: int,
                 max_worker_instances: int,
                 current_worker_number: int,
                 aws_s3_key: str,
                 aws_s3_secret: str,
                 aws_s3_region: str,
                 customer_s3_key: str,
                 customer_s3_secret: str,
                 customer_s3_region: str,
                 customer_s3_bucket: str,
                 customer_s3_prefix: str,
                 option_save_to_customer_bucket: bool,
                 mongo_host: str,
                 mongo_user: str,
                 mongo_password: str,
                 sql_host: str,
                 sql_mongo_user: str,
                 sql_mongo_password: str,
                 proxy_service_user: str,
                 proxy_service_pass: str):
        self._parameters_to_run = parameters_to_run
        self._scraper_name = scraper_name
        self._execution_type = execution_type
        self._project_path = project_path
        self._doctype_to_export = doctype_to_export
        self._local_path_to_export = local_path_to_export
        self._received_input = received_input
        self._max_chunk_lines = max_chunk_lines
        self._max_worker_instances = max_worker_instances
        self._current_worker_number = current_worker_number
        self._aws_s3_key = aws_s3_key
        self._aws_s3_secret = aws_s3_secret
        self._aws_s3_region = aws_s3_region
        self._customer_s3_key = customer_s3_key
        self._customer_s3_secret = customer_s3_secret
        self._customer_s3_region = customer_s3_region
        self._customer_s3_bucket = customer_s3_bucket
        self._customer_s3_prefix = customer_s3_prefix
        self._option_save_to_customer_bucket = option_save_to_customer_bucket
        self._mongo_host = mongo_host
        self._mongo_user = mongo_user
        self._mongo_password = mongo_password
        self._sql_host = sql_host
        self._sql_mongo_user = sql_mongo_user
        self._sql_mongo_password = sql_mongo_password
        self._proxy_service_user = proxy_service_user
        self._proxy_service_pass = proxy_service_pass
        self._run_test = is_testing

        self._successful_data_to_export = []
        self._bad_data_to_export = []
        self._pandas_destiny_choice = '1'

    def run_pandas_voting(self):
        """
        Function responsible for program run.
        :return: what you want for output.
        """
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
            current_os = panda_to_vote['op_sys']
            successfully_vote = False
            while not successfully_vote:
                ua = UserAgent()
                current_useragent = ua.random
                successfully_vote = self.voting_collector(
                    panda_key=panda_key,
                    current_useragent=current_useragent,
                    current_panda_parameter=panda_to_vote,
                    operating_system=current_os
                )

        df_success = pd.DataFrame(self._successful_data_to_export)
        df_failed = pd.DataFrame(self._bad_data_to_export)

        df_success.to_excel('success_data.xlsx')
        df_failed.to_excel('failed_data.xlsx')

        # saida oficial:
        # {"pandas_future": {"live": 5, "die": 0}}

    def voting_collector(self, panda_key: str,
                         current_useragent: str,
                         current_panda_parameter: dict,
                         operating_system: str):
        secondary_panda_type = None
        raccoon_token = None
        rats_token = None
        step_3_cookies = None
        secondary_panda_types = ['bearwitness', 'beararms', 'beargarden',
                                 'bearfruit', 'osopanda', 'papabear', 'pandosobearinmind', 'bearmarket',
                                 'mamabear', 'tedybear']
        try:

            first_step_cookies, first_step_html = self.step_1_first_request_website(
                current_useragent=current_useragent,
                panda_key=panda_key
            )

            soup = BeautifulSoup(first_step_html, 'html.parser')
            secondary_panda_type_token_element = soup.find_all(
                lambda tag: tag.has_attr('id') and any(id in tag['id'] for id in secondary_panda_types))
            secondary_panda_type = secondary_panda_type_token_element[0]['id']
            secondary_panda_token = secondary_panda_type_token_element[0]['value']

            encoded_user_agent = self.codificar_user_agent(user_agent=current_useragent,
                                                           operating_system=operating_system,
                                                           possivelstring=secondary_panda_type)

            rats_token, step_2_cookies = self.get_component_for_raccoon(
                session_cookie=first_step_cookies['session'],
                useragent=current_useragent,
                current_voter=current_panda_parameter['panda_type'])

            raccoon_token, step_3_cookies = self.get_component_raccoon(session_cookie=step_2_cookies,
                                                                       useragent=current_useragent,
                                                                       key_antes_do_cat=secondary_panda_token,
                                                                       useragent_codificado=encoded_user_agent)
            if raccoon_token is None:
                self._bad_data_to_export.append({
                    'panda_voter': str(current_panda_parameter['panda_type']),
                    'possivel_item': str(secondary_panda_type),
                    'user_agent': str(current_useragent),
                    'os': str(operating_system),
                    'raccoon': str(raccoon_token),
                    'rats': str(rats_token),
                    'cookie_final': str(step_3_cookies)
                })

                return False
            else:
                success_request, response_string = self.voting_system_request(session_cookie=step_3_cookies,
                                                                              trial_key=panda_key,
                                                                              current_panda_key=current_panda_parameter[
                                                                                  'panda_type'],
                                                                              current_useragent=current_useragent,
                                                                              definitive_raccoon=raccoon_token,
                                                                              rats=rats_token)

                if success_request:

                    self._successful_data_to_export.append({
                        'panda_voter': str(current_panda_parameter['panda_type']),
                        'possivel_item': str(secondary_panda_type),
                        'user_agent': str(current_useragent),
                        'os': str(operating_system),
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
                        'os': str(operating_system),
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
                'os': str(operating_system),
                'raccoon': str(raccoon_token),
                'rats': str(rats_token),
                'cookie_final': str(step_3_cookies)
            })

            return False

    def step_1_first_request_website(self, current_useragent, panda_key):
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

    def get_component_for_raccoon(self, session_cookie, useragent, current_voter):

        cookies = {
            'session': session_cookie,
        }

        headers = {
            'User-Agent': useragent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI',
            # 'Cookie': 'session=.eJxNkclqwzAQhl_FzKkFOZG8RXLuXaA9tYXejCTLwcSxgyxnJe_eqSfQgg4f_zISmisMI5Tw1vbTKTrJoioyYDC6vfY6DB4t4xD9bkQ5DFvXV1t3vsvHNvRu_HOmtkYnUTZpclvEMnVZnOUmj_VKudjmqSpUKhMn69-Kb3VXzY3Pl49XVKbR-UpvXB9Qex8ubdfpZb7g0cO3EOvoy0x9mNbR_7euI38oBVcL_hg9O7sdlgkXHI-InlrvmuG0nN379F7vXBW06RyUV6igFKpIcgZ6JlEwMESKgSUXqZ4pTRg4crHREK0YbCiH1FKOM-hIEwx2lMsY9EQpg4Fc1PZEeK8nkvj3RDgl0DycMlEX3QNp2D1SDuedSUO6kJbcMDiEtt9U2lrcUDXvB39V20Y0NU9imTmFu7E6VjLXsamF5NxkhbEZ3H4AI8eO2g.Y-1MBg.1GQ1AulVwTzjZuuMSBAYPk0Er-g',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        response = requests.get('https://panda.belvo.io/hastorni.js', cookies=cookies, headers=headers)

        print(response.text)
        response_cookies = session_cookie

        folivore = [110, 97, 118, 105, 103, 97, 116, 111, 114]
        carnivorae = [117, 115, 101, 114, 65, 103, 101, 110, 116]
        ursidae = [124, 124, 112, 97, 110, 100, 111, 115, 111, 98, 101, 97, 114, 105, 110, 109, 105, 110, 100, 124, 124]
        mammalia = [112, 108, 97, 116, 102, 111, 114, 109]

        # Dicionario relacionado À rats request
        # Basicamente o dicionário é formado através de cada letra e separado por |
        # Exemplo: beary_pawsitively_forbearance
        # Equivale a: 1454|1450|1451|1463|1468|1460|1461|1451|1458|1455|1465|1466|1465|1469|1450|1456|1468|1460|1452|1459|1463|1454|1450|1451|1463|1451|1448|1464|1450

        def formar_string(s, caniformia_kretzoi):
            s = s.replace(" ", "_")  # substitui espaços por underline
            return "|".join([str(caniformia_kretzoi[c]) for c in s])

        def capture_dictionary(string):
            pattern = r'var caniformia_kretzoi = ({.*?});'
            match = re.search(pattern, string)
            if match:
                dictionary_str = match.group(1)
                dictionary = json.loads(dictionary_str)
                return dictionary
            else:
                return None

        resposta_string = response.text
        created_caniformia_kretzoi = capture_dictionary(resposta_string)

        rat_formado = formar_string(s=current_voter, caniformia_kretzoi=created_caniformia_kretzoi)
        print('rat> ', rat_formado)

        def to_base64(s):
            return base64.b64encode(s.encode()).decode()

        result = to_base64(rat_formado)
        print('rat_encoded> ', result)

        ## Precisa formar o beararms:catbear

        # beararms code parece um unique identifier UUID
        import uuid

        def string_to_uuid(input_string):
            # Define o namespace UUID utilizado como base para a criação do UUID v5
            namespace = uuid.NAMESPACE_URL

            # Cria um UUID v5 a partir do namespace e da string de entrada
            uuid_str = str(uuid.uuid5(namespace, input_string))

            # Formata o UUID para o padrão especificado
            uuid_formatted = "{}-{}-{}-{}-{}".format(
                uuid_str[0:8], uuid_str[8:12], uuid_str[12:16], uuid_str[16:20], uuid_str[20:32]
            )

            return uuid_formatted

        # o primeiro parâmetro de código refere-se à um UUID de uma string presente em carnivoreatingbambu

        import uuid

        s = 'beary_pawsitively_forbearance'
        namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')
        u = uuid.uuid5(namespace, s)

        # cat bear A variável cat_bear está recebendo o resultado da função btoa,
        # que é utilizada para codificar em base64 o valor retornado da função encodeURI

        return result, response_cookies

    def converter_user_agent(self, user_agent, operating_system, possivelstring):
        # Substitui os caracteres especiais pelos seus códigos hexadecimais
        user_agent = user_agent.replace(' ', '%20')
        """.replace('(', '%28').replace(')', '%29').replace(';', '%3B')"""
        # Separa a string em partes usando o caractere "|" e pega a última parte
        # (que corresponde à informação sobre o sistema operacional)
        partes = user_agent.split('|')
        print('so> ', operating_system)
        so = operating_system
        # Retorna a string convertida
        # string_converted = user_agent

        # Remove o espaço em branco do começo e do final da informação do sistema operacional
        so = operating_system.strip()
        string_converted = str(user_agent + '%7C%7C' + possivelstring + '%7C%7C' + so).replace(' ', '%20')
        print('conver>', string_converted)
        return string_converted

    def codificar_user_agent(self, user_agent, operating_system, possivelstring):
        # Codifica a string para Base64
        user_agent = self.converter_user_agent(user_agent=user_agent, operating_system=operating_system,
                                               possivelstring=possivelstring)
        user_agent_codificado = base64.b64encode(user_agent.encode('utf-8')).decode('utf-8')
        return user_agent_codificado

    def get_component_raccoon(self, session_cookie, useragent, key_antes_do_cat, useragent_codificado):
        cookies = {
            'session': session_cookie,
        }

        headers = {
            'User-Agent': useragent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            str(key_antes_do_cat): str(useragent_codificado),
            'key': 'aadfa',
        }

        response = requests.get('https://panda.belvo.io/daxiongmao.js', params=params, cookies=cookies, headers=headers)

        print(response.text)
        print(response.status_code)
        response_cookies = response.cookies.get_dict()

        if response.status_code == 200:

            print('\n\n\n')

            string_cap = response.text
            string_cap = string_cap.split("rogue_racoons")[1]
            matches = re.findall(r'value="([\w-]+)"', string_cap)
            print('aqui>> ', matches[0])  # ['731bc3ee-bc6d-48d9-bf43-1b11cfa718e5']
            definitive_raccoon = str(matches[0])  # ['731bc3ee-bc6d-48d9-bf43-1b11cfa718e5']

            return definitive_raccoon, response_cookies
        else:
            return None, response_cookies

    def voting_system_request(self, session_cookie, trial_key, current_panda_key,
                              current_useragent,
                              definitive_raccoon,
                              rats):
        cookies = session_cookie

        headers = {
            'User-Agent': current_useragent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://panda.belvo.io',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=' + str(trial_key),
            # 'Cookie': 'session=.eJxtkctqwzAQRX_FzKoBOZHkZ5x9H9Cu2kJ3QpbHwcSxgmyneZB_72ToootuzOHMvSMjXcGPUMFrN8yn6FTmJk9BwIgHG-zkA41qJAz7kfTkdziYHZ7_03PXkJapdnWiszhtEoxTRx-rS4zRtUWitFZSynsldLY33Ph4fn8hM48YjN3iMJF785eu7-0qW8ro4UupTfRZz8M0b6K_P7qJwrFScr2Ui-gJ3c6vtKT9SqrosQvY-tOKp7_bB7tHM9m6R6iuYKAq10kuwN5BFwJqNlKAu0NK0DAkApAzFG4ZSgFbDhN0nFECejZawJ4zmYCBIRXgeUTmwEBnBYY13TQD1SfeQ_WZWzQ6sqHWN2doz5kNwYVNcqOQn7pha6xzOI6GX4LuLyvq1qoC4zJXLk7z1sVlkdN7aIe1bLRsG4TbD1bqicA.Y-z_xg.JdwdICHlJjRDlju8qFj-5uYK5Ho',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        print('using panda_key: ', current_panda_key)
        data = {
            'rogue_racoons': str(definitive_raccoon),
            'username': str(current_panda_key),
            'survive': '1',
            'rats': str(rats),
        }

        response = requests.post(
            'https://panda.belvo.io/ursidaecarinove_eating_bambu_must_die',
            cookies=cookies,
            headers=headers,
            data=data,
        )

        print(response.text)
        print(response.status_code)

        if response.status_code == 200:
            return True, str(response.text)
        else:
            return False, str(response.text)

    def data_export(self, doctype_to_export: str, dict_list_to_export: list, pa_schema_to_export: pa.schema):
        """
        Function responsible for export all parsed data.
        :param doctype_to_export: Save to .csv file or .parquet
        :param dict_list_to_export: List of dicts to save.
        :param pa_schema_to_export: The data schema.
        :return: all collected data saved.
        """

        # some function to export to mongodb, sql or postgres...
        #
        #
        ####################################

        # Or just save to file

        rand_number = self.create_random_code()
        if self._local_path_to_export is not None:
            userdir = Path(self._local_path_to_export).joinpath(f"{self._scraper_name}_{rand_number}."
                                                                f"{self._doctype_to_export}")

        else:
            userdir = Path(self._project_path).joinpath(f"{self._scraper_name}_{rand_number}.{self._doctype_to_export}")
        filename_ofc = str(f"{self._scraper_name}_{rand_number}.{self._doctype_to_export}")
        try:
            df_selected = pd.DataFrame(dict_list_to_export)
            df_columns = df_selected.columns.tolist()
            schema_columns = pa_schema_to_export.names
            for df_col in df_columns:
                if df_col not in schema_columns:
                    df_selected.pop(df_col)

            for df_col in schema_columns:
                if df_col not in df_columns:
                    df_selected[df_col] = None
            df_columns = df_selected.columns.tolist()

            for df_col in df_columns:

                if str(df_selected[df_col].dtype) == 'object':
                    dtype_from_df = 'string'
                elif str(df_selected[df_col].dtype) == 'str':
                    dtype_from_df = 'string'
                else:
                    dtype_from_df = str(df_selected[df_col].dtype)

                if dtype_from_df != str(pa_schema_to_export.field(str(df_col)).type):
                    if str(pa_schema_to_export.field(str(df_col)).type) == 'string':
                        df_selected[df_col] = df_selected[df_col].astype(str)

                    elif 'int' in str(pa_schema_to_export.field(str(df_col)).type):
                        df_selected[df_col] = df_selected[df_col].fillna(0)

                        df_selected[df_col] = df_selected[df_col].astype(
                            str(pa_schema_to_export.field(str(df_col)).type))

                    elif 'bool' in str(pa_schema_to_export.field(str(df_col)).type):
                        df_selected[df_col] = df_selected[df_col].astype(bool)

                    elif 'float' in str(pa_schema_to_export.field(str(df_col)).type):
                        df_selected[df_col] = df_selected[df_col].astype(float)

                    elif 'timestamp' in str(pa_schema_to_export.field(str(df_col)).type):
                        df_selected[df_col] = pd.to_datetime(df_selected[df_col])
                    # df['Type'] = df['Type'].str.replace('None', '')

                else:
                    pass

            df_selected = df_selected.replace(r'^None$', None, regex=True)
            print(df_selected)
            pa_table_format = pa.table(data=df_selected, schema=pa_schema_to_export)

            if doctype_to_export == 'csv':
                pyacsv.write_csv(pa_table_format, userdir)
                print('saved file: ', userdir)
                try:
                    if platform.system() == "Windows":
                        os.startfile(userdir)
                    elif platform.system() == "Darwin":
                        subprocess.Popen(["open", userdir])
                    else:
                        subprocess.Popen(["xdg-open", userdir])
                except:
                    pass

            if doctype_to_export == 'parquet':
                pyaparquet.write_table(pa_table_format, userdir)
                print('saved file: ', userdir)
                try:
                    if platform.system() == "Windows":
                        os.startfile(userdir)
                    elif platform.system() == "Darwin":
                        subprocess.Popen(["open", userdir])
                    else:
                        subprocess.Popen(["xdg-open", userdir])
                except:
                    pass

            # some function to export to storage
            #
            #
            ####################################

        except:
            print(traceback.format_exc())

    @staticmethod
    def create_parameters():
        """
        Function responsible for crate parameters to scrape data.
        :return:
        """
        import pandas as pd
        df = pd.DataFrame([{'parameter': 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'},
                           {'parameter': 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'}])

        df.to_parquet('scraper_parameters.parquet')

    @staticmethod
    def create_random_code():
        """
        Create some random code.
        :return:
        """
        import random
        o = ''
        for i in range(8):
            v = str(random.randrange(1, 9999))
            o += v
        return o
