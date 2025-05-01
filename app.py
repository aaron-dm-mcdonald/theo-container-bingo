import random
from rich import print
from rich.console import Console

console = Console()

word_bank = {
    'lizzo': "Singer known for empowerment anthems",
    'dank': "A type of meme or a moist place",
    'bootygasm': "Slang for... intense appreciation of the posterior",
    'abw': "Acronym: American Black Woman",
    'chewbacca': "A hairy sidekick from Star Wars",
    'panatta': "Famous Italian tennis player",
    "chewbacca's left nut": "A crude joke involving a Star Wars character",
    'swedish blondes': "Stereotypical European attraction",
    'waffle house': "Fine Southern dining"
}

# Difficulty selection
console.rule("[bold cyan]Welcome to the Guessing Game!")
mode = console.input("Choose [green]easy[/green] or [red]hard[/red] mode: ").strip().lower()
while mode not in ['easy', 'hard']:
    mode = console.input("Please type 'easy' or 'hard': ").strip().lower()

# Word + hint
secret_word, hint = random.choice(list(word_bank.items()))
secret_word = secret_word.lower()
display_word = secret_word.replace(' ', '')

# Set lives
if mode == 'easy':
    lives = len(display_word)
else:
    lives = max(1, len(display_word) * 2 // 3)

# Extra revealed letters
extra_reveals = 2 if len(display_word) > 8 else 1 if len(display_word) > 5 else 0
reveal_indexes = set()
while len(reveal_indexes) < extra_reveals:
    i = random.randint(1, len(secret_word) - 2)
    if secret_word[i] != ' ':
        reveal_indexes.add(i)

# Create clue
clue = []
for i, char in enumerate(secret_word):
    if char == ' ':
        clue.append(' ')
    elif i == 0 or i == len(secret_word) - 1 or i in reveal_indexes:
        clue.append(char)
    else:
        clue.append('?')

guessed_word_correctly = False

def update_clue_with_letter(letter, secret_word, clue):
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            clue[i] = letter

def update_clue_with_substring(sub, secret_word, clue):
    found = False
    idx = 0
    while idx <= len(secret_word) - len(sub):
        match = True
        for i in range(len(sub)):
            if secret_word[idx + i] != sub[i]:
                match = False
                break
        if match:
            for i in range(len(sub)):
                if secret_word[idx + i] != ' ':
                    clue[idx + i] = secret_word[idx + i]
            found = True
        idx += 1
    return found

# Display initial info
console.print(f"[bold cyan]Hint:[/bold cyan] {hint}")
console.print(f"[green]The word has {len(display_word)} letters and {secret_word.count(' ')} space(s).[/green]")
console.print(f"[blue]First letter:[/blue] '{secret_word[0]}' | [blue]Last letter:[/blue] '{secret_word[-1]}'")
console.print(f"[magenta]You have {lives} lives in {mode.upper()} mode.[/magenta]")

while lives > 0:
    console.print(f"\n[bold white]Clue:[/bold white] {''.join(clue)}")
    console.print(f"Lives left: [red]{'❤ ' * lives}[/red]")
    guess = console.input("[bold]Guess a letter, part of the word, or the whole word:[/bold] ").lower().strip()

    if guess.replace(' ', '') == display_word:
        guessed_word_correctly = True
        break

    if len(guess) == 1:
        if guess in display_word:
            update_clue_with_letter(guess, secret_word, clue)
        else:
            console.print("[red]Incorrect. You lose a life.[/red]")
            lives -= 1
    else:
        if update_clue_with_substring(guess, secret_word, clue):
            console.print("[green]Partial word matched![/green]")
        else:
            console.print("[red]Incorrect guess.[/red]")
            lives -= 1

    if ''.join(clue).replace(' ', '') == display_word:
        guessed_word_correctly = True
        break

# End game
if guessed_word_correctly:
    console.print(f'[bold green]You won![/bold green] The secret word was "[cyan]{secret_word}[/cyan]"')
else:
    console.print(f'[bold red]You lost![/bold red] The secret word was "[cyan]{secret_word}[/cyan]"')
