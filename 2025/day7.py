class Beam_Tracker:
    __beams = {}
    splits = 0

    def add(self, beam_index, value=1):
        if beam_index in self.__beams:
            self.__beams[beam_index] += value
        else:
            self.__beams[beam_index] = value

    def split(self, beam_index):
        timelines = self.__beams.pop(beam_index)
        self.add(beam_index+1, timelines)
        self.add(beam_index-1, timelines)
        self.splits += 1

    def get_beams_indexes(self):
        return [x for x in self.__beams.keys()]

    def get_splits(self):
        return self.splits

    def get_timelines(self):
        return sum(self.__beams.values())

beams = Beam_Tracker()
with open("input.txt", "r") as f:
    beams.add(f.readline().index("S"))
    for line in f:
        for beam_index in beams.get_beams_indexes():
            if line[beam_index] == "^":
                beams.split(beam_index)

print(f"Part One Answer: {beams.get_splits()}")
print(f"Part Two Answer: {beams.get_timelines()}")