import click
import subprocess


@click.group()
def wpmngr():
    pass


@click.command()
@click.option('-p', '--properties', is_flag=True, help='Show filename, image resolution and file format.')
@click.argument('wallpaper_path', type=click.Path(exists=True))
def setwp(wallpaper_path, properties):
    """Set a Wallpaper"""
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


wpmngr.add_command(setwp)
