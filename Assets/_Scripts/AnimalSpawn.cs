//
// This script is used to display only one animal at a time.
//
// A menu, made out of buttons each representing the animals within the app, allows the user to choose an animal to control.
//
// Each button has an OnClick() event set from within Unity, with "object" holding the GameObject which this script has been applied to
// (i.e. "SafariAnimalsList", the GameObject holding the models for the animals) and "function" AnimalSpawn.Select with a value starting
// with 0 for the first animal.
//

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimalSpawn : MonoBehaviour {

    // Define a new list containing GameObjects
    private List<GameObject> models;

    // Variable holding the animal that has been selected from the bottom menu
    private int SelectionIndex = 0;


    private void Start () {

        SondaManager.inserisciSonda("AnimalSpawn.start");

        // Create a new empty list from the above variable
        models = new List<GameObject>();

        // For each child of the GameObject this script has been applied to
        // i.e. all the animals under the "SafariAnimalsList" GameObject
        foreach(Transform t in transform)
        {
            SondaManager.inserisciSonda("AnimalSpawn.start.foreach(Transform t in transform)");
            // Add the animal to the "models" list
            models.Add(t.gameObject);

            // Set the animal's visibility to hidden
            // i.e. active = false
            t.gameObject.SetActive(false);
        }

        // Only show the animal that has been selected
        // i.e. upon launching the app, models[0] (which is the zebra) will be the only animal visible
        models[SelectionIndex].SetActive(true);
	}

    // Event detecting change of index
    // i.e. event triggered upon pressing one of the animals from the bottom menu (each entry is a button)
    public void Select(int index) {

        SondaManager.inserisciSonda("AnimalSpawn.Select");
        // If the selected animal is already displayed on screen
        if (index == SelectionIndex)
            {
                SondaManager.inserisciSonda("AnimalSpawn.Select.if (index == SelectionIndex)");
                // Nothing happens
                return;
            }

           

        // If the value of index is different than the number of animals contained in the list
        // (in case the app is glitched)
        if (index < 0 || index >= models.Count)
        {
            SondaManager.inserisciSonda("AnimalSpawn.Select.if (index < 0 || index >= models.Count)");
            // Nothing happens
            return;
        }


        // Otherwise, hide the currently displayed animal
        models[SelectionIndex].SetActive(false);

        // Change SelectionIndex to the newly selected animal
        SelectionIndex = index;

        // Display this animal
        models[SelectionIndex].SetActive(true);
	}
}