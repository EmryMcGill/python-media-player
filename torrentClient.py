import requests
import subprocess
import sys


# main func
def main():
    # user inputs movie
    moviename = input('Enter name of movie: ')
    # search API for movie
    baseURL = f'https://api.sumanjay.cf/torrent/?query={moviename}'

    #getting selected movie info
    torrentresults = requests.get(baseURL).json()

    #displaying movie info
    magnet = ''
    for result in torrentresults:
        if 'movie' in result['type'].lower(): 
            print(result['name'])
            print(result['size'])
            magnet = result['magnet']
            break

    # user chooses stream option
    streamchoice = int(input('Torrent Options:\n1) Stream\n2) Download\n'))


    if streamchoice == 1:
        #stream
        download = False
    elif streamchoice == 2:
        #download
        download = True
    else:
        print('wrong option\nExiting...')

    handler(magnet, download)


# handles torrent client
def handler(magnet, download):
    
    if not download:
        cmd = 'peerflix "' + magnet + '" --vlc --path /Documents'
    else:
        cmd = 'peerflix "' + magnet + '" --path /Documents'
    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'): 
        subprocess.call(cmd,shell=True)
    
# run main func
main()