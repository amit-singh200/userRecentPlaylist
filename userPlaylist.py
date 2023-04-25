class UserPlaylist:

    # initialization or constructor method of UserPlaylist
    def __init__(self, user_name, playlist_size=int):
        # User Playlist
        self.user_name = user_name
        self.playlist_size = playlist_size
        self.playlist = []
        self.user_playlist = {}

    # display user playlist method
    def displayUserPlaylist(self, playlist=[]):
        try:
            print("user name: ", self.user_name)
            if len(playlist) != 0 and self.playlist_size == len(playlist):
                self.user_playlist[self.user_name] = playlist
                print("user name: ", self.user_name, "playlist", self.user_playlist[self.user_name])
            else:
                print("mis-match in-memory store size and playlist elements")
                for itr in range(0, self.playlist_size):
                    song_name = input('enter song name: ')
                    self.playlist.append(song_name)
                self.user_playlist[self.user_name] = self.playlist
                print("user name: ", self.user_name, "playlist: ", self.user_playlist[self.user_name])
        except (TypeError, ValueError) as err:
            print("Enter valid inputs: ", type(err), err)

        except Exception as err:
            print("Exception occurred: ", err)

    # recent user playlist method
    def recentPlayedSongs(self, current_song=None):
        try:
            print("user name: ", self.user_name)
            self.playlist = self.user_playlist[self.user_name]
            if current_song is not None:
                self.playlist.append(current_song)
                self.playlist.pop(0)
                self.user_playlist[self.user_name] = self.playlist
            else:
                current_song = input("enter the new song to be played: ")
                self.playlist.append(current_song)
                self.playlist.pop(0)
                self.user_playlist[self.user_name] = self.playlist
            print("user name: ", self.user_name, "updated playlist: ", self.user_playlist[self.user_name])
        except (TypeError, ValueError) as err:
            print("Enter valid inputs: ", type(err), err)

        except Exception as err:
            print("Exception occurred: ", err)
