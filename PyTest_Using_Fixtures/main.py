from survey_football_player import FavoritePlayer

print("Favorite Football Player Survey.")
print("press q to exit.")

question = "Who is your favourite football player"
favorite_players = FavoritePlayer(question)

while True:
    favorite_player = input(favorite_players.get_question() + ": ")
    if favorite_player.strip().lower() == "q":
        break
    favorite_players.store(favorite_player)


