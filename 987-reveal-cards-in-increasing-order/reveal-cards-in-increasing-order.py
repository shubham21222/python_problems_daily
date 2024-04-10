class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        new_deck = [deck[-1]]  
        for i in range(len(deck) - 2, -1, -1):  
            new_deck.insert(0, new_deck.pop())  
            new_deck.insert(0, deck[i]) 
        return new_deck
