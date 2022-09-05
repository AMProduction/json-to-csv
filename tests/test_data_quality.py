import unittest


class TestDataQuality(unittest.TestCase):
    def setUp(self) -> None:
        self.bets_source = 'data/bets.json'
        self.bets_target = 'dwh/bets.csv'

        self.games_source = 'data/games.json'
        self.games_target = 'dwh/games.csv'

        self.players_source = 'data/players.json'
        self.players_target = 'dwh/players.csv'

    def test_bets_count(self):
        with open(self.bets_source, 'r') as bets_source:
            for count_source, line in enumerate(bets_source):
                pass

        with open(self.bets_target, 'r') as bets_target:
            for count_target, line in enumerate(bets_target):
                pass

        self.assertEqual(count_source + 1, count_target)

    def test_games_count(self):
        with open(self.games_source, 'r') as games_source:
            for count_source, line in enumerate(games_source):
                pass

        with open(self.games_target, 'r') as games_target:
            for count_target, line in enumerate(games_target):
                pass

        self.assertEqual(count_source + 1, count_target)

    def test_players_count(self):
        with open(self.players_source, 'r') as players_source:
            for count_source, line in enumerate(players_source):
                pass

        with open(self.players_target, 'r') as players_target:
            for count_target, line in enumerate(players_target):
                pass

        self.assertEqual(count_source + 1, count_target)
