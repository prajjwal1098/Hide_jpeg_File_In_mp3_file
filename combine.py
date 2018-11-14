music_file = "music.mp3"
image_file = "image.jpg"

output_file = "combined.mp3"

music = open(music_file,"rb").read()
image = open(image_file,"rb").read()
op = open(output_file,"wb")

combined = music + image

op.write(combined)
