def zenit_polar_replalce(text):
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
    sample_text = "Zenit Polar é uma técnica interessante."
    modified_text = zenit_polar_replalce(sample_text)

    split_text = sample_text.split()
    cap_sample_text = sample_text.title()

    cap_split_words = [zenit_polar_replalce(word) for word in split_text]

    new_cap_text = ' '.join(cap_split_words)

    print(f"Texto original: {sample_text:>41}")
    print(f"Texto modificado: {modified_text:>41}")
    print(f"Texto modificado com capitalização: {new_cap_text:>41}")
    print(f"Texto original com capitalização: {cap_sample_text:>41}")
    print(f"Palavras modificadas com capitalização: {cap_split_words}")
    #      1234567890234567890123456789012345678901
    #               1        2         3         4

if __name__ == "__main__":
    main()