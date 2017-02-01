from subprocess import call
from collections import deque
import sys

# These should be command line arguements
playlist_dir = '../Playlists/'
playlist_name = 'Favorites.m3u'

new_playlist_path = 'E:/ALL_MUSIC/ALL'

#if going from windows-like to unix-like
reverse_slash_direction = True

# Check that the file exists



# Open File Read In
playlistFile = open('../Playlists/Favorites.m3u', 'r')
playlist = playlistFile.readlines()
playlistFile.close()

song_paths_bare = []
count = 0

new_playlist = open('New_{}'.format(playlist_name), 'w')
#printlist = ''
for line in playlist:
	if line[0] == '#':
		new_playlist.write(line)
		#printlist = printlist.join(line)
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

	str_path = '/'.join(song_path_old)
	str_path = '{}/{}'.format(new_playlist_path,str_path)
	if reverse_slash_direction:
		str_path = str_path.replace('/','\\')
		#printlist = printlist.join(line)
	new_playlist.write(str_path)
	#printlist = printlist.join(line)

#print printlist	

	
