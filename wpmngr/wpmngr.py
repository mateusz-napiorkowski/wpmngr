import click
import subprocess
import os


@click.group()
def wpmngr():
    pass


@click.command()
@click.option('-p', '--properties', is_flag=True, help='Show filename, image resolution and file format.')
@click.argument('wallpaper_path', type=click.Path(exists=True))
def setwp(wallpaper_path, properties):
    """Set a wallpaper."""
    if properties:
        name = subprocess.getoutput('identify -format %f {}'.format(wallpaper_path))
        click.echo('Name: {}'.format(name))
        resolution = subprocess.getoutput('identify -format %wx%h {}'.format(wallpaper_path))
        click.echo('Resolution: {}'.format(resolution))
        format_ = subprocess.getoutput('identify -format %m {}'.format(wallpaper_path))
        click.echo('Format: {}'.format(format_))
    paths = subprocess.getoutput('xfconf-query --channel xfce4-desktop --list |grep -E \"image-path|last-image\"'
                                 ).split('\n')
    for path in paths:
        command = ['xfconf-query', '--channel', 'xfce4-desktop', '--property', path, '--set', wallpaper_path]
        subprocess.run(command)


#TODO not working when filename has spaces
#TODO apply DRY
@click.command()
@click.argument('directory', type=click.Path(exists=True))
def browse(directory):
    # TODO update desctiption
    """Loop through all wallpapers"""
    if directory[-1] != '/':
        directory = '{}/'.format(directory)
    wallpapers = os.listdir(directory)
    if wallpapers:
        helpmsg = "Next wallpaper       - '', 'n', 'next'\n" \
                  "Previous wallpaper   - 'b', 'back'\n" \
                  "Stop browsing        - 'stop', 'abort'\n" \
                  "Display this message - 'h', 'help'\n"
    wp_index = 0
    click.echo("\nBrowsing mode activated. Here's how to navigate: \n{}".format(helpmsg))
    while wp_index != len(wallpapers):
        wp_path = directory + wallpapers[wp_index]
        name = subprocess.getoutput('identify -format %f {}'.format(wp_path))
        resolution = subprocess.getoutput('identify -format %wx%h {}'.format(wp_path))
        format_ = subprocess.getoutput('identify -format %m {}'.format(wp_path))
        click.echo('{}. {} {} {}'.format(wp_index, name, resolution, format_))
        paths = subprocess.getoutput('xfconf-query --channel xfce4-desktop --list |grep -E \"image-path|last-image\"'
                                     ).split('\n')
        for path in paths:
            command = ['xfconf-query', '--channel', 'xfce4-desktop', '--property', path, '--set', wp_path]
            subprocess.run(command)
        instruction = input('>> ').lower()
        while instruction not in ['', 'n', 'next', 'b', 'back', 'stop', 'abort', 'h', 'help']:
            click.echo('Wrong input! Try again.\n{}'.format(helpmsg))
            instruction = input().lower()
        if instruction in ['', 'n', 'next']:
            wp_index += 1
        elif instruction in ['b', 'back']:
            if wp_index != 0:
                wp_index -= 1
        elif instruction in ['stop', 'abort']:
            break
        elif instruction in ['h', 'help']:
            click.echo(helpmsg)


wpmngr.add_command(setwp)
wpmngr.add_command(browse)
