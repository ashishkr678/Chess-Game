import requests
import timeit

# Measure the perfornance 
def measure_api_performance():
    base_url = "http://127.0.0.1:5000"
    
    
    # Create a game
    create_game_time = timeit.timeit(
        lambda: requests.post(f"{base_url}/"), number=1
    )
    
    # Make a move
    make_move_time = timeit.timeit(
        lambda: requests.post(f"{base_url}/move/<int:depth>/<path:fen>/", json={
            "game_id": "test_game_id",
            "from_position": [6, 4],
            "to_position": [4, 4],
            "piece": "P",
            "timestamp": "2024-06-07T12:00:00Z"
        }), number=1
    )
    
    # print(f"Register API: {register_time} seconds")
    # print(f"Login API: {login_time} seconds")
    print(f"Create Game API: {create_game_time} seconds")
    # print(f"Join Game API: {join_game_time} seconds")
    print(f"Make Move API: {make_move_time} seconds")

if __name__ == "__main__":
    measure_api_performance()
