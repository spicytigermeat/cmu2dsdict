import yaml
import argparse
from ftfy import fix_text as fxy

#this is for me cuz i'm silly teehee
DEBUG = False
dbg = 'DEBUG: '

def dict_loader(in_dict_path):
	#get input dict, turn to dictionary
	in_dict = {}
	with open(in_dict_path, 'r', encoding='utf-8') as f:
		for line in f:
			line = fxy(line)
			split_line = line.split('  ')
			in_dict[split_line[0]] = split_line[-1].rstrip().split(' ')
	
	if DEBUG: print(dbg + 'word-hello, phones-' + str(in_dict['hello']))

	return in_dict

def phones_loader(phones_path):
	#get phonemes for dict, turn into py dictionary
	phones = {}
	phones_list = []
	with open(phones_path, 'r', encoding='utf-8') as f:
		for line in f:
			line = fxy(line)
			split_line = line.split(' ')
			phones[split_line[0]] = split_line[-1].rstrip()

	if DEBUG: print(dbg + 'phone-b, type-' + str(phones['b']))

	return phones

def build_dsdict(in_dict, phones, output_path):

	dsdict = {'symbols': [], 'entries': []}

	if DEBUG: print(dsdict['symbols'])

	#build symbols section first :3
	for key in phones:
		symbol = key
		pho_type = phones[key]
		dsdict['symbols'].append({'symbol':symbol, 'type':pho_type})

	if DEBUG: print(dsdict['symbols'][0])

	#build entries section nexd :0
	for key in in_dict:
		word = key
		ph_reading = in_dict[key]
		dsdict['entries'].append({'grapheme':word, 'phonemes':ph_reading})

	if DEBUG: print(dsdict['entries'][0])

	return dsdict

def export_dsdict(dsdict, output_path):
	#manually writing the yaml file to keep it readable, but also a smaller file size.
	out_string = 'symbols:\n'

	#write phone section :3
	for i in range(len(dsdict['symbols'])):
		out_string += '- %s\n' % (str(dsdict['symbols'][i]).replace('\'', ''))

	#write words section >:3c
	out_string += 'entries:\n'
	for i in range(len(dsdict['entries'])):
		out_string += '- %s\n' % (str(dsdict['entries'][i]).replace('\'', ''))
	
	#i do not prefer writing yaml files this way but I cannot get an export I'm happy with otherwise :(
	with open(output_path, 'w', encoding='utf-8') as v:
		v.write(out_string)

	print('Dictionary exported as \"' + output_path + '\".')
	
def main(in_dict_path, phones_path, output_path):
	### main function :3
	#load reference dictionary
	in_dict = dict_loader(in_dict_path)

	#load phoneme definitions
	phones = phones_loader(phones_path)

	#build dict
	dsdict = build_dsdict(in_dict, phones, output_path)

	export_dsdict(dsdict, output_path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Converts any CMU-style phonetic dictionary into a dsdict.yaml for DiffSinger.')
	parser.add_argument('-c', '--cmu', type=str, help='Input CMU-style Dictionary')
	parser.add_argument('-p', '--phones', type=str, help='File with phoneme and description')
	parser.add_argument('-o', '--output', type=str, default='conv_dsdict.yaml', help='What to name the output file, and where to save')
	args = parser.parse_args()
	main(args.cmu, args.phones, args.output)
