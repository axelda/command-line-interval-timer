## Command Line Interval Timer
This repository contains an interval timer for the command line <b>that allows you to specify your own sounds</b> and many other parameters.


## Prerequisites
The timer is written in Python3, hence, <b>you need Python3 installed on your machine.</b> Depending on your OS, you may also have to install
a command line tool to play sounds (see the FAQs for more details). <b>For macOS the timer works out of the box.</b>


## Quickstart (for macOS)
How to start the timer?
1. Download the repository (e. g. with `git clone https://github.com/axelda/command-line-interval-timer.git`).
2. Open a terminal in the root folder of the repository.
3. Run `python interval_timer.py`.

Now, the timer should start with the default values. <b>How to modify the parameters?</b> The command below starts the timer with some of the parameters being modified:

```
python interval_timer.py \
  --initial-start=10 \
  --sets=3 \
  --bout-length=20 \
  --rest-length=10 \
  --bout-end-sound-file='my-cool-closing-tune.mp3'
```

Check the next section to see a list of all the parameters.


## Parameters
The timer has seven parameters that all come with defaults (in brackets):
* initial-start (5): time before the <i>first</i> set begins; use this time to prepare yourself for the start of the workout.
* sets (2): number of sets; each set consists of multiple bouts.
* set-break (60): rest time between the sets
* bouts-per-set (10): number of bouts (rounds) per set
* bout-length (20): length of each bout
* rest-length (20): rest time between the bouts
* prepare-sound-file: sound file that is played before each bout
* bout-end-sound-file: sound file that is played after `bout-length` is over

<b>All times are in seconds.</b>


## FAQ
Here are some common questions:

* What is special about this timer? Most timers do not allow you to specify which sounds are played when a bout starts and ends; this one does. For yoga and meditation you may want to choose relaxing sounds; for HIT workouts instead you choose something fast.
* Does the timer work on other OS than macOS? Yes, but you need a command line tool to play the sound files. In `interval_timer_sox.py` I use the free cross-platform audio software SoX. Just install SoX before you use it.
* On macOS, which command is used to play the sound? `afplay` (built-in utility)
* Does the timer work with Python2.7? I did not test it yet, but I assume the answer is yes.
* Can I contribute? Sure, let me know if you have a concrete suggestion or feature request.
