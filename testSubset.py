# coding: utf-8
import sys
import os.path
import fontTools.ttLib as ttlib
import fontTools.ttLib.tables as tttables

# platformID
WINDOWS = 3

ttf = ttlib.TTFont(os.path.join(os.path.dirname(__file__), 'mplus-1c-black.ttf'))
#ttf = ttlib.TTFont('R:\\TEMP\\meiryo.ttc', fontNumber=0)

# codeDic = [ { (name, code), ... } ]
codeDics = []
tmp = filter(lambda t:t.platformID == WINDOWS, ttf['cmap'].tables)
for t in tmp:
    print t.platformID, t.platEncID
    codeDic = {}
    for code, name in t.cmap.items():
        codeDic[name] = code
        #print name, code
    codeDics.append(codeDic)

sys.exit()

baseStr = u'芗Windows広ります'
baseChars = map(ord, baseStr)
baseChars = sorted(set(baseChars), key=baseChars.index)
baseChars.append(195060)


for name, glyph in ttf['glyf'].glyphs.items():
    code = -1
    for codeDic in codeDics:
        if name in codeDic:
            code = codeDic[name]
    
    #if code == -1:
    #    print name
    
    if code == -1 or not code in baseChars:
        ttf['glyf'].glyphs[name] = tttables._g_l_y_f.Glyph()
    else:
        print " - %s" % name


ttf.save('R:\\TEMP\\testSubset.ttf')
ttf.close()
