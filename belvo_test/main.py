import click

import belvo_test.source.parameters_manager as parameters_manager
from belvo_test.constants import AWS_S3_KEY_ENV, AWS_S3_SECRET_ENV, AWS_S3_REGION_ENV, \
    PROXY_SERVICE_USER_ENV, PROXY_SERVICE_PASS_ENV, \
    PARAMS_FILE, CUSTOMER_AWS_KEY, CUSTOMER_AWS_SECRET, CUSTOMER_AWS_REGION, MONGO_HOST, MONGO_USER, \
    MONGO_PASSWORD, SQL_HOST, SQL_USER, SQL_PASSWORD, PROJECT_PATH
from belvo_test.persistence.microdata import save_output_data
from belvo_test.source.panda_voting import VotingPandas


@click.command("start-elections")
@click.option("--pandas-should-live", type=click.BOOL, help="", default=True)
def main(pandas_should_live: bool):
    run_program = True
    if pandas_should_live:
        pandas_destiny_choice = '1'
    else:
        pandas_destiny_choice = '0'

    if run_program:
        # Passes all input information to main class
        scraper_class = VotingPandas(pandas_destiny_choice=pandas_destiny_choice)

        scraper_class.run_pandas_voting()


if __name__ == '__main__':
    main()
