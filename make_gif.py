import imageio
from PIL import Image
import os

def make_gif(folder = 'image_pop_dens', name = 'CO_pop_dense.GIF', save_to = 'plots'):
    file_names = sorted((fn for fn in os.listdir(folder) if fn.endswith('.png')))
    images = [(folder + '/' + fn) for fn in file_names]
    print images
    frames = [imageio.imread(im) for im in images]
    save_path = save_to + '/' + name
    print save_path
    imageio.mimsave(save_path, frames, 'GIF', **{'duration':.1})

def check_dir(n, dirs):
    if n not in dirs:
        print '{} is not available, try again'.format(n)

def get_from_folder(dirs):
    folder = None
    while folder not in dirs:
        print 'directories to choose from: ', dirs
        folder = raw_input('Type which directory the images are in?: ')
        check_dir(folder, dirs)
    return folder

def get_to_folder(dirs):
    save_to = None
    while save_to not in dirs:
        print 'directories to choose from: ', dirs
        save_to = raw_input('where would you like to save GIF?: ')
        check_dir(save_to, dirs)
    return save_to

def where_to():
    dirs = next(os.walk('.'))[1]
    folder = get_from_folder(dirs)
    save_to = get_to_folder(dirs)
    name = raw_input('what would you like to name your GIF?: ')
    return folder, save_to, name

if __name__ == '__main__':

    yn = raw_input('Custom save? type y for yes, n for no: ')
    if yn == 'y':
        f, st, n = where_to()
        print f, st, n
        make_gif(folder = f, name = n, save_to = st)
    else:
        make_gif()
