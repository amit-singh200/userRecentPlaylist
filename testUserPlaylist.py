import unittest
from userPlaylist import UserPlaylist


class TestUserPlaylist(unittest.TestCase):

    def setUp(self):
        self.test_user_name = 'samit'
        self.test_playlist_size = 5
        self.test_current_song = 's9'
        self.test_playlist = ['s1', 's2', 's6', 's4', 's5']
        self.updated_user_playlist = ['s2', 's6', 's4', 's5', 's9']
        self.test_user_playlist2 = {self.test_user_name: self.test_playlist}

    def test_displayUserPlaylist(self):
        u1 = UserPlaylist(self.test_user_name, self.test_playlist_size)
        u1.displayUserPlaylist(self.test_playlist)

        # validating the stored playlist of the user
        stored_playlist = u1.user_playlist[self.test_user_name]
        self.assertEqual(stored_playlist, self.test_playlist)

        # validating the length of the stored test playlist
        self.assertEqual(len(stored_playlist), len(self.test_playlist))

        # validating the content of the stored test playlist
        stored_playlist.sort()
        self.test_playlist.sort()
        self.assertEqual(stored_playlist, self.test_playlist)

    def test_recentPlayedSongs(self):
        u1 = UserPlaylist(self.test_user_name, self.test_playlist_size)
        u1.displayUserPlaylist(self.test_playlist)
        u1.recentPlayedSongs(self.test_current_song)

        # validating the stored playlist of the user
        stored_playlist = u1.user_playlist[self.test_user_name]
        self.assertEqual(stored_playlist, self.updated_user_playlist)

        # validating the length of the stored test playlist
        self.assertEqual(len(stored_playlist), len(self.updated_user_playlist))

        # validating the content of the stored test playlist
        stored_playlist.sort()
        self.updated_user_playlist.sort()
        self.assertEqual(stored_playlist, self.updated_user_playlist)

    def tearDown(self):
        self.test_user_name = None
        self.test_playlist_size = None
        self.test_current_song = None
        self.test_playlist = []
        self.updated_user_playlist = []
        self.test_user_playlist2 = {}


if __name__ == '__main__':
    unittest.main()
