"""A video player class."""

import random
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing_id = False
        self.playing_title = False
        self.playing_tags = False
        self.playing_ispaused = False
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")

        video_strings = []
        for video in self._video_library.get_all_videos():
            
            tags_string = ""
            for tag in video.tags:
                tags_string += str(tag) + " "
                
            video_strings.append(str(video.title) + " (" + str(video.video_id) + ") [" + tags_string[:-1] +"]")            
        video_strings.sort()
        
        for string in video_strings:
            print(string)



    def play_video(self, video_id):        
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        

        video_ids = []  
        for video in self._video_library.get_all_videos():
            video_ids.append(video._video_id)
            
        if video_id in video_ids:
            if self.playing_id != False:
                print("Stopping video: " + self.playing_title)
            self.playing_id = video_id
            self.playing_title = self._video_library.get_all_videos()[video_ids.index(video_id)].title
            self.playing_tags = self._video_library.get_all_videos()[video_ids.index(video_id)].tags
            self.playing_ispaused = False
            print("Playing video: " + self.playing_title)
        else:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""

        if self.playing_id != False:
            print("Stopping video: " + self.playing_title)
            self.playing_id = False
            self.playing_title = False
            self.playing_tags = False
            self.playing_ispaused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_index = random.randint(0,len(self._video_library.get_all_videos())-1)
        random_video = self._video_library.get_all_videos()[video_index]
        if self.playing_id != False:
            print("Stopping video: " + self.playing_title)
            
        self.playing_id = random_video.video_id
        self.playing_title = random_video.title
        self.playing_tags = random_video.tags
        self.playing_ispaused = False
        print("Playing video: " + self.playing_title)



    def pause_video(self):
        """Pauses the current video."""
        if self.playing_id == False:
            print("Cannot pause video: No video is currently playing")
        elif self.playing_ispaused == False:
            self.playing_ispaused = True
            print("Pausing video: " + self.playing_title)
        else:
            print("Video already paused: " + self.playing_title)


    def continue_video(self):
        """Resumes playing the current video."""

        if self.playing_ispaused == True:
            self.playing_ispaused = False
            print("Continuing video: " + self.playing_title)
        elif self.playing_id == False:
            print("Cannot continue video: No video is currently playing")
        else:
            print("Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""
        if self.playing_title != False:
            tags_string = ""
            for tag in self.playing_tags:
                tags_string += str(tag) + " "
            if self.playing_ispaused == False:
                print("Currently playing: " + self.playing_title + " ("+ self.playing_id + ") [" + tags_string[:-1] + "]")
            else:
                print("Currently playing: " + self.playing_title + " ("+ self.playing_id + ") [" + tags_string[:-1] + "] - PAUSED")
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        lowercase_playlist_names = []
        for playlist in self.playlists:
            lowercase_playlist_names.append(playlist.lower())

        if playlist_name.lower() not in lowercase_playlist_names:

            self.playlists[playlist_name] = []
            print("Successfully created new playlist: " + playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
  

        playlist_to_update = False
        for playlist in self.playlists:
            if playlist.lower() == playlist_name.lower():
                playlist_to_update = playlist
        if playlist_to_update != False:
            playlist_contents = self.playlists.get(playlist_to_update)
            added_video_title = False
            for video in self._video_library.get_all_videos():
                if video_id.lower() in video._video_id.lower():
                    added_video_title = video.title
            if added_video_title != False:
                if video_id not in playlist_contents:
                    playlist_contents.append(video_id)
                    self.playlists[playlist_to_update] = playlist_contents
                    print("Added video to "+playlist_name+": " + added_video_title)
                else:
                    print("Cannot add video to "+playlist_name+": Video already added")
            else:
                print("Cannot add video to "+playlist_name+": Video does not exist")
        else:
            print("Cannot add video to "+playlist_name+": Playlist does not exist")
        

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlists) != 0:
            print("Showing all playlists:")
            for playlist in reversed(self.playlists):
                print(playlist)

        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_to_read = False
        for playlist in self.playlists:
            if playlist.lower() == playlist_name.lower():
                playlist_to_read = playlist
                chosen_playlist = self.playlists[playlist_to_read]
        if playlist_to_read != False:
            print("Showing playlist: " + playlist_name)
            if chosen_playlist != []:
                for playlist_song in chosen_playlist:
                    for song in self._video_library.get_all_videos():
                        if playlist_song.lower() == song.video_id.lower():
                            tags_string = ""
                            for tag in song.tags:
                                tags_string += str(tag) + " "
                            print(str(song.title) + " (" + str(song.video_id) + ") [" + tags_string[:-1] +"]")
            else:
                print("No videos here yet")
        else:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")


    def remove_from_playlist(self, playlist_name, video_id):


        playlist_to_update = False
        for playlist in self.playlists:
            if playlist.lower() == playlist_name.lower():
                playlist_to_update = playlist
        if playlist_to_update != False:
            playlist_contents = self.playlists.get(playlist_to_update)
            removed_video_title = False
            for video in self._video_library.get_all_videos():
                if video._video_id.lower() == video_id.lower():
                    removed_video_title = video.title
            if removed_video_title != False:
                element_removed = False
                for element in playlist_contents:
                    if element.lower() == video_id.lower():
                        playlist_contents.remove(element)
                        element_removed = True
                self.playlists[playlist_to_update] = playlist_contents
                if element_removed == True:
                    print("Removed video from "+ playlist_name+": " + removed_video_title)
                else:
                    print("Cannot remove video from "+playlist_name+": Video is not in playlist")
            else:
                print("Cannot remove video from "+playlist_name+": Video does not exist")
        else:
            print("Cannot remove video from "+playlist_name+": Playlist does not exist")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_to_update = False
        for playlist in self.playlists:
            if playlist.lower() == playlist_name.lower():
                playlist_to_update = playlist
        if playlist_to_update != False:
            self.playlists[playlist_to_update] = []
            print("Successfully removed all videos from "+playlist_name)
            

        else:
            print("Cannot clear playlist "+playlist_name+": Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_to_update = False
        for playlist in self.playlists:
            if playlist.lower() == playlist_name.lower():
                playlist_to_update = playlist
        if playlist_to_update != False:
            del self.playlists[playlist_to_update]
            print("Deleted playlist: "+playlist_name)
            

        else:
            print("Cannot delete playlist "+playlist_name+": Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        
        possible_videos = []
        video_ids = []
        for video in self._video_library.get_all_videos():
            if search_term.lower() in video.title.lower():
                tags_string = ""
                for tag in video.tags:
                    tags_string += str(tag) + " "
                possible_videos.append(str(video.title) + " (" + str(video.video_id) + ") [" + tags_string[:-1] +"]")
                video_ids.append(video.video_id)
        if possible_videos != []:
            print("Here are the results for " + search_term+":")
            for video_index, video_details in enumerate(possible_videos):
                print(str(video_index+1)+") "+ video_details)
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            number_input = input()
            try:
                if number_input.isdigit() and 0 < int(number_input) <= len(video_ids):
                    self.play(video_ids[int(number_input)+1])
            except:
                pass
        else:
            print("No search results for "+search_term)

        
                
                

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        possible_videos = []
        video_ids = []
        for video in self._video_library.get_all_videos():
            if video_tag in video.tags:
                tags_string = ""
                for tag in video.tags:
                    tags_string += str(tag) + " "
                possible_videos.append(str(video.title) + " (" + str(video.video_id) + ") [" + tags_string[:-1] +"]")
                video_ids.append(video.video_id)
        if possible_videos != []:
            print("Here are the results for " + video_tag+":")
            for video_index, video_details in enumerate(possible_videos):
                print(str(video_index+1)+") "+ video_details)
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            number_input = input()
            try:
                if number_input.isdigit() and 0 < int(number_input) <= len(video_ids):
                    self.play(video_ids[int(number_input)+1])
            except:
                pass
        else:
            print("No search results for "+video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
