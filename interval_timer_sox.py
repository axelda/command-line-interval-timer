import time
import os

try:
    import click
except ImportError:
    print('The click package is not installed; please install it first.')


@click.command()
@click.option('--initial-start', default=5, required=True, type=int)
@click.option('--sets', default=2, required=True, type=int)
@click.option('--set-break', default=60, required=True, type=int)
@click.option('--bouts-per-set', default=10, required=True, type=int)
@click.option('--bout-length', default=20, required=True, type=int)
@click.option('--rest-length', default=20, required=True, type=int)
@click.option('--prepare-sound-file', default='prepare_to_start.mp3', type=click.Path())
@click.option('--bout-end-sound-file', default='321.mp3', type=click.Path())
  

def do_multiple_sets(initial_start,
                     sets,
                     set_break,
                     bouts_per_set,
                     bout_length,
                     rest_length,
                     prepare_sound_file,
                     bout_end_sound_file):

    time.sleep(initial_start)

    for i in range(sets):
        click.echo('Set {} starts.'.format(i+1))
        #do_one_set(bouts_per_set, bout_length, rest_length)
        for _ in range(bouts_per_set):

            os.system('play -q ' + prepare_sound_file)
            time.sleep(bout_length)
            os.system('play -q ' + bout_end_sound_file)

            time.sleep(rest_length)

        click.echo('Set {} finished.'.format(i+1))

        if i==(sets-1): break

        time.sleep(set_break)


if __name__ == "__main__":
    do_multiple_sets()