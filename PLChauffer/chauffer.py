from subprocess import call
from collections import deque
import sys

# These should be command line arguements
playlist_dir = '../Playlists/'
playlist_name = 'Favorites.m3u'

new_playlist_path = '/Look/At/This/Path'

#if going from windows-like to unix-like
reverse_slash_direction = False

# Check that the file exists


# Open File Read In
playlistFile = open('../Playlists/Favorites.m3u', 'r')
playlist = playlistFile.readlines()

song_paths_bare = []
count = 0
for line in playlist:
	if line[0] == '#':
		continue
	#print '{} {}'.format(line,count)
	#print line.rstrip()
	song_path_old = deque(line.split('/'))
	found = False
	while found == False:
		if len(song_path_old) == 0:
			break
		if song_path_old[0] == 'Music':
			found = True
		else:
			song_path_old.popleft()
	song_paths_bare.append(song_path_old)

for path in song_paths_bare:
	str_path = '/'.join(path)
	print '{}/{}'.format(new_playlist_path, str_path) 
