def translate(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:

        # Rule 1: starts with vowel OR xr / yt
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            result.append(word + "ay")
            continue

        idx = 0

        # Rule 3: consonants followed by "qu"
        while idx < len(word):
            if word[idx] in vowels:
                break
            if word[idx] == "q" and word[idx + 1] == "u":
                idx += 2
                break
            if word[idx] == "y" and idx != 0:
                break
            idx += 1

        # Rule 2 & Rule 4 handled here
        result.append(word[idx:] + word[:idx] + "ay")

    return " ".join(result)
