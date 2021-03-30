import argparse
import regex

def tokenizer(input):
    tokenizer = re.compile(r'\W+')
    tokens = tokenizer.split(input)
    return tokens

def main(text_path, keyword, window_size, out_path = 'out/output.csv'):
    

if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    ap.add_argument('text_path', required=True, help='Path to textfile')
    ap.add_argument('keyword', required=True, help='The keyword you want to find collocation of')
    ap.add_argument('window_size', required=True, help='The size of the window')
    args = ap.parse_args()

    main(args.text_path, args.keyword, args.window_size)
