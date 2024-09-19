
ADDON_NAME = "" #🟢


def clink(name, text,url=None):
    if not url:
        return f'{name} : {text}<br>'
    return f'{name} : <a href="{url}">{text}</a><br>'

credits = """
<br><br><br>
<b>[ CREDIT ]</b>
<br><br><br>
""".replace('\n', '<br>')

patreon = """
Special Thanks
<b>[ PATRONS ]</b>
Arthur Bookstein
Haruka
Luis Alberto, Letona Quispe
GP O'Byrne
Tobias Klös
07951350313540
Douglas Beeman
Gabriel Vinicio Guedes
Ernest Chan
Haley Schwarz
Daniel Kohl-Fink
Ketan Pal
Lily
Tim
Oleksandr Pashchenko
Alba Grecia Suárez Recuay
Kurt Grabow
Alex D
Kyle Mondlak
Jesse Asiedu
Renoaldo Costa Silva Junior
Felipe Dias
NamelessGO
Fahim Shaik
Corentin
Yitzhak Bar Geva
龍星 武田
Muneeb Khan
Hikori
Lê Hoàng Phúc
ElAnki
oiuhroiehg
Tae Lee
Ashok Rajpurohit
Tobias Günther
NoirHassassin
Jk
Jake Stucki
Cole Krueger
Ansel Ng
Victor Evangelista
Moritz Bluhm
Maik C.
Ricardo Escobar
Daniel Valcárcel Málaga
Lerner Alcala
Jason Liu
Blake
Rogelio Rojas
Bunion Bandit
ifjymk
K
Aaron Buckley
KM
Melchior Schilling
Адріан Недбайло
철수 박
Lisette Lerma
Abhi S
Natalia Ostaszewska
Jordyn Kindness
Wa sup
Patrick Lee
Jacob Royce
Mattia Adami
Gregory Dance
Carlos Garcia
cedox
Jonny MacEachern
🌠
Tan Mun Ling
Martin Gerlach
Knightwalker
Lukas Hammerschmidt
HORUS ™
as cam
Richard Fernandez
K Chuong Dang
Hashem Hanaktah
Justin Skariah
Marli
Ella Schultz
Ali Abid
Siva Garapati
Nitin Chetla
hubert tuyishime
J
Dan S
Salman Majid
C
Maduka Gunasinghe
Marcin Skic
Andreas China
anonymous
Chanho Youne
Dhenis Ferisco
Wave
Foxy_null
WolfsForever
César Flores
Abufit Club
JB Eyring
Yazan Bouchi
Corey
mootcourt
Peter McCabe
Daniel Chien
D N
Mrudang
Yon Uni
Saad
Jared
Mohull Mehta
Robert Malone
On The Path Of Righteousness
Wei
Xeno G
Theodore Addo
Robert Balisong
Tyler Schulte
Jonathan Contreras
Greg
Philly
Đen Trắng
Osasere Osula
Morgan Torres
Rae Hanna
Natalie
Michael Pekala
Fraol Feye
Cameron M
Omar Toro
Keeler Kime
Melvin Ezennia
Nailah Kahotep
Sean Voiers


""".replace('\n', '<br>')

sound =("<b>[ SOUNDS & BGM ]</b><br>"+
clink("Sound Effect", "Koukaon lab","https://soundeffect-lab.info/",)+
clink("Music" , "MaouDamashii","https://maou.audio/",)+
clink("Catgirl Voice","Cici Fyre","https://cicifyre.itch.io/")+
clink("Robot Voice","Charlie Pennell Productions©","https://www.charliepennellproductions.com/")+
clink("classical music"," Bernd Krueger","http://www.piano-midi.de/")
)


