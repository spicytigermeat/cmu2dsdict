# cmu2dsdict

## How to Use
What you need:
- custom cmu-style dictionary. All phonemes should be ready to go, properly capitalized + no extras (like tone indicators)
- phoneme text file. Should be set up like this:
```
aa vowel
b stop
f fricative
ch affricate
l liquid
n nasal
w semivowel
```
Run the command like so:
```
python cmu2dsdict.py -c {cmudict.txt} -p {phones.txt} -o "converted-dsdict.yaml" -cm
```
[-cm] will export the dictionary using smaller lines, making it load a bit faster. This is recommended :)
