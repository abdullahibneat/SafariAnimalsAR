using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class SondaManager : MonoBehaviour
{
    private static bool primoAccesso = true;
    private static string path;

    public static void inserisciSonda(string sonda)
    {
        if (primoAccesso)
        {
            path = Application.persistentDataPath + "/LogFile.txt";            
            primoAccesso = false;
        }

        File.AppendAllText(path, sonda + "\n");
        
    }
}

