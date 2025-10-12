# -----------------------------------------------------------------------------
# 🔧 Command Line Usage Notes
# -----------------------------------------------------------------------------
# You can run the script directly from the terminal:
#
#     python 01_DTMF.py -v audio_test.wav
#
# Or, if you are using the original CLI command from dtmf-decoder:
#
#     dtmf [-h] [-v] [-l] [-r] [-d] [-t F] [-i T] file.wav
#
# Optional arguments:
#   -h, --help       Show this help message and exit.
#   -v, --verbose    Display a complete timeline of detected tones.
#   -l, --left       Use only the left channel (if the audio is stereo).
#   -r, --right      Use only the right channel (if the audio is stereo).
#   -d, --debug      Show diagnostic graphs to visualize signal detection.
#   -t F             Acceptable frequency error in hertz (default: 20 Hz).
#   -i T             Time interval in seconds for processing (default: 0.05 s).
#
# Example:
#     python 01_DTMF.py -v audio_test.wav
#
# Notes:
# - The `-v` (verbose) flag is useful for confirming which tones were detected
#   and when they occurred in the timeline.
# - Adjusting `-t` can help if your tones are slightly off the standard DTMF
#   frequencies, but this does not directly improve precision.
# - Keep your audio mono, 8–16 kHz sample rate, and normalized for best results.
# Special thanks to the original authors of dtmf-decoder — this script serves as a tutorial 
# on how DTMF can be applied in phone-based surveys, particularly for gender-related research.
# Link to the repository: https://github.com/ribt/dtmf-decoder
# -----------------------------------------------------------------------------
