import click
import subprocess

@click.group()
def wpmngr():
    pass

@click.command()
@click.argument('wallpaper_path', type=click.Path(exists=True))
def setwp(wallpaper_path):
    """Set a Wallpaper"""
    paths = subprocess.getoutput('xfconf-query --channel xfce4-desktop --list |grep -E \"image-path|last-image\"'
                                 ).split('\n')
    for path in paths:
        command = ['xfconf-query', '--channel', 'xfce4-desktop', '--property', path, '--set', wallpaper_path]
        subprocess.run(command)

wpmngr.add_command(setwp)