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
    
    global animale;
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


constSu = 0; 
constgiu = 1;
constDestra = 2;
constSinistra = 3;

poco = None;
listaBottoni = None;
pad = None;
listaAnimali = None;
nomeAnimaleAttualmentePresente = None;

f = open("AllTransitionsCoverageInterazioni.txt","w+");

f.write("Unico paths All Transitions Coverage \n");

avviaApp();
verificaComparsaScena();
verificaAnimaleUnico();

for bottone in listaBottoni:
    clickBottone(bottone)
    verificaAnimaleUnico();
    
for index in range(len(listaBottoni)):
    if (index > 3):
        verificaMovimento(constSu,nomeAnimaleAttualmentePresente,pad);
    else:
        verificaMovimento(index,nomeAnimaleAttualmentePresente,pad)
    
    if (index == 0):        
        verificaMovimento(constSu,nomeAnimaleAttualmentePresente,pad);
        verificaMovimento(constgiu,nomeAnimaleAttualmentePresente,pad);
        verificaMovimento(constDestra,nomeAnimaleAttualmentePresente,pad);
        verificaMovimento(constSinistra,nomeAnimaleAttualmentePresente,pad);
        
    clickBottone(listaBottoni[index])
    verificaAnimaleUnico();
    
f.write("Test concluso senza errori \n");

keyevent("KEYCODE_APP_SWITCH")
keyevent("KEYCODE_APP_SWITCH")  

chiudiApp();
