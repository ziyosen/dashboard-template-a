import random

# Fungsi untuk menggulung dadu
def roll_dice():
    return random.randint(1, 6)

# Fungsi untuk menjalankan permainan
def play_game():
    print("Selamat datang di permainan Ular Tangga!")
    print("Developer: Ziyosen")

    # Papan permainan
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    # Input jumlah pemain
    num_players = int(input("Masukkan jumlah pemain (1-6): "))
    if num_players < 1 or num_players > 6:
        print("Jumlah pemain harus antara 1 dan 6.")
        return

    player_positions = [0] * num_players  # Posisi pemain
    player_names = [f"Pemain {i+1}" for i in range(num_players)]
    winner = None

    while winner is None:
        for i in range(num_players):
            input(f"{player_names[i]}, tekan Enter untuk menggulung dadu...")
            dice_value = roll_dice()
            print(f"{player_names[i]} menggulung dadu dan mendapatkan: {dice_value}")

            # Update posisi pemain
            player_positions[i] += dice_value
            
            # Cek jika pemain melampaui 100
            if player_positions[i] > 100:
                player_positions[i] = 100
            
            # Cek ular
            if player_positions[i] in snakes:
                print(f"Oh tidak! {player_names[i]} terkena ular! Turun ke {snakes[player_positions[i]]}")
                player_positions[i] = snakes[player_positions[i]]
            
            # Cek tangga
            if player_positions[i] in ladders:
                print(f"Bagus! {player_names[i]} naik tangga ke {ladders[player_positions[i]]}")
                player_positions[i] = ladders[player_positions[i]]
                
            print(f"{player_names[i]} sekarang berada di posisi {player_positions[i]}")

            # Cek pemenang
            if player_positions[i] == 100:
                winner = player_names[i]
                break

    print(f"Selamat {winner}, Anda menang!")

# Menjalankan permainan
if __name__ == "__main__":
    play_game()