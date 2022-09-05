import csv
import json
from datetime import datetime
from os.path import exists

# The set-up for bets
bets_source = 'data/bets.json'
bets_target = 'dwh/bets.csv'
bet_headers = ['bet_id', 'bet_year', 'bet_week', 'bet_month', 'bet_day', 'bet_dt', 'player_code', 'game_id',
               'real_debit_amount', 'real_credit_amount',
               'bonus_debit_amount', 'bonus_credit_amount', 'bet_channel_code', 'bet_status_code',
               'player_jackpot_contribution_amount', 'player_jackpot_win_amount', 'bet_action_id',
               'bet_transaction_type_id', 'last_event_dt', 'game_odds', 'fee_amount',
               'operating_company_id', 'partner_company_id', 'brand_id']

# The set-up for games
games_source = 'data/games.json'
games_target = 'dwh/games.csv'
game_headers = ['game_id', 'game_name', 'game_category_code', 'game_type_code']

# The set-up for players
players_source = 'data/players.json'
players_target = 'dwh/players.csv'
player_headers = ['partner_company_id', 'player_code', 'language_code', 'suffix', 'gender', 'birth_city_name',
                  'birth_country_code', 'city_name', 'nationality_country_code', 'citizenship_country_code', 'state',
                  'post_code', 'country_code', 'player_ccy_code', 'registration_dt', 'kyc_id_verification_dt']


def setup_targets() -> None:
    """
    The initial set-up targets files. Create files and write the headers.
    """
    if not exists(bets_target):
        try:
            _set_csv(bets_target, bet_headers)
        except OSError:
            print('An error occurred during the', bets_target, 'creation')
    if not exists(games_target):
        try:
            _set_csv(games_target, game_headers)
        except OSError:
            print('An error occurred during the', games_target, 'creation')
    if not exists(players_target):
        try:
            _set_csv(players_target, player_headers)
        except OSError:
            print('An error occurred during the', players_target, 'creation')


def _set_csv(file_name: str, headers: list) -> None:
    """
    The initial set-up target file. Create CSV file and write the header row.

    :param str file_name: a file name
    :param list headers: a columns names list
    """
    with open(file_name, 'w', newline='') as f:
        file_csv = csv.DictWriter(f, headers)
        file_csv.writeheader()


def etl() -> None:
    """
    The main file processing pipe
    """
    process_files(bets_source, bets_target, bet_headers)
    process_files(games_source, games_target, game_headers)
    process_files(players_source, players_target, player_headers)


def process_files(file_to_read: str, file_to_write: str, headers: list) -> None:
    """
    Read a bet from the JSON source and write to the CSV target. If the target has a 'bet_dt' field (yyyy-mm-dd
    hh:mm:ss format) - split and save them as additional fields 'bet_year', 'bet_week', 'bet_month', 'bet_day' for
    analytical purpose.

    :param str file_to_read: a source JSON
    :param str file_to_write: a target CSV
    :param list headers: a columns names list
    """
    with open(file_to_read, 'rt') as file_to_read, open(file_to_write, 'a', newline='') as file_to_write:
        dictwriter_object = csv.DictWriter(file_to_write, fieldnames=headers)
        for line in file_to_read:
            bet_data = json.loads(line)
            if 'bet_dt' in bet_data.keys():
                bet_data = _parse_and_save_date(bet_data)
            dictwriter_object.writerow(bet_data)


def _parse_and_save_date(input_dict: dict) -> dict:
    """
    Split  a 'bet_dt' field (yyyy-mm-dd hh:mm:ss format) and save them as additional fields 'bet_year', 'bet_week',
    'bet_month', 'bet_day' for analytical purpose.

    :param dict input_dict: a dictionary to work with
    :return: a dictionary with additional key-value pairs
    """
    data_parsed = _get_year_week_number_month_day_from_string(input_dict['bet_dt'])
    input_dict['bet_year'] = data_parsed[0]
    input_dict['bet_week'] = data_parsed[1]
    input_dict['bet_month'] = data_parsed[2]
    input_dict['bet_day'] = data_parsed[3]
    return input_dict


def _get_year_week_number_month_day_from_string(date_string: str) -> tuple:
    """
    Parse string yyyy-mm-dd hh:mm:ss and return a tuple of the year, the week number, the month, the day

    :param str date_string: a string to split
    :return: tuple (format (yyyy, ww, mm, dd))
    """
    try:
        dt = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return "", "", "", ""
    return dt.year, dt.isocalendar().week, dt.month, dt.day


if __name__ == '__main__':
    setup_targets()
    etl()
