class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d= {}
        for i,p in enumerate(position):
            d[p] = (target-p)/speed[i]
        fleet = 1
        time = 0
        for i in sorted(d.keys())[::-1]:
            if time == 0:
                time = d[i]
            else:
                if d[i]>time:
                    fleet +=1
                    time = d[i]
        return fleet
