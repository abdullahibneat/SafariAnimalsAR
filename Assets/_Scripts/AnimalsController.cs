//
// Source: https://www.youtube.com/watch?v=khavGQ7Dy3c
//
// This script, provided by the above source, allows the user to control the motion of
// each animal, switching the animation from idle to walk.
//

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityStandardAssets.CrossPlatformInput;


public class AnimalsController : MonoBehaviour
{
    // Define the RigidBody component
    private Rigidbody rb;

    // Define the Animation component
    private Animation anim;


    void Start()
    {
        
        // Assign the above variable "rb" to the GameObject's RigidBody component
        rb = GetComponent<Rigidbody>();

        // Assign the above variable "anim" to the GameObject's Animation component
        anim = GetComponent<Animation>();
        SondaManager.inserisciSonda("AnimalsController.start");
        
    }

    // For each frame
    void Update()
    {
        SondaManager.inserisciSonda("AnimalsController.update");
        // Get the horizontal axis from the joystick
        // (CrossPlatformInput is the library which controls the joystick)
        float x = -CrossPlatformInputManager.GetAxis("Horizontal");

        // Get the vertical axis from the joystick
        float y = CrossPlatformInputManager.GetAxis("Vertical");

        // Create a new vector, which will hold the position of the joystick
        Vector3 movement = new Vector3(x, 0, y);

        // Rate of speed the animals will be moving
        rb.velocity = movement * 0.15f;

        // If joystick's x and y values are different from 0
        // i.e. joystick has been moved
        if (x != 0 && y != 0)
        {
            // Move the animal in the direction of the joystick
            transform.eulerAngles = new Vector3(transform.eulerAngles.x, Mathf.Atan2(x, y) * Mathf.Rad2Deg, transform.eulerAngles.z);
            SondaManager.inserisciSonda("AnimalsController.update.if (x != 0 && y != 0)");
        }

        // If either x or y values are different from 0
        // i.e. animal is moving
        if (x != 0 || y != 0)
        {
            // Play the walk animation
            anim.Play("walk");
            SondaManager.inserisciSonda("AnimalsController.update.if (x != 0 || y != 0)");
        }

        // Otherwise
        // i.e. animal is not being moved
        else
        {
            // Play the idle animation
            anim.Play("idle");
            SondaManager.inserisciSonda("AnimalsController.update.if (x != 0 || y != 0).else");
        }
    }
}