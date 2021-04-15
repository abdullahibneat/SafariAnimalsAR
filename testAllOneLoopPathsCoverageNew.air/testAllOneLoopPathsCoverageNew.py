# -*- encoding=utf8 -*-
__author__ = "Danilo"

from airtest.core.api import *
auto_setup(__file__)
from random import *
from poco.drivers.unity3d import UnityPoco


def avviaApp():
    
    os.system('cmd /c "cd '+os.environ['USERPROFILE']+'\\Desktop\\AirtestIDE\\airtest\\core\\android\\static\\adb\\windows & adb shell am start com.abdu.SafariAR/com.unity3d.player.UnityPlayerActivity"')
    time.sleep(18);
    inizializza();
    
    
def chiudiApp():
    keyevent("KEYCODE_APP_SWITCH")
    keyevent("DEL")
    time.sleep(5)
        
def inizializza():
    global poco;
    global nomeAnimaleAttualmentePresente;
    
    poco = UnityPoco();
    animaleDefault = "Safari_ZebraSkin";
    nomeAnimaleAttualmentePresente = animaleDefault;


def verificaComparsaScena():
    global listaBottoni
    global pad
    global listaAnimali
    
    scenaSavana = poco("terrain").children();
    comparsaScena = False;
    listaBottoni = poco(type='Button');
    pad = poco("MobileJoystick");

    if(len(scenaSavana) > 0 and len(listaBottoni) > 0 and pad.exists()):
        comparsaScena = True;
    assert_equal(comparsaScena,True,"scena comparsa dopo rilevazione marker");
    
    listaAnimali = getListaAnimali(listaBottoni);
    
def getListaAnimali(listaBottoni):
    listaAnimali = [];
    for bottone in listaBottoni:
        tipoAnimale = bottone.attr('name');
        nomeAnimale = "Safari_"+tipoAnimale+"Skin";
        listaAnimali.append(nomeAnimale);
    return listaAnimali;

def verificaAnimaleUnico():
    
    global listaAnimali
    global nomeAnimaleAttualmentePresente
    
    for nome in listaAnimali:
        if (nome != nomeAnimaleAttualmentePresente ):
            specie = nome.split("_")[1].split("Skin")[0];
            assert_equal(poco(nome).exists(),False,specie+" non presente sulla scena");

def verificaMovimento(direzione,nomeAnimaleAttualmentePresente,pad):
    direzioni = ["su","giu","destra","sinistra"];
    print("Transizione spostamento pad "+ direzioni[direzione]);
    f.write("pad spostato: " + direzioni[direzione]+"\n");
    animale = poco(nomeAnimaleAttualmentePresente);
    posizione = animale.get_position();
    spostamento = False;
    
    #spostamento su
    if(direzione == 0):
        pad.swipe([0.0, -0.03])
        posizioneSpostamento = animale.get_position();
        if(posizione[1]>posizioneSpostamento[1]):
            spostamento = True;
    #spostamento giu
    elif(direzione == 1):
        pad.swipe([0.0, 0.03])
        posizioneSpostamento = animale.get_position();
        if(posizione[1]<posizioneSpostamento[1]):
            spostamento = True;
    #spostamento a destra
    elif(direzione == 2):
        pad.swipe([0.03, 0.0])
        posizioneSpostamento = animale.get_position();
        if(posizione[0]<posizioneSpostamento[0]):
            spostamento = True;
    #spostamento a sinistra
    else:
        pad.swipe([-0.03, 0.0])
        posizioneSpostamento = animale.get_position();
        if(posizione[0]>posizioneSpostamento[0]):
            spostamento = True;
    
    assert_equal(spostamento,True,"spostatamento avennuto nella direzione:"+direzioni[direzione])
    

def clickBottone(bottone):
    
    #global animale;
    global nomeAnimaleAttualmentePresente
    global listaAnimali
    
    tipoAnimale = bottone.attr('name');
    f.write("bottone cliccato: " + tipoAnimale+"\n");
    nomeAnimale = "Safari_"+tipoAnimale+"Skin";
    animale = poco(nomeAnimale);
    if( nomeAnimale != nomeAnimaleAttualmentePresente):
        assert_equal(animale.exists(),False,tipoAnimale+" attualmente non presente sulla scena");
    bottone.click();    
    assert_equal(animale.exists(),True,tipoAnimale+" presente sulla scena");    
    nomeAnimaleAttualmentePresente = nomeAnimale;    


    
    
poco = None;
listaBottoni = None;
pad = None;
listaAnimali = None;
nomeAnimaleAttualmentePresente = None;

f = open("AllOneLoopPathsCoverageInterazioni.txt","w+");

f.write("PATHS LUNGHEZZA 3 \n");
f.write("\npath 1\n");
avviaApp();
#animale = poco(animaleDefault);
verificaComparsaScena();
verificaAnimaleUnico();


#PATHS DI LUNGHEZZA TRE 6
for ind in range(len(listaBottoni)):
    clickBottone(listaBottoni[ind]);   
    verificaAnimaleUnico();
    chiudiApp();
    avviaApp();
    verificaComparsaScena();
    verificaAnimaleUnico();
    if(ind < len(listaBottoni)-1):
        f.write("\npath "+str(ind+2)+"\n");

f.write("\nPATHS LUNGHEZZA 4 \n");
f.write("path 1\n");
count = 2; 


# PATHS DI LUNGHEZZA QUATTRO 24 + 16 +24
for ind in range(len(listaBottoni)):    
    for direction in range(4):
        
        clickBottone(listaBottoni[ind]);
        verificaAnimaleUnico();
        verificaMovimento(direction,nomeAnimaleAttualmentePresente,pad);
        chiudiApp();
        avviaApp();
        verificaComparsaScena();
        verificaAnimaleUnico();
             
        f.write("\npath "+str(count)+"\n");
        count = count+1

for i in range(4):
    for j in range(4):
        verificaMovimento(i,nomeAnimaleAttualmentePresente,pad);
        verificaMovimento(j,nomeAnimaleAttualmentePresente,pad);
        chiudiApp();
        avviaApp();
        verificaComparsaScena();
        verificaAnimaleUnico();
        f.write("\npath "+str(count)+"\n");
        count = count+1


for i in range(4):
    for j in range(len(listaBottoni)):
        verificaMovimento(i,nomeAnimaleAttualmentePresente,pad);
        clickBottone(listaBottoni[j]);
        verificaAnimaleUnico();
        chiudiApp();        
        if (i != 3 or j != len(listaBottoni)-1):            
            avviaApp();
            verificaComparsaScena();
            verificaAnimaleUnico();
            f.write("\npath "+str(count)+"\n");
            count = count+1


f.write("Test concluso senza errori \n");