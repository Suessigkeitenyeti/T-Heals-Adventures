import glob
from dominate import document
from dominate.tags import *

#Liste von allen Ordnerpfaden im Ordner "Berichte"
Stufendir = glob.glob('Berichte/*')
#Liste von allen Ordnern im Ordner "Berichte" (ohne relativen Pfad)
Stufen = [elem[9:] for elem in Stufendir]
#Sortiere Alphabetisch
Stufen.sort()

#Solange es noch Stufen gibt, erstelle Tabelle für die nächste Stufe
for Stufe in Stufendir:
    #Sammle alle Dungeonpfade und Dungeonnamen auf dieser Stufe
    DungeonNamenPfad = glob.glob(Stufe + '/*')
    DungeonNamen = [elem[18:] for elem in DungeonNamenPfad]
    DungeonHTMLPfad = [glob.glob(elem + '/*.html') for elem in DungeonNamenPfad]
    #print(DungeonHTMLPfad)
    if DungeonHTMLPfad[:1]!=[]:
    #EHHH? IDK MAN, ich brauche ein Tupel mit gleich viele Namen und Pfaden oder ne andere Möglichkeit die HTML Tabelle zu basteln
    #maybe schleife 1 - geht alle elemente in htmlpfad durch, dann schleife 2 für alle elemente darin, pack das equivalent in dem berichtpfad da rein
        for BerichtPfadList in DungeonHTMLPfad:
            for BerichtPfad in BerichtPfadList:
                toss, BerichtName = BerichtPfad.rsplit('\\', 1)
                DungeonStufenTupel = (BerichtName, BerichtPfad)
    #DAS SCHEINT HIER ZWISCHEN NICHT ZU FUNKTIONIEREN
                #Mache Tabelle für alle Dungeons auf der Stufe
                print(DungeonStufenTupel)
                print(ul(li(a(BerichtName, href=BerichtPfad))))
    else:
        print(Stufe[9:] + ' hat keine Dungeons!')

#for Stufe in Stufendir: glob.glob(Stufe + '/*.html')

#print(ul(li(a(name, href=link)) for name, link in (Stufe, Stufen)))


#print(StufenMitDungeons)

#for Dungeonpfad in StufeDungeon: print(ul(li(a(Dungeonpfad[1], href=glob.glob(Dungeonpfad[1] + "/*.html")))))


#with document(title="T' Heals Adventures") as doc:
 #   h1('BLUBB')
  #  for path in FirstLayer:
   #     div(img(src=path), _class='FOOBAR')


#with open('Test.html', 'w') as f:
 #   f.write(doc.render())
