with open("input.txt", "r") as f:
    processed = 0
    splits = 0
    first_index = f.readline().index("S")
    beams = {first_index}
    quantum_beams = [first_index]
    for line in f:
        for beam in [x for x in beams]:
            if line[beam] == "^":
                splits += 1
                beams.remove(beam)
                if beam+1 < len(line):
                    beams.add(beam+1)
                if beam-1 > -1:
                    beams.add(beam-1)
        for beam in [x for x in quantum_beams]:
            if line[beam] == "^":
                quantum_beams.remove(beam)
                if beam+1 < len(line):
                    quantum_beams.append(beam+1)
                if beam-1 > -1:
                    quantum_beams.append(beam-1)
        processed += 1
        print(f"Processed: {processed}/142")
    print(f"Part One Answer: {splits}")
    print(f"Part Two Answer: {len(quantum_beams)}")