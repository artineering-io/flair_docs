---
title: "Activation"
sidebar:
  order: 2
---
<span class="new-label">New in Flair 1.2</span>
When Flair is run and doesn't find a valid license, you will be prompted with the activation picker:

<figure class="aio-ui-highres aio-window">
<img src="/media/maya/setup/activation/activation_key.png" alt="Activation picker" />
<figcaption>Choose the license you wish to activate.</figcaption>
</figure>

* **With a license key** lets you enter the [activation key](#with-a-license-key) of your license.  
* **Through a license server** lets you enter the port and hostname to connect to a [floating license](#floating-licenses) server.
* **Free version** activates the free version of Flair, only limited in resolution to 1280 x 800 pixels.

## With a license key 
You activate your Flair license key by choosing `With a license key`, entering the **activation key** and clicking on `Activate`.

The activation key is sent to you via email shorly after [making your purchase](https://artineering.io/software/flair#pricing).
To validate license keys, you will need to be online upon loading Flair. If you happen to not have internet at some point while launching Flair, you can still use Flair _Free_ with a limited resolution until you are back online to validate your license.

:::note
A **single Flair license** can be active on **only one computer at a time**.  
Licenses can be **migrated between computers after 6 hours** have passed from a previous activation.
:::

If the license key has been activated on a different computer, you will be asked if you want to [migrate the license](#license-migration) to this machine. Otherwise, you will directly be prompted with the [**End-User-License Agreement (EULA)**](#end-user-license-agreements-eulas), which must be accepted to use Flair.

### License Migration

Licenses keys can be **migrated between computers** once **6 hours have passed** from a previous activation.

:::caution
Attempting to migrate (transfer) the license before 6 hours have passed will lead to a failed activation error.
:::

To migrate a license, **just enter the license key into the new computer**  during activation. If a another license was previously activated on the new computer, follow the **steps to [change the license](#changing-a-license)** to **delete the activated license** and **trigger a new license activation**.

If the license activation key was previously used on another computer, you will be prompted to **confirm the migration** of the license.

<figure class="aio-ui aio-window">
<img src="/media/maya/setup/activation/activation_migration.png" alt="Flair migration prompt" />
<figcaption>Flair license prompt that appears to confirm the license migration.</figcaption>
</figure>

Click `Activate` to confirm, or `Cancel` to abort the activation.

After a successful migration, the license in the **other computer will automatically deactivate** and you can **use Flair in the new computer**.

## Floating Licenses
You activate a floating license by choosing `Through a license server`, entering the **port number** (default: 6349), the **hostname or ip address** of the licensing server and clicking on `Activate` to **claim a license**. If a license is available on the licensing server, it will be **assigned to your computer**.

<figure class="aio-ui-highres aio-window">
<img src="/media/maya/activation_server.png" alt="Flair server activation" />
<figcaption>Enter the port number and hostname or ip address in the text fields.</figcaption>
</figure>

:::note
If you don't want to manually enter the port and hostname, you can specify a `FLAIR_SERVER` environment variable containing `PORT@HOSTNAME` pointing directly to the licensing server.
:::

Floating Flair licenses do not need an internet connection for validation, but **require a licensing server within your local network** instead.
The licensing server will **relay the available licenses to the computers** that need the Flair license, allowing licenses to **roam between artists**.

Licenses are released from the licensing server once all instances of Flair are closed or if Flair doesn't send a heartbeat within a minute from the computer that claimed it.

:::note
Floating licenses are available when purchasing multiple Flair _STUDIO_ or _INDIE for Education_ licenses directly through us. [**Get in touch**](https://artineering.io/contact) with our sales team to get setup.
:::

If a floating license has never been used on the computer, you will be prompted with the [**End-User-License Agreement (EULA)**](#end-user-license-agreements-eulas), which must be accepted to use Flair.

## Free version
You activate a the free version of Flair by choosing `Free version` and clicking on `Activate`.

<figure class="aio-ui-highres aio-window">
<img src="/media/maya/setup/activation/activation_free.png" alt="Flair free version activation" />
<figcaption>Click on Activate to activate the free version of Flair.</figcaption>
</figure>

This will prompt the [**End-User-License Agreement (EULA)**](#end-user-license-agreements-eulas), which must be accepted to use Flair.

## Changing a license
If you want to remove a Flair license and activate a different one instead you need to **re-install Flair** and choose to **Delete the existing license**.

:::note
This is useful when upgrading/downgrading between the Free, Community, Indie or Studio licenses.
:::

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/KtiFdePYM-Q" title="Changing the Flair license" allowfullscreen loading="lazy"></iframe>
<figcaption>Changing the Flair license</figcaption>
</figure>

You can activate a different license by **re-installing Flair** again and choosing to **Delete the existing license**.

<figure class="aio-ui aio-window">
<img src="/media/maya/setup/activation/re-install_delete_license.png" alt="Installation dialog with Delete the existing license selected" />
<figcaption>Re-installation dialog with license deletion.</figcaption>
</figure>

1. Open the folder where Flair was installed from
2. Drag-and-drop the `install_maya.mel` file onto the Maya viewport
3. Within the installation dialog, check "Delete the existing license"
4. Proceed with the installation
4. Restart Maya
3. Load Flair to trigger the license activation again

## End-User-License-Agreements (EULAs)
The End-User-License-Agreements are the terms by which you can use Flair. These are normal in any type of software and serves as a legal contract to protect the developers of an application.

<figure class="aio-ui aio-window">
<img src="/media/maya/setup/activation/activation_eula.png" alt="End-User-License Agreement dialog" />
<figcaption>End-User-License Agreement (EULA).</figcaption>
</figure>

The EULAs for each version of Flair can be found below:
* [Flair Studio EULA](https://artineering.io/legal/flair-studio-eula)
* [Flair Indie EULA](https://artineering.io/legal/flair-indie-eula)
* [Flair Community EULA](https://artineering.io/legal/flair-community-eula)
* [Flair Free EULA](https://artineering.io/legal/flair-free-eula)

Once you have read and agreed to the End-User License Agreement, click on **I Agree**.

---

## FAQ
<details>

<summary>Whitelist URL and port on firewall for the Flair license to be validated</summary>

If you can't validate Flair on your workstation because your access to the internet is restricted by a firewall, add a whitelist rule for our licensing server: _api.keygen.sh_ on port 443.

</details>

<details>

<summary>I have not received my activation key</summary>

The email is most likely in your spam folder. Please double-check the spam folder of the email you entered or your _Patreon_ email (for _Community_ licenses).

If the license still has not arrived within an hour [contact us](https://artineering.io/contact) to help you get started.

</details>

<details>

<summary>Flair freezes on Linux during activation</summary>

If Maya freezes after claiming a license, it could be that the required QtWebEngine dependencies are not found. The easiest workaround is to add an environment variable to auto-accept the Flair EULA with `FLAIR_ACCEPT_EULA=1`.  
Yes, Linux can be a pain sometimes as every Linux distribution is different.

</details>

<details>

<summary>The viewport is all black and I get the Error compiling GLSL code on Windows.</summary>

This can happen when the viewport is forced to use DirectX (e.g., with an environment variable) instead of OpenGL. 

During installation, we try to automatically set the Viewport 2.0 rendering engine to OpenGL, but this can fail depending on your setup.  Check your Maya setup for anything that might force the viewport to use DirectX and remove it. Then, manually set the rendering engine to OpenGL (`Preferences->Display->Viewport 2.0->Rendering Engine->OpenGL Core Profile`). Maya will prompt to restart the application and Flair will be able to run after restarting.

</details>
