//
// This script enables continuos autofocus on the camera on the device.
// By default, Vuforia apps have locked autofocus.
//
// Source: https://library.vuforia.com/content/vuforia-library/en/articles/Solution/Working-with-the-Camera.html#Camera-Focus-Modes
//

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Vuforia;

public class AutoFocus : MonoBehaviour {

    void Start()
    {
        // Get the Vuforia instance of the app
        var vuforia = VuforiaARController.Instance;

        // Register OnVuforiaStarted event
        vuforia.RegisterVuforiaStartedCallback(OnVuforiaStarted);

        // Register OnPaused event
        vuforia.RegisterOnPauseCallback(OnPaused);
    }

    // As soon as Vuforia is initialized
    private void OnVuforiaStarted()
    {
        // Override FocusMode
        CameraDevice.Instance.SetFocusMode(

            // Enable continuos autofocus
            CameraDevice.FocusMode.FOCUS_MODE_CONTINUOUSAUTO);
    }

    // When Vuforia is paused
    private void OnPaused(bool paused)
    {
        // When it's resumed
        if (!paused)
        {
            // Focus mode may be reset to default
            // Therefore, re-enable autofocus
            CameraDevice.Instance.SetFocusMode(
                CameraDevice.FocusMode.FOCUS_MODE_CONTINUOUSAUTO);
        }
    }
}
