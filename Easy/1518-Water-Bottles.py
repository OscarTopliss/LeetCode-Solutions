class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # initial drink
        emptyBottles: int = numBottles
        drunkBottles: int = numBottles
        numBottles = 0
        while emptyBottles >= numExchange:
            # exchange
            numBottles += emptyBottles // numExchange
            emptyBottles -= (emptyBottles // numExchange) * numExchange

            # drink
            emptyBottles += numBottles
            drunkBottles += numBottles
            numBottles = 0

        # final drink
        drunkBottles += numBottles
        return drunkBottles
