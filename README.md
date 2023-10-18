# cmu2dsdict

## How to Use
What you need:
- custom cmu-style dictionary. All phonemes should be ready to go, properly capitalized + no extras (like tone indicators)
- phoneme text file, needs to be formatted like the phones_eng.txt file. Include all phonemes a DB can use!
Run the command like so:
```
python cmu2dsdict.py -c {cmudict.txt} -p {phones.txt} -o "converted-dsdict.yaml" -cm
```
[-cm] will export the dictionary using smaller lines, making it load a bit faster. This is recommended :)
