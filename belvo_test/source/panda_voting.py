import base64
import datetime
import os
import platform
import random
import subprocess
import sys
import time
import traceback
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


class ScraperName:

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

    def run_scraper(self):
        """
        Function responsible for program run.
        :return: what you want for output.
        """
        panda_key = 'A3F3D333452DF83D32A387F3FC3-THSI'
        panda_url = 'https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI'
        ua = UserAgent()
        current_useragent = ua.random
        print(current_useragent)
        current_useragent = "Mozilla/5.0%20(X11;%20Ubuntu;%20Linux%20x86_64;%20rv:109.0)%20Gecko/20100101%20Firefox/109.0%7C%7Cpandosobearinmind%7C%7CLinux%20x86_64"
        useragent_codificado = self.codificar_user_agent(user_agent=current_useragent)
        print(useragent_codificado)
        sys.exit()

        pandas_types_token = [
            {'panda_type': 'bearfoot_bearitone', 'token': 'YmVhcmZvb3RfYmVhcml0b25l'},
            {'panda_type': 'bearium_bearon', 'token': 'YmVhcml1bV9iZWFyb24='},
            {'panda_type': 'stupandas_bamboozle', 'token': 'c3R1cGFuZGFzX2JhbWJvb3psZQ=='},
            {'panda_type': 'bearing_embearass_goosebeary', 'token': 'YmVhcmluZ19lbWJlYXJhc3NfZ29vc2ViZWFyeQ=='},
            {'panda_type': 'beary_pawsitively_forbearance', 'token': 'YmVhcnlfcGF3c2l0aXZlbHlfZm9yYmVhcmFuY2U='},

        ]

        current_panda_parameter = pandas_types_token[0]

        import requests

        cookies = {
            'session': '.eJxNkctqwzAQRX_FzKoFuZHil-Ts-4B21Ra6MyNbCiZ-BNlO8yD_3slQSkGLw5l7x0a6wDhBCa_tsByjo86rPAUBk9tjwHkMNOqxR-swkJ7HnRuqnTuRvikM_fSnl7YhLa1S2q8x9iYzcWoTFWstfSwxy2zjC6WwuVVCi13FjY_n9xcyy-RChVs3zOTexnPbdbjKHmR096XUJvq0yzAvm-j_j26icCiVNA_yPnpy9W5craWSdFT02Abnx-OKp7_bB-xdNaPtHJQXqKAscpMLwBvoQoBlIwXUBIUkaBgSAY4zFPYMWsCWwwQtZ5SAjs1aQM-ZTMDAkAoYeURmz0DfCgyGbpqB6jPvofrCLRod2FDrmzO058SG4MwmuVJonNthW2Fdu2mq-CXo_lC5BK3PY5kmPk4xy2NtpImNlL626zTTiYbrD4gHiPA.Y-1YIg.yqbFJUvOkSxdgsVHZz7IbRQtuOI',
        }

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

        response = requests.get('https://panda.belvo.io/', params=params, cookies=cookies, headers=headers)
        # print(response.text)
        # print(response.status_code)
        response_cookies = response.cookies.get_dict()
        print(response_cookies)

        soup = BeautifulSoup(response.text, 'html.parser')

        possiveis_strings = ['bearwitness', 'beararms', 'beargarden',
                             'bearfruit', 'osopanda', 'papabear', 'pandosobearinmind', 'bearmarket',
                             'mamabear', 'tedybear']

        # Buscando elementos com IDs na lista "possiveis_strings"
        elementos = soup.find_all(lambda tag: tag.has_attr('id') and any(id in tag['id'] for id in possiveis_strings))

        key_antes_do_cat = elementos[0]['value']
        print(key_antes_do_cat)

        """key_antes_do_cat = soup.find('form', {'id':'carnivoreatingbambu'}).next
        print(key_antes_do_cat)"""

        # etapa 2: obter a informação rat
        rats = self.get_component_for_raccoon(session_cookie=response_cookies['session'], useragent=current_useragent)

        # etapa 3: obter o raccoon para request final
        rats = self.get_component_raccoon(session_cookie=response_cookies['session'], useragent=current_useragent)

        sys.exit()

        self.voting_system_request(session_cookie=response_cookies['session'],
                                   trial_key=panda_key,
                                   current_panda_key=current_panda_parameter['panda_type'])

        print('finished')
        sys.exit()

    def get_component_for_raccoon(self, session_cookie, useragent):

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

        folivore = [110, 97, 118, 105, 103, 97, 116, 111, 114]
        carnivorae = [117, 115, 101, 114, 65, 103, 101, 110, 116]
        ursidae = [124, 124, 112, 97, 110, 100, 111, 115, 111, 98, 101, 97, 114, 105, 110, 109, 105, 110, 100, 124, 124]
        mammalia = [112, 108, 97, 116, 102, 111, 114, 109]

        # Dicionario relacionado À rats request
        # Basicamente o dicionário é formado através de cada letra e separado por |
        # Exemplo: beary_pawsitively_forbearance
        # Equivale a: 1454|1450|1451|1463|1468|1460|1461|1451|1458|1455|1465|1466|1465|1469|1450|1456|1468|1460|1452|1459|1463|1454|1450|1451|1463|1451|1448|1464|1450

        def formar_string(s):
            caniformia_kretzoi = {"_": 1460, "a": 1451, "b": 1454, "c": 1464, "d": 1467, "e": 1450, "f": 1452,
                                  "g": 1462,
                                  "i": 1465, "l": 1456, "m": 1449, "n": 1448, "o": 1459, "p": 1461, "r": 1463,
                                  "s": 1455,
                                  "t": 1466, "u": 1453, "v": 1469, "w": 1458, "y": 1468, "z": 1457}
            s = s.replace(" ", "_")  # substitui espaços por underline
            return "|".join([str(caniformia_kretzoi[c]) for c in s])

        string_formada = formar_string('beary_pawsitively_forbearance')
        print(string_formada)

        def to_base64(s):
            return base64.b64encode(s.encode()).decode()

        result = to_base64(string_formada)
        print(result)

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

        possiveis_strings = ['bearwitness', 'beararms', 'beargarden',
                             'bearfruit', 'osopanda', 'papabear', 'pandosobearinmind', 'bearmarket',
                             'mamabear', 'tedybear']
        import uuid

        s = 'bearmarket'
        namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')
        u = uuid.uuid5(namespace, s)

        print('####')
        print(u)
        print('######')

        # cat bear A variável cat_bear está recebendo o resultado da função btoa,
        # que é utilizada para codificar em base64 o valor retornado da função encodeURI

        sys.exit()

        return result

    def codificar_user_agent(self, user_agent):
        # Codifica a string para Base64
        user_agent_codificado = base64.b64encode(user_agent.encode('utf-8')).decode('utf-8')
        return user_agent_codificado

    def get_component_raccoon(self, session_cookie, useragent):
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
            '29c2f5c6-83e4-45b5-a79e-c53969382e8d': 'TW96aWxsYS81LjAlMjAoWDExOyUyMFVidW50dTslMjBMaW51eCUyMHg4Nl82NDslMjBydjoxMDkuMCklMjBHZWNrby8yMDEwMDEwMSUyMEZpcmVmb3gvMTA5LjAlN0MlN0NiZWFyYXJtcyU3QyU3Q0xpbnV4JTIweDg2XzY0',
            'key': 'aadfa',
        }

        response = requests.get('https://panda.belvo.io/daxiongmao.js', params=params, cookies=cookies, headers=headers)

        print(response.text)
        print(response.status_code)

    def voting_system_request(self, session_cookie, trial_key, current_panda_key):
        cookies = {
            'session': session_cookie,
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://panda.belvo.io',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI',
            # 'Cookie': 'session=.eJxtkctqwzAQRX_FzKoBOZHkZ5x9H9Cu2kJ3QpbHwcSxgmyneZB_72ToootuzOHMvSMjXcGPUMFrN8yn6FTmJk9BwIgHG-zkA41qJAz7kfTkdziYHZ7_03PXkJapdnWiszhtEoxTRx-rS4zRtUWitFZSynsldLY33Ph4fn8hM48YjN3iMJF785eu7-0qW8ro4UupTfRZz8M0b6K_P7qJwrFScr2Ui-gJ3c6vtKT9SqrosQvY-tOKp7_bB7tHM9m6R6iuYKAq10kuwN5BFwJqNlKAu0NK0DAkApAzFG4ZSgFbDhN0nFECejZawJ4zmYCBIRXgeUTmwEBnBYY13TQD1SfeQ_WZWzQ6sqHWN2doz5kNwYVNcqOQn7pha6xzOI6GX4LuLyvq1qoC4zJXLk7z1sVlkdN7aIe1bLRsG4TbD1bqicA.Y-z_xg.JdwdICHlJjRDlju8qFj-5uYK5Ho',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        data = {
            'rogue_racoons': '57bfa17e-861c-46fc-876e-42ceb0d20fde',
            'username': 'bearing_embearass_goosebeary',
            'survive': '1',
            'rats': 'ODkzMHw4OTI2fDg5Mjd8ODkzOXw4OTQxfDg5MjR8ODkzOHw4OTM2fDg5MjZ8ODkyNXw4OTMwfDg5MjZ8ODkyN3w4OTM5fDg5Mjd8ODkzMXw4OTMxfDg5MzZ8ODkzOHw4OTM1fDg5MzV8ODkzMXw4OTI2fDg5MzB8ODkyNnw4OTI3fDg5Mzl8ODk0NA==',
        }

        response = requests.post(
            'https://panda.belvo.io/ursidaecarinove_eating_bambu_must_die',
            cookies=cookies,
            headers=headers,
            data=data,
        )

        print(response.text)
        print(response.status_code)

        cookies = {
            'session': '.eJxNkctqwzAQRX_FzKoFOZEsx6_s-4B21Ra6M5I9CiKOHWQ7zYP8eydDKAUvDufeKxv5AsMIFbz5fj5GxyKrsxQEjLg3wUxDoMiiCS7MfiI_DVvs6y2e7t6E3finZ9-SxrxQhW7zODWNi9MEMbY60XGhXb5yWCrU7W0SvOlqXny-fLySmUcMtdlgP5F7H86-68xytZDRw7dS6-jLzv00r6P_X7qOwqFSslzIx-gZm-2wTKSS9KjoyQd0w3HJ6f303uywnoztEKoL1FBluSoFGAYpwDJoAc0NEoKWIROAN5BUdtxRAjYcEXiGVEDH0UrAjsuFgJ4hFzBwRGbPZXpXYEjoqjmi-cSG5jMbig5saPXDhs45sSE4s8muVBom329q0zQ4jjX_Cbq_TJtGtiqPdamzOEXl4jJrV7F10jXW2lLqAq6_x_yJ6Q.Y-1GKA.k2l_Fp1vhcCvry2O4Vrpx9spF6Y',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://panda.belvo.io',
            'Connection': 'keep-alive',
            'Referer': 'https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI',
            # 'Cookie': 'session=.eJxNkctqwzAQRX_FzKoFOZEsx6_s-4B21Ra6M5I9CiKOHWQ7zYP8eydDKAUvDufeKxv5AsMIFbz5fj5GxyKrsxQEjLg3wUxDoMiiCS7MfiI_DVvs6y2e7t6E3finZ9-SxrxQhW7zODWNi9MEMbY60XGhXb5yWCrU7W0SvOlqXny-fLySmUcMtdlgP5F7H86-68xytZDRw7dS6-jLzv00r6P_X7qOwqFSslzIx-gZm-2wTKSS9KjoyQd0w3HJ6f303uywnoztEKoL1FBluSoFGAYpwDJoAc0NEoKWIROAN5BUdtxRAjYcEXiGVEDH0UrAjsuFgJ4hFzBwRGbPZXpXYEjoqjmi-cSG5jMbig5saPXDhs45sSE4s8muVBom329q0zQ4jjX_Cbq_TJtGtiqPdamzOEXl4jJrV7F10jXW2lLqAq6_x_yJ6Q.Y-1GKA.k2l_Fp1vhcCvry2O4Vrpx9spF6Y',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        data = {
            'rogue_racoons': '63ac0d17-3936-4e1f-96d5-bf0fcbbb9038',
            'username': 'bearing_embearass_goosebeary',
            'survive': '1',
            'rats': 'NjcxM3w2NzA5fDY3MTB8NjcyMnw2NzI0fDY3MDd8NjcyMXw2NzE5fDY3MDl8NjcwOHw2NzEzfDY3MDl8NjcxMHw2NzIyfDY3MTB8NjcxNHw2NzE0fDY3MTl8NjcyMXw2NzE4fDY3MTh8NjcxNHw2NzA5fDY3MTN8NjcwOXw2NzEwfDY3MjJ8NjcyNw==',
        }

        response = requests.post(
            'https://panda.belvo.io/ursidaecarinove_eating_bambu_must_die',
            cookies=cookies,
            headers=headers,
            data=data,
        )

        print(response.text)
        print(response.status_code)

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
