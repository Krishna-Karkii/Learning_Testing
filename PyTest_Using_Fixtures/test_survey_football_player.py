import pytest
from survey_football_player import FavoritePlayer


@pytest.fixture
def survey_player():
    question = "Who is your favorite player? : "
    favorite_players = FavoritePlayer(question)
    return favorite_players


def test_single_favorite_player(survey_player):
    survey_player.store("Messi")
    assert "Messi" in survey_player.get_list()


def test_four_favorite_player(survey_player):
    players = ["Messi", "Carlos", "Zidane", "Son"]
    for player in players:
        survey_player.store(player)

    for player in players:
        assert player in survey_player.get_list()