caractor = ("<b>[ IMAGE&3D MATERIALS ]</b><br>" +
clink("Knight","rvros","https://rvros.itch.io/") +
clink("Hooded","Penzilla","https://penzilla.itch.io/")+
clink("CatGirl","(Unity-chan)Kanbayashi Yuko<br>© Unity Technologies Japan/UCL","https://unity-chan.com/contents/guideline/")+
clink("Monsters","RPG dot(R-do) monta!","http://rpgdot3319.g1.xrea.com/")+
clink("Sushi","Ichika","https://www.ac-illust.com/main/profile.php?id=23341701&area=1")+
clink("Textures","PiiiXL","https://piiixl.itch.io/")+
clink("Banner Materials,Lock on cursor<br>","Nanamiyuki's Atelier","https://nanamiyuki.com/")+
clink("Sniper animated","DJMaesen","https://sketchfab.com/3d-models/sniper-animated-eae1ba5b43ae4bc89b0647fb5d8a2d27")+
clink("Parasite Zombie","Mixamo","https://www.mixamo.com/")+
clink("MiniZombie&RedHat","Fkgcluster","https://fkgcluster.itch.io/survivaltowerdefense")+
clink("BloodEffect","XYEzawr","https://xyezawr.itch.io/gif-free-pixel-effects-pack-5-blood-effects")+
clink("Cats","girlypixels","https://girlypixels.itch.io/")+
clink("Terminator-Core","Fred Drabble","https://sketchfab.com/3d-models/fusion-core-f717683d5502496d9e1ef1f1e1d1cb45" )+
clink("Terminator-Robo","Threedee","https://www.threedee.design/cartoon-robot")+
clink("Meowknight","9E0", "https://9e0.itch.io/")+
clink("Vegetable","Butter Milk","https://butterymilk.itch.io/")+
clink("Flower","kathychow","https://kathychow.itch.io/")+
clink("Crops", "bluecarrot16, Daniel Eddeland (daneeklu),<br> Joshua Taylor, Richard Kettering (Jetrel).<br> Commissioned by castelonia", "https://opengameart.org/content/lpc-crops")+
clink("Farmer","Butter Milk","https://butterymilk.itch.io/")

            )


addons = ("<b>[ Original Add-on ]</b><br>"+
clink ("Enhance main window","Arthur Milchior","https://github.com/Arthur-Milchior/anki-enhance-main-window")+
clink ("Based on" ,"Anki code by Damien Elmes", "https://github.com/dae")+
clink ("Based on" ,"Helen Foster's code in add-on Deck counts now later", "https://github.com/HelenFoster")+
clink ("Original idea", "Juda Kaleta")+
clink ("Somme CSS","Some idea from cjdduarte")+
clink ("Bug correction","telotortium on Github")+
clink ("Percent bar","Idea and partial realization by Kyle Khonkhortisan Mills")+
clink ("Contributor","Kyle Mills","https://github.com/khonkhortisan")+
clink ("Contributor","ngirard","https://github.com/ngirard")+
clink ("Contributor","grac-zh","https://github.com/grac-zh")+
clink ("Contributor","Aleksej","https://github.com/aleksejrs")+
clink ("Contributor","Robert Irelan","https://github.com/telotortium")+
clink ("Contributor","Scott Noyes","https://github.com/snoyes")+
clink ("Contributor","Guillem Palau","https://github.com/guillempalau")+
clink ("Contributor","Sam Bradshaw","https://github.com/roxgib")+
clink ("Contributor","Jeffrey Ying","https://github.com/Jefftree")+
clink ("Contributor","Gustaf-C","https://github.com/Gustaf-C")
)

budle = ("<b>[ BUNDLE SOURCE CODE ]</b><br>"+
clink ("BGM","Pyglet","https://pyglet.readthedocs.io/en/latest/index.html")+
clink ("webp","dwebp","https://developers.google.com/speed/webp/download")+
clink ("midi","FluidSynth","https://www.fluidsynth.org/")

)

thankYou = ("""
<br><br><br>
<h3>%s</h3><br>""" % ADDON_NAME +
clink("Customized  by", "Shigeyuki","https://www.patreon.com/Shigeyuki")+
"""
<br>
Thank you very much!
<br><br><br><br>
""")