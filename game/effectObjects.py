from game.effectFunctions import *
effectObjects = {
    "ant" : Effect(ant, Triggers.Faint),
    "beaver" : Effect(beaver, Triggers.Sell),
    "cricket" : Effect(cricket, Triggers.Faint),
    "duck" : Effect(duck, Triggers.Sell),
    "fish" : Effect(fish, Triggers.Level),
    "horse" : Effect(horse, Triggers.Summon),
    "mosquito" : Effect(mosquito, Triggers.StartBattle)

}