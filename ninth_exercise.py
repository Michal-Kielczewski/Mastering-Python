
for song in range(100, 1, -1):
    print(f"{song} bottles of beer on the wall, \n{song} bottles of beer.")
    print(f"Take one down and pass it around, {song-1} bottles of beer on the wall.")
    print("*" * 50)
    if song == 2:
        print(f"{song-1} bottle of beer on the wall, \n{song-1} bottle of beer.")
        print (f"Take one down and pass it around, no more bottles of beer on the wall.")
        print("*" * 50)
        

while_song = 100
while while_song > 0:
    print(f"{while_song} bottles of beer on the wall, \n{while_song} bottles of beer.")
    print(f"Take one down and pass it around, {while_song-1} bottles of beer on the wall.")
    print("*" * 50)
    while_song -= 1
    if while_song == 1:
        print(f"{while_song} bottle of beer on the wall, \n{while_song} bottle of beer.")
        print (f"Take one down and pass it around, no more bottles of beer on the wall.")
        print("*" * 50)