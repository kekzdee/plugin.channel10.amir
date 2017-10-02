import urlparse
import sys,urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin



base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def play_video(path):

    play_item = xbmcgui.ListItem(path=path)

    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

mode = args.get('mode', None)


if mode is None:
    video_play_url = "http://nana10-hdl-il-sw.ctedgecdn.net/Nana10-Live/amlst:hd_,500,1000,1200,2400,/chunklist_b1000000.m3u8"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Live', iconImage='DefaultVideo.png')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    xbmcplugin.endOfDirectory(addon_handle)


elif mode[0] == 'play':
    final_link = args['playlink'][0]
    play_video(final_link)
