import click

from elections_test.source.panda_voting import VotingPandas


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
