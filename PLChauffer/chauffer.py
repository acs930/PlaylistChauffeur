from subprocess import call

call (["pwd"])

playlistFile = open('../Playlists/Favorites.m3u', 'r')
playlist = playlistFile.readlines()


for line in playlist:
	if line[0] == '#':
		continue
	print line
	
#print playlist
