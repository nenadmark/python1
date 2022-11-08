# Napisite program koji kreira akorde na osnovu pocetnog tona, odnosno note

ton = input("Unesi početni ton: ").upper()
note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]
note_length = len(note)

for i in note:
    starting_note = note.index(ton)
    dur_2 = (starting_note + 4) % note_length
    dur_3 = (starting_note + 7) % note_length
    mol_2 = (starting_note + 3) % note_length
    mol_3 = (starting_note + 7) % note_length

print("Durski akord čine: ", ton, note[dur_2],  note[dur_3])
print("Molski akord čine: ", ton.lower(), note[mol_2].lower(),  note[mol_3].lower())