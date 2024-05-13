<h1 align=center> TmuxRadio </h1>
<p align=center> SEARCH, PLAY radio station from the globe from your terminal </p>

### Demo
<p align=center>https://github.com/sifaw99/terminal_radio/assets/64286343/27e3ef74-6a57-4408-ab6b-e48edd1f4558</p>

### Features
- [x] Looks minimal and user-friendly
- [x] Supports more than 40K stations !! :radio:
- [x] Consume less memory than GUI app !!  
### Install
First run:`pip3 install setuptools`, and then <br/>
Simply run: `pip3 install tmuxradio`

I recommend installing it using `pipx install tmuxradio`

### External Dependency

It needs [FFmpeg](https://ffmpeg.org/download.html) to be installed on your
system in order to play the audio

on Ubuntu-based system >= 20.04, Run

```
sudo apt update && sudo apt install ffmpeg
```

For other systems including Windows see the above link.

### Run

Search a station with `radio -s [STATION_NAME]`. <br/>
Or  <br/>
Search a station with `tmuxradio -s [STATION_NAME]`. <br/>
`-s` is mandatory option

#### TODO:

- [ ] Create other options filter by tag, country, votes, popularity...
- [ ] Fetch song information artist and music name
- [ ] Create favorite list
- [ ] Test app in other platform currently tested in Ubuntu





