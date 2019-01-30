from Text import Text


text = Text("VALIDA EM TODO O TERRITORIO NACIONAL" +  "14/09/1992 13956878701 GABRIEL AMAZONAS MESQUITA")

for line in text.lines:
    print("Line: ")
    print(line.raw_string)
    print("\n")
    for block in line.blocks:
        print("Block: ")
        print(block.raw_string)
        print("\n")
        print("Contains NUmbers?: "+  str(block.contains_digits))
