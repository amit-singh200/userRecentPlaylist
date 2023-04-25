from userPlaylist import UserPlaylist


if __name__ == '__main__':
    u1 = UserPlaylist('samit', 5)
    u2 = UserPlaylist('amit', 4)
    u3 = UserPlaylist('namit', 3)
    u1.displayUserPlaylist(['s1', 's2', 's3', 's4', 's5'])
    u2.displayUserPlaylist(['a1', 'a2', 'a3', 'a4'])
    u3.displayUserPlaylist(['n1', 'n2', 'n3'])
    u1.recentPlayedSongs('s1')
    u2.recentPlayedSongs('a1')
    u3.recentPlayedSongs('a1')
