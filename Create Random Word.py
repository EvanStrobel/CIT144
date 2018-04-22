def createRandomWord():
    import random
    lstPrefixes = ["ad","aer","anti","blasto","cell",
                   "chloro","diplo","epi","extra","exo",
                   "halo","inter","morph","omni","para",
                   "pro","retro","semi","ultra","zoo"]
    lstSuffixes = ["blast","dactyl","hedron","lysis",
                   "mancy","ism","meter","stasis","zoic",
                   "able","age","algia","ation","dom",
                   "hood","ing","itis","osis","phobia",
                   "ward"]
    random.shuffle(lstPrefixes)
    random.shuffle(lstSuffixes)
    strWord = lstPrefixes[1] + lstSuffixes[1]
    return(strWord)
