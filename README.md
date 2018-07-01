# Safari Animals AR
A simple game I made to get into Augmented Reality using Unity and Vuforia. Available on the [Google Play Store](https://play.google.com/store/apps/details?id=com.abdu.SafariAR).

![In-game screenshot](https://raw.githubusercontent.com/abdullahibneat/SafariAnimalsAR/master/screenshot.png)

## Marker
By default, the game uses the following marker:

![AR marker](https://raw.githubusercontent.com/abdullahibneat/abdullahibneat.github.io/master/assets/images/AR.jpg)

This can be changed by following the [instructions below](https://github.com/abdullahibneat/SafariAnimalsAR#Change-the-AR-marker).

## Scripts
The app has the following three custom scripts, coded in C#, within the "/assets/[_Scripts](https://github.com/abdullahibneat/SafariAnimalsAR/tree/master/Assets/_Scripts)" folder:

| Name                 | Description                                                                          |
|----------------------|--------------------------------------------------------------------------------------|
| AnimalsController.cs | *Script responsible of moving the animals in the direction of the virtual joystick.* |
| AnimalSpawn.cs       | *Allows the user to pick an animal from a menu.*                                     |
| AutoFocus.cs         | *Used to configure Vuforia to use autofocus on the device's camera.*                 |

Each script includes in-line comments explaining what the line is used for.

## How to use
1. Begin by downloading the project and opening it into Unity. Note the project was last used in `Unity 2018.1.6f1`.
2. Navigate to the `_Scenes` folder, and load the `main` scene by double-clicking it.
3. Select the `AR Camera` component from the hierarchy, and under the `Vuforia Behaviour` component, click on `Open Vuforia Configuration`.
4. Press the `Add license` button just below the App License Key field. This step is required for Vuforia to be enabled. You will be redirected to the [Vuforia Dev Portal](https://developer.vuforia.com/license-manager). Login or register with a free account, and generate a new license key.
5. Copy the license key and paste it into the `App License Key` input field encountered in step 3.

## Change the AR marker
To change the AR marker, head over to the [Vuforia Target Manager](https://developer.vuforia.com/target-manager) and create a new `Database` of type `device`. Open the newly created database, and add at least 1 target. Download the database for the Unity editor. Open the `.unitypackage` file and import its contents into Unity.
Select the `Image Target` component from the hierarchy, and select your database from within the `Image Target Behaviour` as well as your `Image Target`.

## Export for Android
Make sure you have the [required software](https://docs.unity3d.com/Manual/android-sdksetup.html) installed beforehand. Open the `Build settings` dialogue from the `File` menu, and press `Build`.

## Export for iOS
Follow Unity's [Getting started with iOS](https://docs.unity3d.com/Manual/iphone-GettingStarted.html) guide.