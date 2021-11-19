with open('/Users/cynthiathena/Documents/IF/[SEM 7] Speech processing/tubes_speech/tubes-speech/src/prompts.txt') as f:
    lines = f.read().splitlines()
    new_line = []
    for line in lines:
        words = line.split()
        for idx, word in enumerate(words[1:]):
            words[idx + 1] = word.upper()
        new_line.append(' '.join(words))
    print(new_line)

with open('/Users/cynthiathena/Documents/IF/[SEM 7] Speech processing/tubes_speech/tubes-speech/src/prompts.txt', 'w') as f:
    for line in new_line:
        f.write(line + '\n')